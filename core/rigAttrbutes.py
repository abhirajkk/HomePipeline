from ..core import dataAttribute

'''
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

data = {'name': 'FK',
        'component': None,
        'module': None,
        'color': 17,
        'side': 'M',
        'hierarchy': ['zero', 'offset', 'ctrl'],
        'lock_visibility': True,
        'lock_translate': True,
        'lock_rotate': True,
        'lock_scale': True,
        'module_hierarchy': ['inputs', 'outputs', 'controls', 'deform'],
        'guide': None,
        'bind': None,
        'inputs': None,
        'outputs': None,
        'controls': []
        }
