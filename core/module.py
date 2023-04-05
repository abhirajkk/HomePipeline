import pymel.core as pm


class Base:
    def __init__(self, name):
        self.top_node = '{}_{}'.format(name, 'local')
        self.name = name
        self.module_nodes = ['inputs', 'outputs', 'controls', 'deform']
        self._module_data = {}

    def build(self):
        pm.createNode('transform', n=self.top_node)
        for each in self.module_nodes:
            node = pm.createNode('transform', n='{}_{}'.format(self.name, each), p=self.top_node)
            self._module_data[each] = node.name()

    @property
    def inputs(self):
        return self._module_data['inputs']

    @property
    def outputs(self):
        return self._module_data['outputs']

    @property
    def controls(self):
        return self._module_data['controls']

    @property
    def deform(self):
        return self._module_data['deform']