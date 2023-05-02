import pymel.core as pm
from importlib import reload
from ..core import coreMeta
reload(coreMeta)


class Control:
    def __init__(self, name):
        self._hierarchy = ['zero', 'offset', 'ctrl']
        self.control_name = name
        self._node = None
        self._control_data = {}

    def build(self):
        nodes = []
        for i, each in enumerate(self._hierarchy):
            grp = pm.createNode('transform', n='{}_{}'.format(self.control_name, each))
            nodes.append(grp)
            self._control_data[each] = grp.name()
            if i > 0:
                pm.parent(nodes[i], nodes[i-1])

    def __getitem__(self, item):
        return self._control_data.get(item)

    @property
    def hierarchy(self):
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, value):
        self._hierarchy = value



