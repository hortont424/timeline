from __future__ import print_function

from .CalendarFrontend import CalendarFrontend, calendarFrontend

import icalendar
import uuid

@calendarFrontend("ics")
class iCalendarFrontend(CalendarFrontend):
    def __init__(self, events):
        super(iCalendarFrontend, self).__init__(events)

        cal = icalendar.Calendar()
        cal.add('prodid', '-//LifeCalendar//hortont.com//')
        cal.add('version', '2.0')

        for event in events:
            icsevt = icalendar.Event()

            icsevt.add('summary', event.title + str(event.name))
            icsevt.add('dtstart', event.date.date)
            icsevt.add('dtstamp', event.date.date)
            icsevt.add('dtend', event.endDate.date)

            description = event.details

            if description:
                description += "\n\n"

            if isinstance(event.address, list):
                description += "\n\n".join([str(addr) for addr in event.address])
            else:
                if event.address:
                    description += str(event.address)

            icsevt.add('description', description.strip())

            icsevt.add('transp', "TRANSPARENT")
            icsevt['uid'] = uuid.uuid4().hex
            cal.add_component(icsevt)

        self.ics = cal.as_string()

    def getFile(self):
        return self.ics