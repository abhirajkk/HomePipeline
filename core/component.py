from abc import ABC, abstractmethod
from maya import cmds


class Component(ABC):
    def __init__(self):
        self.guide = None
        self.chain = None
        self.data = Data()
        self.config = Data()
        self.config.hierarchy = ['zero', 'offset', 'ctrl']
        self.config.shape = 'circle'
        self.config.color = 17

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def post_build(self):
        pass

    @abstractmethod
    def pre_build(self):
        pass

    def build_chain(self):
        if self.guide:
            for each in self.guide:
                jnt = cmds.createNode('joint', n=each.replace('_guide', '_SJ'))
                cmds.matchTransform(jnt, each)

    def parent(self):
        cmds.parent(self.config.parent, self.data.zero)

    def build(self):
        self.pre_build()
        self.main()
        self.post_build()


class Data:
    def __init__(self, **kwargs):
        self._data = {}
        if kwargs:
            for key, value in kwargs.items():
                self.__dict__[key] = value

    def __getattr__(self, item):
        return self.__dict__.get(item)

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def update(self, **kwargs):
        for key, value in kwargs.items():
            self.__dict__[key] = value

