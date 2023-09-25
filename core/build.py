import os
import json

class Build:

    def __init__(self):
        self._modules = []
        self._env = None

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value

    def get_module(self):
        return self._modules

    def add_module(self, module):
        module.build()
        self._modules.append(module)

    def build(self):
        if self._modules:
            # build all modules found in self._modules
            for each in self._modules:
                # each.build()
                path = os.path.join(self.env, '{}_{}_{}.json'.format(each.config.side, each.config.name,
                                                                     each.config.module))
                with open(path, 'w') as fh:
                    json.dump(each.config.__dict__, fh, indent=4)

            # handle all connections between each other
            for each in self._modules:
                pass
