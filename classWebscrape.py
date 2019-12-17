import requests
from bs4 import BeautifulSoup
import sys



class webScrap:

    def __init__(self,url):
        
        self.url=url
        print(self.url)
        self.file_jobs = open('Jobs.txt','a')
            #self.file_locations = open('Locations.txt', 'a')

    def openUrl(self):
        response = requests.get(self.url)
        print(response)
        data = response.text
        #print(data)
        
        self.soup = BeautifulSoup(data, 'html.parser')
        

    def job_Info(self):
        self.jobs_data = self.soup.find_all('div',{'class':'jobsearch-SerpJobCard'})
        for job_data in self.jobs_data[1:]:     
            self.jobs_title = job_data.find('a',{'class':'jobtitle'}).text
            self.location_tag = job_data.find('div',{'class':'location'})
            self.location = self.location_tag.text if self.location_tag else 'N/A'
            #print(self.jobs_titles)
            self.file_jobs.write(self.jobs_title + ' : ')
            self.file_jobs.write(self.location)
           # self.file_jobs.write('\n')
        #return self.jobs_titles

    
    def location(self):
        self.jobs_data = self.soup.find_all('div',{'class':'jobsearch-SerpJobCard'})
        for job_data in self.jobs_data[1:]:
           # self.location_tag = job_data.find('div',{'class':'location'})
           # self.location = self.location_tag.text if self.location_tag else 'N/A'
            #self.file_locations.write(self.location)
            self.file_locations.write('\n')
            print(self.location)            
        
    

    def saveInfo(self,file_location,file_Titles):
        self.file_jobs = open('Jobs.txt','w')
        self.file_location = open('Location.txt','a')
        self.file_location.write(file_location)
        self.file_jobs.write(file_Titles)

##
def main():
    open_queu = open('indeed/queue.txt','r+')
    read_queu = open_queu.read()
    read_queuList = read_queu.split("\n")
    for url in range(len(read_queuList)-1):
        myurl=webScrap(read_queuList[url])
        myurl.openUrl()
        myurl.job_Info()
        #myurl.location()
if __name__ == '__main__':    
    main()


        
        
