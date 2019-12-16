
from multiprocessing import Process, Queue
import threading
from graphics import*
from Cool_button import Button
from time import sleep
##import time
from queue import Queue
from spider import Spider
from extractDomain import *
from general import *
from classWebscrape import *
domainName = getSubDomain(startURL)
queueFile = pjName+'/queue.txt'
crawledFile = pjName+'/crawled.txt'
numThreads = 1

threadQueue = Queue()
Spider('indeed','https://www.indeed.com/q-USA-jobs.html',domainName)

# each link is a job and has to be crawled
def createJobs():
    for link in fileToSet(queueFile):
        threadQueue.put(link)
        print('progress')            
    threadQueue.join()
    crawl()
    
def openFile():    
    open_queu = open('Indeed/queue.txt','r+')
    read_queu = open_queu.read()
    read_queuList = read_queu.split("\n")
    
    for url in range(len(read_queuList)-1):        
        myurl=webScrap(read_queuList[url])
        myurl.openUrl()
        myurl.job_Info()
##       # myurl.location()
##        #total_url.append(url)        
##        #if len(total_url)>500:
##           # sys.exit()
##        #n+=1
##        if n>50:
##            sys.exit()
##        else:
##            pass
       

def crawl():
##    createSpiders()
    queuedLinks  = fileToSet(queueFile)
    if len(queuedLinks)>0:        
        #print(str(len(queuedLinks))+' left to crawl')
        createJobs()
        
def createSpiders():
    for x in range(numThreads):
         t = threading.Thread(target=work)
         t.daemon = True
         t.start()

def window():
    sleep(4)
    win=GraphWin('WEB scraping',600,600)
    win.setCoords(0.0,0.0,130.0,130.0)
def work():
    queuedLinks = fileToSet(queueFile)
    while True:
        url = threadQueue.get()
        Spider.crawl(threading.current_thread().name, url)
        threadQueue.task_done()
#def action():    
##    p1 = Process(target=crawl, args=())
##    p2 = Process(target = openFile, args=())
##    p1.start()
##    print('progress')
##    p2.start()
##    print('here')
##    p1.join()
##    p2.join()
createSpiders()

if __name__== '__main__':

    win=GraphWin('WEB scraping',600,600)
    win.setCoords(0.0,0.0,130.0,130.0)
    button1=Button(win,Point(60,35),30,12,'Exit Window')
    button2=Button(win,Point(15,120),25,15,'Stop_Program')
    button3=Button(win,Point(60,60),20,10,'start')

    
    pt  = win.getMouse()
    button2.activate()
    button3.activate()
##    start=time.time()
##    period = 1
    
    while not button1.isClicked(pt):            
        if button3.isClicked(pt):

            p1 = Process(target=crawl, args=())
            p2 = Process(target = openFile, args=())
            p1.start()
            p2.start()
            print('please wait')
            sleep(5)
            print('crawling')
            sleep(15)
            print('scraping the internet')
            sleep(15)
            print('creating files for jobs')
            sleep(15)
            print('Almost Done')
            p1.terminate()
            sleep(5)
            p2.terminate()                
            print('Done crawling')
            p1.join()            
            p2.join()
                  

        pt=win.getMouse()
    win.close()




