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

    def build_fk(self):
        joints = chain.Chain.get_chain_from_scene(self.module_name)
        if joints:
            self.build()
            zero_nodes = []
            ctrl_nodes = []
            for joint in joints:
                fk_ctrl = control.Control(joint.replace('_JNT', '_fk'))
                fk_ctrl.build()
                pm.parent(fk_ctrl.zero, self.controls)
                pm.matchTransform(fk_ctrl.zero, joint)
                zero_nodes.append(fk_ctrl.zero)
                ctrl_nodes.append(fk_ctrl.ctrl)

            # set hierarchy
            for i in range(1, len(zero_nodes)):
                pm.parent(zero_nodes[i], ctrl_nodes[i-1])
        else:
            pm.warning('Cant find joint chain!!')

    def build_chain(self):
        pass
