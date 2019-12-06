from urllib.request import urlopen
from findLinks import findLinks
from general import *
# Spider class is a class to initiate spiders to crawl the web
class Spider:
    # global variables declared since all instances of spider should refer to the same variables rather than having their own instances.
    projectName = ''
    startURL = ''
    domainName = ''
    # need domain name for the same reason that in HTML you can write the file path and not the full domain.
    crawledFile = ''
    queueFile = ''
    crawledSet = set()
    queueSet = set()

    @staticmethod
    def start():
        createrDir(Spider.projectName)
        createFiles(Spider.projectName, Spider.startURL)
        # since the first spider needs to intiate the directory and the related files but also add the the startURL to the queue.txt file
        Spider.queueSet = fileToSet(Spider.queueFile)
        # making content in the files to queue so as to make the web crawling faster
        Spider.crawledSet = fileToSet(Spider.crawledFile)

    @staticmethod
    def crawl(spiderName, pageURL):
        if pageURL not in Spider.crawledSet:
            #         to make sure to not crawl a file thats already been crawled.
            print(spiderName + ' crawling ' + pageURL)
            print('Queue: ' + str(len(Spider.queueSet)))
            print('Crawled: ' + str(len(Spider.crawledSet)))
            Spider.addToQueue(Spider.getLinks(pageURL))
            Spider.queueSet.remove(pageURL)
            # removes the pageURL from the queueset since its been crawled and adds it to the crawled set.
            Spider.crawledSet.add(pageURL)
            Spider.updateFile()
    @staticmethod
    def getLinks(pageURL):
        try:
            print(pageURL, 'page url')
            response = urlopen(pageURL)
            if response.getheader('Content-Type')=="text/html":
                htmlInbinary = response.read()
                htmlInString = htmlInbinary.decode('utf-8')
                print(htmlInString)
            finder = findLinks(Spider.startURL,pageURL)
            finder.feed(htmlInString)
        except:
            print('Somethings not working')
            return set()
        return finder.pageLinks()
    @staticmethod
    def addToQueue(links):
        for url in links:
            if url in Spider.queueSet:
                continue
            elif url in Spider.crawledSet:
                continue
            elif Spider.domainName not in url:
                continue
            else:
                Spider.queueSet.add(url)
    @staticmethod
    def updateFile():
        setToFile(Spider.queueSet,Spider.queueFile)
        setToFile(Spider.crawledSet,Spider.crawledFile)

    def __init__(self,projectName,startURL,domainName):
        Spider.projectName = projectName
        Spider.startURL = startURL
        Spider.domainName = domainName
        Spider.queueFile = projectName+"/queue.txt"
        Spider.crawledFile = projectName + "/crawled.txt"
        self.start()
        # start function is
        self.crawl('Spider 1', Spider.startURL)
