import pymel.core as pm
from ..core import module

from importlib import reload
reload(module)


class DagNode(module.Base):

    def __init__(self, name):
        super(DagNode, self).__init__(name)
        self._hierarchy = ['zero', 'offset', 'ctrl']
        self.control_name = 'name'
        print("Ran Dag node init")

    def build_dag(self):
        nodes = []
        for i, each in enumerate(self.hierarchy):
            grp = pm.createNode('transform', n='{}_{}'.format(self.control_name, each))
            nodes.append(grp)
            if i > 0:
                pm.parent(nodes[i], nodes[i-1])
            setattr(self, each, grp.name())

    @classmethod
    def lock_translate(cls, node, value=True, attrs=('tx', 'ty', 'tz')):
        cls.lock_attr(node, value, attrs)

    @classmethod
    def lock_rotate(cls, node, value=True, attrs=('rx', 'ry', 'rz')):
        cls.lock_attr(node, value, attrs)

    @classmethod
    def lock_scale(cls, node, value=True, attrs=('sx', 'sy', 'sz')):
        cls.lock_attr(node, value, attrs)

    @staticmethod
    def lock_attr(node, value, attrs):
        if value:
            for att in attrs:
                pm.PyNode(node).attr(att).lock()
                pm.PyNode(node).attr(att).setKeyable(False)
        else:
            for att in attrs:
                pm.PyNode(node).attr(att).unlock()
                pm.PyNode(node).attr(att).setKeyable(True)

    @property
    def hierarchy(self):
        return self._hierarchy

    @hierarchy.setter
    def hierarchy(self, value):
        self._hierarchy = value
