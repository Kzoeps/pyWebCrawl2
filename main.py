import threading
from queue import Queue
from spider import Spider
from extractDomain import *
from general import *
pjName = 'indeed'
startURL='https://www.indeed.com/q-USA-jobs.html'
domainName = getSubDomain(startURL)
queueFile = pjName+'/queue.txt'
crawledFile = pjName+'/crawled.txt'
numThreads = 12

threadQueue = Queue()
Spider(pjName,startURL,domainName)

# each link is a job and has to be crawled
def createJobs():
    for link in fileToSet(queueFile):
        threadQueue.put(link)
    threadQueue.join()
    crawl()

def crawl():
    queuedLinks  = fileToSet(queueFile)
    if len(queuedLinks)>0:
        print(str(len(queuedLinks))+' left to crawl')
        createJobs()
def createSpiders():
    for x in range(numThreads):
         t = threading.Thread(target=work)
         t.daemon = True
         t.start()
def work():
    while True:
        url = threadQueue.get()
        Spider.crawl(threading.current_thread().name, url)
        threadQueue.task_done()
createSpiders()
crawl()
