class SchemaObject(object):
    knownKeys = []

    def __init__(self, obj):
        super(SchemaObject, self).__init__()

        for k in obj.keys():
            if k not in self.knownKeys:
                raise Exception("Invalid key '{0}' in {1}".format(k, type(self).__name__))

            setattr(self, "_" + k, obj[k])
