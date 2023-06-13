from abc import ABC, abstractmethod
from maya import cmds
import json
import os
from .. import project_settings


class Component(ABC):
    def __init__(self):
        self.guide = None
        self.chain = None
        self.data = Data()
        self.config = Data()
        self.config.hierarchy = ['zero', 'offset', 'ctrl']
        self.config.shape = 'circle'
        self.config.color = 17
        self.config.lock_translate = False
        self.config.lock_rotate = False
        self.config.lock_scale = False
        self.config.lock_visibility = True

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
        if self.config.__dict__.get('build'):
            path = os.path.join(self.config.build, '{}_{}_{}.json'.format(self.config.side, self.config.name,
                                                                          self.config.module))
            with open(path, 'w') as fh:
                json.dump(self.config.__dict__, fh, indent=4)

    def attach(self):
        pass


class Data:
    def __init__(self, **kwargs):
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

