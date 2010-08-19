import datetime

class Date(object):
    def __init__(self, d, includeDay=False):
        super(Date, self).__init__()

        self._date = d

        if self._date:
            self.date = datetime.date(*(map(int, self._date.split("-"))))
        else:
            self.date = datetime.date.today() + datetime.timedelta(1000)

        # This seems particularly hacky. Why is iCal not inclusive of
        # ending date?
        if includeDay:
            self.date += datetime.timedelta(days=1)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")