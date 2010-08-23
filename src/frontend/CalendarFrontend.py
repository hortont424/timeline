from __future__ import print_function

calendarFrontends = {}

def calendarFrontend(name, mimetype):
    def wrap(cls):
        calendarFrontends[name] = (cls, mimetype)
        return cls
    return wrap

def getCalendarFrontend(name):
    if name in calendarFrontends:
        return calendarFrontends[name]
    else:
        return None

class CalendarFrontend(object):
    def __init__(self, events):
        super(CalendarFrontend, self).__init__()

        self.events = events

        self.earliestDate = events[0].date.date
        self.latestDate = events[0].date.date

        for event in events:
            self.earliestDate = min(self.earliestDate, event.date.date, event.endDate.date)
            self.latestDate = max(self.latestDate, event.date.date, event.endDate.date)

        print(self.earliestDate, self.latestDate)

        self.totalDays = (self.latestDate - self.earliestDate).days

    def getFile(self):
        warn("Abstract method!")
        exit(9)