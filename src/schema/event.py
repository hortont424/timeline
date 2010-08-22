from .schemaObject import SchemaObject

from .address import Address
from .name import Name
from .date import Date

class Event(SchemaObject):
    knownKeys = ["name", "address", "date", "details", "participants", "yearly"]

    def __init__(self, obj, title=""):
        super(Event, self).__init__(obj)

        self.title = title

        if hasattr(self, "_address"):
            if isinstance(self._address, list):
                self.address = [Address(a) for a in self._address]
            else:
                self.address = Address(self._address)
        else:
            self.address = None

        if hasattr(self, "_date"):
            if isinstance(self._date, list):
                if len(self._date) == 1:
                    self.date = Date(self._date[0])
                    self.endDate = Date(None)
                elif len(self._date) == 2:
                    self.date = Date(self._date[0])
                    self.endDate = Date(self._date[1])
                else:
                    raise Exception("Too many dates!")
            else:
                self.date = Date(self._date)
                self.endDate = self.date
        else:
            raise Exception("Not enough dates!!")

        if hasattr(self, "_name"):
            self.name = Name(self._name)
        else:
            self.name = Name("Unnamed Event")

        if hasattr(self, "_details"):
            self.details = self._details
        else:
            self.details = ""

        if hasattr(self, "_yearly"):
            self.yearly = self._yearly
        else:
            self.yearly = False

    def __str__(self):
        outStr = str(self.name)

        if self.date:
            if self.endDate:
                if self.date == self.endDate:
                    outStr += " ({0})".format(self.date)
                else:
                    outStr += " ({0} -> {1})".format(self.date, self.endDate)
            else:
                outStr += " ({0} -> present)".format(self.date)

        return outStr