import pymel.core as pm
import maya.cmds as mc
from importlib import reload

from ..core import control, module, component
reload(control)
reload(module)
reload(component)

from.. modules import chain
reload(chain)


class FK(component.Component):
    def __init__(self, **kwargs):
        super(FK, self).__init__()
        self.config.__init__(**kwargs)
        self.module_obj = module.Base(f'{self.config.side}_{self.config.name}{self.config.module}')

    def main(self):
        self.guide = chain.Chain.get_chain_from_scene('{}_{}'.format(self.config.side, self.config.name))
        if self.guide:
            self.module_obj.build_module()
            zero_nodes = []
            ctrl_nodes = []
            for joint in self.guide:
                control_name = joint.replace('_JNT', '_fk')
                ctrl_obj = control.Control(control_name, self.config)
                ctrl_obj.build()

                # post
                self.data[control_name] = ctrl_obj
                pm.matchTransform(ctrl_obj.zero, joint)
                zero_nodes.append(ctrl_obj.zero)
                ctrl_nodes.append(ctrl_obj.ctrl)
            # set hierarchy
            for i in range(1, len(zero_nodes)):
                pm.parent(zero_nodes[i], ctrl_nodes[i-1])
            mc.parent(zero_nodes[0], self.module_obj.controls)

        else:
            pm.warning('Cant find joint chain!!', '{}_{}'.format(self.config.side, self.config.name))
        print(self.data.__dict__)
        print(self.config.__dict__)

    def post_build(self):
        pm.select(clear=True)

    def pre_build(self):
        pass

    def build_chain(self):
        pass
