
from multiprocessing import Process, Queue
import threading
from graphics import*
from Cool_button import Button
from time import sleep
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
##    Queued links serves as the basis on which the spider should crawl
    linkNo = 0
##    link No is the accumulator variable used to crawlthrough links
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
        sleep(5)
        j=j+1

    sleep(5)
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

##    Graphic variables -->
    jobName = Text(Point(15,90),'Job name')
    searchText = Text(Point(70,95),'Search Location')
    searchJobText = Text(Point(35,95),'Search Job')
    location = Text(Point(55,90),'Location')
    searchJob = Entry(Point(35,90),12)
    searchButton = Button(win,Point(92,90),8,6,'search')
    exitButton = Button(win,Point(80,20),7,6,'Exit')
    jobName.draw(win)
    location.draw(win)
    search = Entry(Point(70,90),12)
    searchJob.draw(win)
    search.draw(win)
    searchText.draw(win)
    searchJobText.draw(win)
##    Graphic variables end <--
    
    jobsFile = open('jobs.txt','r')
##    jobs.txt stores all the jobs scraped from indeed.com
    jobFiletext = jobsFile.read()
    jobsFileList = jobFiletext.split('\n')
    jobsFileList = jobsFileList[1:]
    jobFiletextLower = jobFiletext.lower()
    jobsFileListLower = jobFiletextLower.split('\n')
    jobsFileListLower = jobsFileListLower[1:]
    searchedList = []
##    searchedList is a list to store all of the jobs or locations that the user wants to search
    jobsLocsDrawnPos = []
    #jobsLocsDrawnPos is a list to store the Text objects of the work
    searchNotFound = False
##    SearchNotFound is a variable to test whether a search result has been null
    for job_location in range(1,len(jobsFileList)):
        jobsFileList[job_location] = jobsFileList[job_location].split(':')
        jobsFileListLower[job_location] = jobsFileListLower[job_location].split(':')
        # we split the list into a sublist of job name and location so that it is easier to access individually
    pos = 5
    for eachJob in range(10):
        if len(jobsFileList[eachJob][0])>27:
            jobText = jobsFileList[eachJob][0][0:27]+'...'
##            This is done since some of the names of jobs are long so it needed to be compressed
        else:
            jobText = jobsFileList[eachJob][0]
        displayJob = Text(Point(20,80-pos),jobText)
        displayJob.draw(win)
        locationText = jobsFileList[eachJob][1]
        displayLocation = Text(Point(65,80-pos),locationText)
        displayLocation.draw(win)
        jobsLocsDrawnPos.append([displayJob,displayLocation])
        pos +=5
    
    pt = win.getMouse()
    while exitButton.isClicked(pt)!=True:
        if searchButton.isClicked(pt):
            searchVar = search.getText().lower()
            searchJobVar = searchJob.getText().lower()
##            SearchVar and searchjobVar and entries for user to either search for a specific location of a job name
            pos = 5
            if searchJobVar == '':
                for eachJobLocation in range(len(jobsFileListLower)):
                    if searchVar in jobsFileListLower[eachJobLocation][1]:
                        searchedList.append(jobsFileList[eachJobLocation])
            else:
                for eachJobLocation in range(len(jobsFileListLower)):
                    if searchJobVar in jobsFileListLower[eachJobLocation][0]:
                        searchedList.append(jobsFileList[eachJobLocation])
                
            for eachDrawnText in range(len(jobsLocsDrawnPos)):
                jobsLocsDrawnPos[eachDrawnText][0].undraw()
                jobsLocsDrawnPos[eachDrawnText][1].undraw()
            jobsLocsDrawnPos = []
##            # jobsLocsDrawnPos is emptied in order to store the searched variables text objects
            if len(searchedList)>10:
                searchedList = searchedList[0:10]
##                since there are numerous jobs we split it to 10 in order for it to be easier to read
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
##                    writing the searched jobs onto the graphics
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
            
            
                
                    
        
                    
                    
            
    


