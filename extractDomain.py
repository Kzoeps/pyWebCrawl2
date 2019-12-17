from urllib.parse import urlparse
def getDomain(url):
    try:
        return urlparse(url).netloc
    # just returns the domain name without file paths and protocols.
    except:
        print('something not working in extractDomain')
        return ''
# gets the second last and last element of the domain since the web crawler needs to make sure that it is in the right domain and not crawl different domains.
def getSubDomain(url):
    try:
        domainList = getDomain(url).split('.')
        return domainList[-2]+'.'+domainList[-1]
    # this returns the last and second last element of the domain which is the .com and what comes before that.
    except:
        print('something not working in extractDomain')
        return ''