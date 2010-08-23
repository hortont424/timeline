from __future__ import print_function

import os

calendarBackends = {}

def calendarBackend(extension):
    def wrap(cls):
        if extension in calendarBackends:
            print("Extension {0} already claimed by {1}.".format(extension,
                str(calendarBackends[extension])))
            exit(8)

        calendarBackends[extension] = cls
        return cls
    return wrap

def getCalendarBackend(extension):
    if extension in calendarBackends:
        return calendarBackends[extension]
    else:
        return None

class CalendarBackend(object):
    def __init__(self, fileName, dataPath):
        super(CalendarBackend, self).__init__()

        fileBase = os.path.splitext(os.path.basename(fileName))[0]
        dirName = os.path.dirname(os.path.relpath(fileName, dataPath))

        self.fileName = fileName
        self.dataPath = dataPath
        self.events = None

        if dirName:
            self.title = "({0} - {1}) ".format(dirName.replace("-", " "),
                                               fileBase.replace("-", " "))
        else:
            self.title = "({0}) ".format(fileBase.replace("-", " "))
