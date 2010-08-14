class Name(object):
    def __init__(self, n):
        super(Name, self).__init__()

        self._name = n

    def __str__(self):
        return self._name