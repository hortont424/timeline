from __future__ import print_function

import vobject

from .CalendarBackend import CalendarBackend, calendarBackend

from util import *
from schema import *

@calendarBackend("vcf")
class VCardCalendarBackend(CalendarBackend):
    def __init__(self, fileName, dataPath):
        super(VCardCalendarBackend, self).__init__(fileName, dataPath)

        vcevents = []

        try:
            for card in vobject.readComponents(readFile(fileName)):
                if hasattr(card, "bday"):
                    vcevents.append({"name": card.fn.value,
                                     "date": card.bday.value,
                                     "yearly": True})
            self.events = [Event(vcevent, title=self.title) for vcevent in vcevents]
        except Exception as e:
            print("Failed to load file {0}: {1}".format(fileName, str(e)))