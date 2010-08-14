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

zeroTime = datetime.time(0, 0, 0)

data = json.loads(readFile("data/residence.cal"))

cal = icalendar.Calendar()
cal.add('prodid', '-//LifeCalendar//hortont.com//')
cal.add('version', '2.0')

for jsevent in data:
    icsevt = icalendar.Event()
    evt = Event(jsevent)

    icsevt.add('summary', evt.name)
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

startServer(cal.as_string())