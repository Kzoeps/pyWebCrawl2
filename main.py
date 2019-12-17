
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
startURL = 'https://www.indeed.com/q-USA-jobs.html'
domainName = getSubDomain(startURL)
pjName = 'indeed'
queueFile = pjName+'/queue.txt'
crawledFile = pjName+'/crawled.txt'
numThreads = 1

threadQueue = Queue()
Spider('indeed',startURL,domainName)

# each link is a job and has to be crawled
def createJobs():
    for link in fileToSet(queueFile):
        threadQueue.put(link)
        print('progress')            
    threadQueue.join()
    crawl()
    
def openFile():    
    open_queu = open('indeed/queue.txt','r+')
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
    win.setCoords(0.0,0.0,100.0,100.0)
    

##    button1=Button(win,Point(60,35),30,12,'Exit Window')
##    button2=Button(win,Point(15,120),25,15,'Stop_Program')
##    button3=Button(win,Point(60,60),20,10,'start')

##    click= Text(Point(50,50),'click anywhere')
##    click.draw(win)
##    button2.activate()
##    button3.activate()
##    start=time.time()
##    period = 1
    
##    while not button1.isClicked(pt):            
##        if button3.isClicked(pt):

    p1 = Process(target=work, args=())
    p2 = Process(target=openFile, args=())
##    p3 = Process(target = loading , args = (
##        ))
    p1.start()
    p2.start()
##    p3.start()
##    win.setBackground('black')
    loading_text=Text(Point(50,65),'LOADING...')
    loading_text.setTextColor('red')
    loading_text.setSize(20)
    loading_text.draw(win)
    name=[]    
    for k in range(1,7):
        name.append('rect'+str(k))
    x1=35
    y1=55
    x2=40
    y2=50
    n=0
    for i in range(6):
        name[i]=Rectangle(Point(x1,y1),Point(x2,y2))
        name[i].setFill('black')
        name[i].setOutline('black')
        name[i].draw(win)
        n=5
        x1+=n
        x2+=n
        y1=y1
        y2=y2

    j=0
    while not j>=6:
        name[j].setFill('red')
        sleep(7)
        j=j+1

    sleep(7)
    x1=35
    y1=55
    x2=40
    y2=50
    n=0
    for i in range(6):
        name[i].undraw()
        n=5
        x1+=n
        x2+=n
        y1=y1
        y2=y2

    loading_text.undraw()
##        

##    click.setText('please wait')

##    click.setText('crawling')
##    click.setText('scraping the internet')
##    click.setText('creating files for jobs')
##    click.setText('Almost Done')
    p1.terminate()
    p2.terminate()
##    p3.terminate()
##    click.setText('Done crawling')
    p1.join()            
    p2.join()
##    p3.join()
##    click.undraw()

    
##              
##    sleep(1)
##    win.close()

    jobName = Text(Point(20,90),'Job name')
    jobName.draw(win)
    location = Text(Point(55,90),'Location')
    location.draw(win)
    search = Entry(Point(70,90),10)
    searchText = Text(Point(70,95),'Search')
    search.draw(win)
    searchText.draw(win)
    searchButton = Button(win,Point(90,90),10,6,'search')
    jobsFile = open('jobs.txt','r')
    jobFiletext = jobsFile.read()
    jobsFileList = jobFiletext.split('\n')
    jobsFileList = jobsFileList[1:]
    jobFiletextLower = jobFiletext.lower()
    jobsFileListLower = jobFiletextLower.split('\n')
    jobsFileListLower = jobsFileListLower[1:]
    print(jobsFileList)
    searchedList = []
    jobsLocsDrawnPos = []
    searchNotFound = False
    for job_location in range(1,len(jobsFileList)):
        jobsFileList[job_location] = jobsFileList[job_location].split(':')
    pos = 5
    for eachJob in range(10):
        if len(jobsFileList[eachJob][0])>27:
            jobText = jobsFileList[eachJob][0][0:27]+'...'
        else:
            jobText = jobsFileList[eachJob][0]
        print(jobText)
        displayJob = Text(Point(20,80-pos),jobText)
        displayJob.draw(win)
        locationText = jobsFileList[eachJob][1]
        displayLocation = Text(Point(65,80-pos),locationText)
        displayLocation.draw(win)
        jobsLocsDrawnPos.append([displayJob,displayLocation])
        pos +=5
    exitButton = Button(win,Point(80,20),7,6,'Exit')
    pt = win.getMouse()
    while exitButton.isClicked(pt)!=True:
        if searchButton.isClicked(pt):
            searchVar = search.getText().lower()
            pos = 5

            for eachJobLocation in range(len(jobsFileListLower)):
                if searchVar in jobsFileListLower[eachJobLocation]:
                    searchedList.append(jobsFileList[eachJobLocation])
            for eachDrawnText in range(len(jobsLocsDrawnPos)):
                jobsLocsDrawnPos[eachDrawnText][0].undraw()
                jobsLocsDrawnPos[eachDrawnText][1].undraw()
            jobsLocsDrawnPos = []
            if len(searchedList)>10:
                searchedList = searchedList[0:10]
            if len(searchedList)>0:
                for eachSearched in range(len(searchedList)):
                    if len(searchedList[eachSearched][0])>27:
                        jobSearchText = searchedList[eachSearched][0][0:27]+'...   '
                    else:
                        jobSearchText = searchedList[eachSearched][0]
        
                    if len(searchedList[eachSearched][1])>27:
                        locationSearchText = searchedList[eachSearched][1][0:27]+'...   '
                    else:
                        locationSearchText = searchedList[eachSearched][1]
                    searchedJob = Text(Point(20,80-pos),jobSearchText)
                    searchedLocation = Text(Point(65,80-pos),locationSearchText)                    
                    searchedJob.draw(win)
                    searchedLocation.draw(win)
                    jobsLocsDrawnPos.append([searchedJob,searchedLocation])
                    pos+=5
              #  
            else:
                notFoundText = Text(Point(50,50),'Searched Text Not Found,\n Please search again!\n Thank You!')
                notFoundText.setSize(20)
                notFoundText.setTextColor('red')
                notFoundText.draw(win)
                searchNotFound = True
                
            search.setText('')
            searchedList = []
            
        pt = win.getMouse()
        if searchNotFound == True:
            notFoundText.undraw()
            searchNotFound = False
    win.close()
            
            
                
                    
        
                    
                    
            
    


