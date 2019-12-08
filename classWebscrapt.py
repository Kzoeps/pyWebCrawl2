import requests
from bs4 import BeautifulSoup


class webScrap:

    def __init__(self,url):
        self.url=url
        print(self.url)
        self.file_jobs = open('Jobs.txt','a')
        self.file_locations = open('Locations.txt', 'a')

    def openUrl(self):
        response = requests.get(self.url)
        print(response)
        data = response.text
        #print(data)
        
        self.soup = BeautifulSoup(data, 'html.parser')
        break

    def job_Info(self):
        self.jobs_data = self.soup.find_all('p',{'class':'result-info'})
        for job_data in self.jobs_data[1:]:     
            self.jobs_title = job_data.find('a',{'class':'result-title'}).text            
            #print(self.jobs_titles)
            self.file_jobs.write(self.jobs_title)
            self.file_jobs.write('\n')
        #return self.jobs_titles
    
    def location(self):
        self.jobs_data = self.soup.find_all('p',{'class':'result-info'})
        for job_data in self.jobs_data[1:]:
            self.location_tag = job_data.find('span',{'class':'result-hood'})
            self.location = self.location_tag.text[2:-1] if self.location_tag else 'N/A'
            self.file_locations.write(self.location)
            self.file_locations.write('\n')
            print(self.location)            
        
    

    def saveInfo(self,file_location,file_Titles):
        self.file_jobs = open('Jobs.txt','w')
        self.file_location = open('Location.txt','a')
        self.file_location.write(file_location)
        self.file_jobs.write(file_Titles)


def main():
    myurl=webScrap('https://accounts.craigslist.org/login?rt=L&rp=%2Flogin%2Fhome')

    myurl.openUrl()
    #myurl.job_Info()
    myurl.job_Info()
    myurl.location()
    #file_location = myurl.location()
    #myurl.saveInfo(file_location,file_Titles)
    
main()

        
        
