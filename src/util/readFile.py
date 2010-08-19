import codecs

def readFile(fileName):
    fileHandle = codecs.open(fileName, encoding='utf-8')
    fileContents = unicode(fileHandle.read())
    fileHandle.close()
    return fileContents