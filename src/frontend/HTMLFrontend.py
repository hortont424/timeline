from __future__ import print_function

from .CalendarFrontend import CalendarFrontend, calendarFrontend

import icalendar
import datetime
from unicodedata import normalize
from array import array
from random import random

pointsPerDay = 1
pointsPerEvent = 50

@calendarFrontend("html", "text/html")
class HTMLFrontend(CalendarFrontend):
    def __init__(self, events):
        super(HTMLFrontend, self).__init__(events)

        self.width = pointsPerDay * self.totalDays
        self.height = 500

        self.titleColors = {}
        self.dayDescent = array('L', [0] * (self.totalDays + 1))

        self.html = ""

        for event in sorted(events, key=lambda e:(e.date.date - e.endDate.date).days):
            self.html += self.generateEvent(event)

    def generateEvent(self, event, offset=None):
        startDay = (event.date.date - self.earliestDate).days
        endDay = (event.endDate.date - self.earliestDate).days + 1

        rangeDescent = max(self.dayDescent[startDay:endDay])

        x1 = pointsPerDay * startDay
        x2 = pointsPerDay * endDay
        y1 = rangeDescent * pointsPerEvent
        y2 = y1 + pointsPerEvent

        for day in range(startDay, endDay):
            self.dayDescent[day] = rangeDescent + 1

        if event.title not in self.titleColors:
            # TODO: decent colors, please
            newColor = (random() * 255, random() * 255, random() * 255)
            self.titleColors[event.title] = '#%02x%02x%02x' % newColor

        return "<div style='position: absolute; left: {0}; top: {1}; width: {2}; height: {3}; background-color: {4};'></div>".format(x1, y1, x2 - x1, y2 - y1, self.titleColors[event.title])

    def getFile(self):
        return self.html
