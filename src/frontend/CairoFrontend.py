from __future__ import print_function

from .CalendarFrontend import CalendarFrontend, calendarFrontend

import icalendar
import datetime
import cairo
import StringIO
from unicodedata import normalize
from array import array

pointsPerDay = 5
pointsPerEvent = 50

@calendarFrontend("pdf", "application/pdf")
class CairoFrontend(CalendarFrontend):
    def __init__(self, events):
        super(CairoFrontend, self).__init__(events)

        self.width = pointsPerDay * self.totalDays
        self.height = 500

        surfaceData = StringIO.StringIO()
        surface = cairo.PDFSurface(surfaceData, self.width, self.height)
        self.ctx = cairo.Context(surface)

        #for x in range(0, width, pointsPerDay):
        #    self.ctx.move_to(x, 0)
        #    self.ctx.line_to(x, height)
        #    self.ctx.stroke()

        self.dayDescent = array('L', [0] * (self.totalDays + 1))

        for event in sorted(events, key=lambda e:(e.date.date - e.endDate.date).days):
            self.drawEvent(event)

        surface.finish()
        self.pdf = surfaceData.getvalue()

    def drawEvent(self, event, offset=None):
        startDay = (event.date.date - self.earliestDate).days
        endDay = (event.endDate.date - self.earliestDate).days + 1

        x1 = pointsPerDay * startDay
        x2 = pointsPerDay * endDay
        y1 = max(self.dayDescent[startDay:endDay]) * pointsPerEvent
        y2 = y1 + pointsPerEvent

        for day in range(startDay, endDay):
            self.dayDescent[day] += 1

        self.ctx.rectangle(x1, y1, x2 - x1, y2 - y1)
        self.ctx.fill()

    def getFile(self):
        return self.pdf
