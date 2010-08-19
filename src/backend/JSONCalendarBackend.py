from __future__ import print_function

import os
import json

from .CalendarBackend import CalendarBackend, calendarBackend

from util import *
from schema import *

@calendarBackend("json")
class JSONCalendarBackend(CalendarBackend):
    def __init__(self, fileName):
        super(JSONCalendarBackend, self).__init__()
        self.fileName = fileName

        fileBase = os.path.splitext(os.path.basename(fileName))[0]
        title = "({0}) ".format(fileBase.replace("-", " "))

        try:
            jsevents = json.loads(readFile(fileName))
            self.events = [Event(jsevent, title=title) for jsevent in jsevents]
        except Exception as e:
            print("Failed to load file {0}: {1}".format(fileName, str(e)))