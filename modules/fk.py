from ..core import control

import pymel.core as pm
import maya.cmds as mc
from importlib import reload
reload(control)

from.. modules import chain
reload(chain)

from ..core import dataAttribute
reload(dataAttribute)

from ..core import module
reload(module)

from ..functions import attrFn
reload(attrFn)


class FK(dataAttribute.DataClass):
    def __init__(self, **kwargs):
        super(FK, self).__init__(**kwargs)
        self.module_obj = module.Base(f'{self.side}_{self.name}{self.module}')

    def build_fk(self):
        self.guide = chain.Chain.get_chain_from_scene('{}_{}'.format(self.side, self.name))
        if self.guide:
            self.module_obj.build_module()
            zero_nodes = []
            ctrl_nodes = []
            for joint in self.guide:
                control_name = joint.replace('_JNT', '_fk')
                ctrl_obj = control.Control(control_name)
                ctrl_obj.build()
                self.controls[control_name] = ctrl_obj
                pm.matchTransform(ctrl_obj['zero'], joint)
                zero_nodes.append(ctrl_obj['zero'])
                ctrl_nodes.append(ctrl_obj['ctrl'])

                if self.lock_translate:
                    attrFn.AttrFn.lock_translate(ctrl_obj['ctrl'], True)

            # set hierarchy
            for i in range(1, len(zero_nodes)):
                pm.parent(zero_nodes[i], ctrl_nodes[i-1])
            mc.parent(zero_nodes[0], self.module_obj.controls)

        else:
            pm.warning('Cant find joint chain!!', '{}_{}'.format(self.side, self.name))

    def build_chain(self):
        pass
