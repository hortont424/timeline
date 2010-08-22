import datetime

class Date(object):
    def __init__(self, d, includeDay=False):
        super(Date, self).__init__()

        self._date = d
        self._includeDay = includeDay

        if self._date:
            self.date = datetime.date(*(map(int, self._date.split("-"))))
        else:
            self.date = datetime.date.today() + datetime.timedelta(1000)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")