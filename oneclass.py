
class foo(object):
    i = None

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_instance(cls):
        if cls.i:
            return cls.i
        else:
            obj = cls('hexm')
            cls.i = obj
            return obj