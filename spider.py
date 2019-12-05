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
    crawledSet = ''
    queueSet = ''
    def __init__(self,projectName,startURL,domainName):
        Spider.projectName = projectName
        Spider.startURL = startURL
        Spider.domainName = domainName
        Spider.queueFile = projectName+"/queue.txt"
        Spider.crawledFile = projectName + "/crawled.txt"
        self.start()
        self.crawl('Spider 1', Spider.startURL)

