from __future__ import print_function

from .CalendarFrontend import CalendarFrontend, calendarFrontend

import json
import uuid
import datetime
from unicodedata import normalize
from copy import deepcopy

@calendarFrontend("json", "application/json")
class JSONFrontend(CalendarFrontend):
    def __init__(self, events):
        super(JSONFrontend, self).__init__(events)

        jsonsrc = ""

        jsevents = [evt.simplify() for evt in sorted(events, key=lambda e:e.date.date)]

        self.js = json.dumps(jsevents, sort_keys=True, indent=4)

    def getFile(self):
        return self.js