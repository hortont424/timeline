class SchemaObject(object):
    knownKeys = []
    outputKeys = []

    def __init__(self, obj):
        super(SchemaObject, self).__init__()

        for k in obj.keys():
            if k not in self.knownKeys:
                raise Exception("Invalid key '{0}' in {1}".format(k, type(self).__name__))

            setattr(self, "_" + k, obj[k])

    def simplify(self):
        freshObject = {}

        for k in self.outputKeys:
            if not hasattr(self, k):
                continue

            attrValue = getattr(self, k)

            if isinstance(attrValue, SchemaObject):
                attrValue = attrValue.simplify()

            if isinstance(attrValue, list):
                attrValue = [av.simplify() for av in attrValue]

            freshObject[k] = attrValue

        return freshObject