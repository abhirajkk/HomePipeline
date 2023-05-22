import pymel.core as pm
from importlib import reload
from ..core import coreMeta
reload(coreMeta)

from ..functions import attrFn
reload(attrFn)


class Control:
    def __init__(self, name, config):
        # self._hierarchy = ['zero', 'offset', 'ctrl']
        self.control_name = name
        self._control_data = {}
        self.config = config

    def build(self):
        nodes = []
        for i, each in enumerate(self.config.hierarchy):
            grp = pm.createNode('transform', n='{}_{}'.format(self.control_name, each))
            nodes.append(grp)
            self._control_data[each] = grp.name()
            if i > 0:
                pm.parent(nodes[i], nodes[i-1])
            if each == self._hierarchy[-1]:
                self.lock_translate(grp, self.translate)
                self.lock_rotate(grp, self.rotate)
                self.lock_scale(grp, self.scale)
                self.lock_visibility(grp, self.visibility)

    def __getattr__(self, item):
        return self._control_data.get(item)
    #
    # @property
    # def hierarchy(self):
    #     return self._hierarchy
    #
    # @hierarchy.setter
    # def hierarchy(self, value):
    #     self._hierarchy = value

    def lock_translate(self, node, value):
        self.lock(node, value, 'translate')

    def lock_rotate(self, node, value):
        self.lock(node, value, 'rotate')

    def lock_scale(self, node, value):
        self.lock(node, value, 'scale')

    def lock_visibility(self, node, value):
        self.lock(node, value, 'visibility')

    @staticmethod
    def lock(node, value, attr_type):
        if isinstance(value, bool):
            if value is True:
                if attr_type == 'translate':
                    attrFn.AttrFn.lock_attr(node, ('tx', 'ty', 'tz'))
                elif attr_type == 'rotate':
                    attrFn.AttrFn.lock_attr(node, ('rx', 'ry', 'rz'))
                elif attr_type == 'scale':
                    attrFn.AttrFn.lock_attr(node, ('sx', 'sy', 'sz'))
                else:
                    attrFn.AttrFn.lock_attr(node, ['v'])
        else:
            attrFn.AttrFn.lock_attr(node, value)

