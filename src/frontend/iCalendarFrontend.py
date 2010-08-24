from __future__ import print_function

from .CalendarFrontend import CalendarFrontend, calendarFrontend

import icalendar
import uuid
import datetime
from unicodedata import normalize

@calendarFrontend("ics", "text/calendar")
class iCalendarFrontend(CalendarFrontend):
    def __init__(self, events):
        super(iCalendarFrontend, self).__init__(events)

        cal = icalendar.Calendar()
        cal.add('prodid', '-//Timeline//hortont.com//')
        cal.add('version', '2.0')

        for event in events:
            icsevt = icalendar.Event()

            icsevt.add('summary', normalize("NFKD", u"({0}) ".format(event.title)) +
                                  normalize("NFKD", unicode(event.name)))
            icsevt.add('dtstart', event.date.date)
            icsevt.add('dtstamp', event.date.date)
            # This seems particularly hacky. Why is iCal not inclusive of
            # ending date?
            icsevt.add('dtend', event.endDate.date + datetime.timedelta(days=1))

            if event.yearly:
                icsevt.add('rrule', {"FREQ": "YEARLY", "INTERVAL": 1})

            description = event.details

            if description:
                description += "\n\n"

            if isinstance(event.address, list):
                description += "\n\n".join([str(addr) for addr in event.address])
            else:
                if event.address:
                    description += str(event.address)

            icsevt.add('description',
                       normalize("NFKD", unicode(description.strip())))

            icsevt.add('transp', "TRANSPARENT")
            icsevt['uid'] = uuid.uuid4().hex
            cal.add_component(icsevt)

        self.ics = cal.as_string()

    def getFile(self):
        return self.ics