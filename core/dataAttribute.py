from ..core import coreMeta
from importlib import reload
reload(coreMeta)


class DataClass:
    def __init__(self, **kwargs):

        # internal attributes
        self.guide = None
        self.bind = {}
        self.inputs = {}
        self.outputs = {}
        self.controls = {}

        # override by user input
        for key, value in kwargs.items():
            if key in self.__dict__:
                self.__dict__[key] = value

    def __getattr__(self, item):
        return self.controls[item]


class RigConfig:
    def __init__(self, **kwargs):
        self.name = 'fk'
        self.component = None
        self.module = None
        self.side = 'M'
        self.color = 17
        self.lock_visibility = True
        self.lock_translate = False
        self.lock_rotate = False
        self.lock_scale = False
        self.hierarchy = ['zero', 'offset', 'ctrl']

        # override by user input
        for key, value in kwargs.items():
            if key in self.__dict__:
                self.__dict__[key] = value

