import pymel.core as pm
from importlib import reload

from ..functions import attrFn, curveFn
reload(attrFn)
reload(curveFn)

from ..library import controlShapes
reload(controlShapes)


class Control:
    def __init__(self, name, config):
        self.control_name = name
        self._control_data = {}
        self.config = config

    def build(self):
        nodes = []
        for i, each in enumerate(self.config.hierarchy):

            if each is not self.config.hierarchy[-1]:
                grp = pm.createNode('transform', n='{}_{}'.format(self.control_name, each))
                nodes.append(grp)
                self._control_data[each] = grp.name()
            else:
                if self.config.shape:
                    shape_data = controlShapes.shapes.get(self.config.shape, 'circle')[0]
                    ctrl = pm.curve(d=shape_data['degree'],
                                    p=shape_data['point'], k=shape_data['knot'],
                                    n='{}_{}'.format(self.control_name, each))
                    nodes.append(ctrl)
                    self._control_data[each] = ctrl.name()
                    self.lock_translate(ctrl, self.config.lock_translate)
                    self.lock_rotate(ctrl, self.config.lock_rotate)
                    self.lock_scale(ctrl, self.config.lock_scale)
                    self.lock_visibility(ctrl, self.config.lock_visibility)
                    curveFn.set_shape_color(ctrl.getShape().name(), self.config.color)
            if i > 0:
                pm.parent(nodes[i], nodes[i-1])

    def __getattr__(self, item):
        return self._control_data.get(item)

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

