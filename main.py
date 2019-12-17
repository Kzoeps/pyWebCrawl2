
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
def openFile():    
    open_queu = open('indeed/queue.txt','r+')
    read_queu = open_queu.read()
    read_queuList = read_queu.split("\n")
    
    for url in range(len(read_queuList)-1):        
        myurl=webScrap(read_queuList[url])
        myurl.openUrl()
        myurl.job_Info()
def window():
    sleep(4)
    win=GraphWin('WEB scraping',600,600)
    win.setCoords(0.0,0.0,130.0,130.0)
def work():
    queuedLinks = fileToSet(queueFile)
    linkNo = 0
    while len(queuedLinks)>0:
        url = queuedLinks[linkNo]
        Spider.crawl('Spider 1', url)
        linkNo += 1


if __name__== '__main__':
    win=GraphWin('WEB scraping',800,600)
    win.setCoords(0.0,0.0,100.0,100.0)

    p1 = Process(target=work, args=())
    p2 = Process(target=openFile, args=())
    p1.start()
    p2.start()
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
        sleep(0.5)
        j=j+1

    sleep(0.5)
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
    p1.terminate()
    p2.terminate()
    p1.join()            
    p2.join()


    jobName = Text(Point(15,90),'Job name')
    jobName.draw(win)
    location = Text(Point(55,90),'Location')
    location.draw(win)
    search = Entry(Point(70,90),12)
    searchJob = Entry(Point(35,90),12)
    searchJob.draw(win)
    searchText = Text(Point(70,95),'Search Location')
    searchJobText = Text(Point(35,95),'Search Job')
    search.draw(win)
    searchText.draw(win)
    searchJobText.draw(win)
    searchButton = Button(win,Point(92,90),8,6,'search')
    jobsFile = open('jobs.txt','r')
    jobFiletext = jobsFile.read()
    jobsFileList = jobFiletext.split('\n')
    jobsFileList = jobsFileList[1:]
    jobFiletextLower = jobFiletext.lower()
    jobsFileListLower = jobFiletextLower.split('\n')
    jobsFileListLower = jobsFileListLower[1:]
    searchedList = []
    jobsLocsDrawnPos = []
    searchNotFound = False
    for job_location in range(1,len(jobsFileList)):
        jobsFileList[job_location] = jobsFileList[job_location].split(':')
        jobsFileListLower[job_location] = jobsFileListLower[job_location].split(':')
    pos = 5
    for eachJob in range(10):
        if len(jobsFileList[eachJob][0])>27:
            jobText = jobsFileList[eachJob][0][0:27]+'...'
        else:
            jobText = jobsFileList[eachJob][0]
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
            searchJobVar = searchJob.getText().lower()
            pos = 5
            if searchJobVar == '':
                for eachJobLocation in range(len(jobsFileListLower)):
                    if searchVar in jobsFileListLower[eachJobLocation][1]:
                        searchedList.append(jobsFileList[eachJobLocation])
##                        searchedJobsAndLocationsFile.write(str('hi]'))
            else:
                for eachJobLocation in range(len(jobsFileListLower)):
                    if searchJobVar in jobsFileListLower[eachJobLocation][0]:
                        searchedList.append(jobsFileList[eachJobLocation])
##                        searchedJobsAndLocationsFile.write(str('hi'))
                
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
            else:
                notFoundText = Text(Point(50,50),'Searched Text Not Found,\n Please search again!\n Thank You!')
                notFoundText.setSize(20)
                notFoundText.setTextColor('red')
                notFoundText.draw(win)
                searchNotFound = True
                
            search.setText('')
            searchJob.setText('')
            searchedList = []
            
        pt = win.getMouse()
        if searchNotFound == True:
            notFoundText.undraw()
            searchNotFound = False
    win.close()
            
            
                
                    
        
                    
                    
            
    


