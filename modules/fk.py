from ..core import control

import pymel.core as pm
from importlib import reload
reload(control)

from.. modules import chain
reload(chain)

from.. core import dagNode
reload(dagNode)


class FK(dagNode.DagNode):
    def __init__(self, name):
        self.module_name = name
        super(FK, self).__init__('{}_{}'.format(self.module_name, 'fk'))

    def build_fk(self):
        joints = chain.Chain.get_chain_from_scene(self.module_name)
        if joints:
            self.build_module()
            zero_nodes = []
            ctrl_nodes = []
            for joint in joints:
                self.control_name = joint.replace('_JNT', '_fk')
                self.build_dag()
                pm.parent(self.zero, self.controls)
                pm.matchTransform(self.zero, joint)
                zero_nodes.append(self.zero)
                ctrl_nodes.append(self.ctrl)
                self.lock_translate(self.ctrl, True)

            # set hierarchy
            for i in range(1, len(zero_nodes)):
                pm.parent(zero_nodes[i], ctrl_nodes[i-1])
        else:
            pm.warning('Cant find joint chain!!')

    def build_chain(self):
        pass
