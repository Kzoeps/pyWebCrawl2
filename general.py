import os
# import the operating system library
def createrDir(directory):
    if not os.path.exists(directory):
        # checks if the directory already exists or not by checking if the path already exists or not
        print('creating directory for "'+directory+'"')
        os.makedirs(directory)
#         creates a directory
# create queued and crawled files

def createFiles(project, startURL):
    queueFile = project + '/queue.txt'
    # a variable which stores the path of the queue file.
    crawledFile = project + '/crawled.txt'
    # a variable which stores the path of the crawled file.
    if not os.path.isfile(queueFile):
        # checks if file is present or not
        newFile(queueFile, startURL)
    if not os.path.isfile(crawledFile):
        newFile(crawledFile, '')

# newFile is a function to create a new file.
def newFile(name, data):
    file = open(name,'w')
    file.write(data)
    file.close()

# writing data onto an existing file
def writeToFile(name,data):
    with open(name,'a') as file:
        file.write(data+'\n')

# delete data of an existing file.
def deleteContents(path):
    with open(path,'w'):
        pass
# using a set since it does not allow duplication since that is needed to make sure duplicate links are not copied.
# Read the crawled or queue files and convert to set.
def fileToSet(fileName):
    convertedSet = set()
    with open(fileName,'rt') as f:
        for eachline in f:
            convertedSet.add(eachline.replace('\n',''))
#             adding all links to the set
    return convertedSet
# converting a set to a file.
def setToFile(linksSet, fileName):
    deleteContents(fileName)
    for eachLink in linksSet:
        writeToFile(fileName, eachLink)

