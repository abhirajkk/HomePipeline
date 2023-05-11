import pymel.core as pm


class Base:
    def __init__(self, name):
        self.top_node = '{}_{}'.format(name, 'local')
        self.name = name
        self.module_nodes = ['inputs', 'outputs', 'controls', 'deform']
        self.module_data = {}

    def build_module(self):
        pm.createNode('transform', n=self.top_node)
        for each in self.module_nodes:
            node = pm.createNode('transform', n='{}_{}'.format(self.name, each), p=self.top_node)
            self.module_data[each] = node.name()

    def __getattr__(self, item):
        return self.module_data.get(item)

