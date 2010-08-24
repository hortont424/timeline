from .schemaObject import SchemaObject

class Name(SchemaObject):
    def __init__(self, n):
        self._name = n

    def __str__(self):
        return self._name

    def simplify(self):
        return unicode(self)