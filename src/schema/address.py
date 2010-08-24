from .schemaObject import SchemaObject

class Address(SchemaObject):
    knownKeys = ["name", "street", "city", "state", "country", "zipCode"]

    def __init__(self, obj):
        super(Address, self).__init__(obj)

    def __str__(self):
        outStr = ""

        if hasattr(self, "_street"):
            if isinstance(self._street, list):
                outStr += "\n".join(self._street)
            else:
                outStr += self._street

        outStr += "\n"

        if hasattr(self, "_name"):
            outStr += self._name + " "

        if hasattr(self, "_city"):
            outStr += self._city + " "

        if hasattr(self, "_state"):
            outStr += self._state + " "

        if hasattr(self, "_zipCode"):
            outStr += self._zipCode + " "

        if hasattr(self, "_country"):
            outStr += "\n"
            outStr += self._country

        return outStr