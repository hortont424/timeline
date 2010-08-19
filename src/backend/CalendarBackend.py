from __future__ import print_function

calendarBackends = {}

def calendarBackend(extension):
    def wrap(cls):
        calendarBackends[extension] = cls
        return cls
    return wrap

def getCalendarBackend(extension):
    if extension in calendarBackends:
        return calendarBackends[extension]
    else:
        return None

class CalendarBackend(object):
    def __init__(self):
        super(CalendarBackend, self).__init__()
        self.events = None