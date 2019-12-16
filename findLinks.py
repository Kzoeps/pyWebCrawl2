from html.parser import *
from urllib import parse
# htmlParser is a library for parsing html.
class findLinks(HTMLParser):
    # def error has to be written for HTMLParser since its a requirement for exception handling
    #def error(self, message):
     #   print('somethings not working in findLinks')
      #  pass
    def __init__(self,startURL, pageURL):
        super().__init__()
        self.startURL = startURL
        self.pageURL = pageURL
        self.allLinks = set()
    #     allLinks is a set to store the links.
    def handle_starttag(self, tag, attrs):
        # this function only handles the start tag of HTML and not the closing tag
        if tag == 'a':
            for (attribute, value) in attrs:
    #             it goes through all the attributes and value in the a tag.
                if attribute == "href":
                    url = parse.urljoin(self.startURL,value)
#                     needed since in html links can be written without the home page url and just the file path parse url join, joins homepage and startURL
                    self.allLinks.add(url)
    def pageLinks(self):
        return self.allLinks
if __name__ == '__main__':
    def main():
        finder = findLinks('https://www.bbc.com/','bbc.com')
        finder.feed('<html><head><a href = "/askdnfjaksjdnf"><body>')
# .feed is used to parse the html in the object.
