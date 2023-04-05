import pymel.core as pm


class Control:
    def __init__(self, name):
        self.hierarchy = ['zero', 'offset', 'ctrl']
        self.control_name = name
        self._control_data = {}

    def build(self):
        nodes = []
        for i, each in enumerate(self.hierarchy):
            grp = pm.createNode('transform', n='{}_{}'.format(self.control_name, each))
            nodes.append(grp)
            self._control_data[each] = grp.name()
            if i > 0:
                pm.parent(nodes[i], nodes[i-1])

    @property
    def zero(self):
        return self._control_data['zero']

    @property
    def offset(self):
        return self._control_data['offset']

    @property
    def ctrl(self):
        return self._control_data['ctrl']