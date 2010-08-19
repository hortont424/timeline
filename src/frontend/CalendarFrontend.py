from __future__ import print_function

calendarFrontends = {}

def calendarFrontend(name):
    def wrap(cls):
        calendarFrontends[name] = cls
        return cls
    return wrap

class CalendarFrontend(object):
    def __init__(self, events):
        super(CalendarFrontend, self).__init__()

        self.events = events

    def getFile(self):
        warn("Abstract method!")
        exit(9)