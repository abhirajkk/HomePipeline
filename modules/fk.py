from ..core import control
from ..core import module
import pymel.core as pm
from importlib import reload
reload(control)
reload(module)
from.. modules import chain
reload(chain)


class FK(module.Base):
    def __init__(self, name):
        self.module_name = name
        super(FK, self).__init__('{}_{}'.format(self.module_name, 'fk'))
        self._fk_data = {}

    def build_fk(self):
        self.build()

        for joint in chain.Chain.get_chain_from_scene(self.module_name):
            ctrl = control.Control(joint.replace('_JNT', '_fk'))
            ctrl.build()
            pm.parent(ctrl.zero, self.controls)
            self._fk_data[joint.name()] = ctrl
        # items = self._fk_data.keys()
        # for i in range(1, len(items)):
        #     pm.parent(items.index(i))
