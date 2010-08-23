from __future__ import print_function

import json

from .CalendarBackend import CalendarBackend, calendarBackend

from util import *
from schema import *

@calendarBackend("json")
class JSONCalendarBackend(CalendarBackend):
    def __init__(self, fileName, dataPath):
        super(JSONCalendarBackend, self).__init__(fileName, dataPath)

        try:
            jsevents = json.loads(readFile(fileName))
            self.events = [Event(jsevent, title=self.title) for jsevent in jsevents]
        except Exception as e:
            print("Failed to load file {0}: {1}".format(fileName, str(e)))