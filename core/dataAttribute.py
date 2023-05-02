from ..core import coreMeta
from importlib import reload
reload(coreMeta)


class DataClass:
    def __init__(self, **kwargs):
        self.name = 'fk'
        self.component = None
        self.module = None
        self.side = 'M'
        self.color = 17
        self.hierarchy = ['zero', 'offset', 'ctrl']
        self.lock_visibility = True
        self.lock_translate = True
        self.lock_rotate = False
        self.lock_scale = True
        self.module_hierarchy = ['inputs', 'outputs', 'controls', 'deform']
        self.nodes = {}
        self.guide = None
        self.bind = {}
        self.inputs = {}
        self.outputs = {}
        self.controls = {}

        for key, value in kwargs.items():
            if key in self.__dict__:
                self.__dict__[key] = value



'''
class DataClass(metaclass=coreMeta.Meta):
    def __init__(self, *args, **kwargs):

        self.name = kwargs.get('name', 'fk')
        self.component = kwargs.get('component', None)
        self.module = kwargs.get('module', None)
        self.side = kwargs.get('side', 'M')
        self.color = kwargs.get('color', 17)
        self.hierarchy = kwargs.get('hierarchy', ['zero', 'offset', 'ctrl'])
        self.lock_visibility = kwargs.get('lock_visibility', True)
        self.lock_translate = kwargs.get('lock_translate', True)
        self.lock_rotate = kwargs.get('lock_rotate', False)
        self.lock_scale = kwargs.get('lock_rotate', True)
        self.module_hierarchy = kwargs.get('hierarchy', ['inputs', 'outputs', 'controls', 'deform'])
        self.nodes = kwargs.get('nodes', {})
        self.guide = kwargs.get('guide', None)
        self.bind = kwargs.get('bind', {})
        self.inputs = kwargs.get('inputs', {})
        self.outputs = kwargs.get('outputs', {})
        self.controls = kwargs.get('controls', {})
'''