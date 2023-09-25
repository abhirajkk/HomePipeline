from abc import ABC, abstractmethod
from maya import cmds
import json
import os
from .. import project_settings


class Component(ABC):
    def __init__(self):
        self.guide = None
        self.chain = None
        self.data = []
        self.controls = []
        self.joints = []
        self._attach_module = None
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
            for i, each in enumerate(self.guide):
                self.joints.append(cmds.createNode('joint', n=each.replace('_JNT', '_SJ'), p=self.data[i].ctrl))

    def build(self):
        self.pre_build()
        self.main()
        self.post_build()
        # if self.config.__dict__.get('build'):
        #     path = os.path.join(self.config.build, '{}_{}_{}.json'.format(self.config.side, self.config.name,
        #                                                                   self.config.module))
        #     with open(path, 'w') as fh:
        #         json.dump(self.config.__dict__, fh, indent=4)

    @property
    def attach_module(self):
        return self._attach_module

    @attach_module.setter
    def attach_module(self, value):
        self._attach_module = value


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

