from schema import *
from server import startServer

import datetime
import os
import json
import codecs
import string
import re
import sys
import uuid

import icalendar

def readFile(fn):
    fileHandle = codecs.open(fn, encoding='utf-8')
    fileContents = unicode(fileHandle.read())
    fileHandle.close()
    return fileContents

cal = icalendar.Calendar()
cal.add('prodid', '-//LifeCalendar//hortont.com//')
cal.add('version', '2.0')

for root, dirs, files in os.walk("data"):
    for file in files:
        fileBase, fileExtension = os.path.splitext(os.path.basename(file))

        if not fileExtension.lower().endswith("cal"):
            continue

        prefix = "({0}) ".format(fileBase.replace("-", " "))

        print "Loading {0} ...".format(file),

        try:
            jsevents = json.loads(readFile(os.path.join(root, file)))
        except Exception as e:
            print "failed (invalid file: {0})!".format(str(e))
            continue

        for jsevent in jsevents:
            icsevt = icalendar.Event()
            evt = Event(jsevent)

            icsevt.add('summary', prefix + str(evt.name))
            icsevt.add('dtstart', evt.date.date)
            icsevt.add('dtstamp', evt.date.date)
            icsevt.add('dtend', evt.endDate.date)

            description = ""
            if isinstance(evt.address, list):
                description = "\n\n".join([str(addr) for addr in evt.address])
            else:
                description = str(evt.address)
            icsevt.add('description', description)

            icsevt.add('transp', "TRANSPARENT")
            icsevt['uid'] = uuid.uuid4().hex
            cal.add_component(icsevt)

        if len(jsevents) == 1:
            print "got {0} event!".format(len(jsevents))
        else:
            print "got {0} events!".format(len(jsevents))

startServer(cal.as_string())