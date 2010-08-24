from .schemaObject import SchemaObject

import datetime

class Date(SchemaObject):
    def __init__(self, d):
        self._date = d

        if self._date:
            self.date = datetime.date(*(map(int, self._date.split("-"))))
        else:
            self.date = datetime.date.today() + datetime.timedelta(1000)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

    def simplify(self):
        return unicode(self)