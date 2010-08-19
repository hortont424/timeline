from __future__ import print_function

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
    def __init__(self):
        super(CalendarBackend, self).__init__()
        self.events = None