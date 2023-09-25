import pymel.core as pm
import maya.cmds as mc
from importlib import reload

from ..core import control, module, component
reload(control)
reload(module)
reload(component)

from.. modules import chain
reload(chain)


class Placer(component.Component):
    def __init__(self, **kwargs):
        super(Placer, self).__init__()
        self.config.__init__(**kwargs)
        self.module_obj = module.Base(f'{self.config.side}_{self.config.name}_{self.config.module}')

    def main(self):

        all_ctrl_obj = control.Control('All', self.config)
        all_ctrl_obj.build()

        placer_ctrl_obj = control.Control('Placer', self.config)
        placer_ctrl_obj.build()

        mc.parent(placer_ctrl_obj.zero, all_ctrl_obj.ctrl)

        mc.parent(all_ctrl_obj.zero, self.data[1])
        self.data.append(all_ctrl_obj)
        self.controls.append(all_ctrl_obj.ctrl)
        self.data.append(placer_ctrl_obj)
        self.controls.append(placer_ctrl_obj.ctrl)

    def post_build(self):
        pm.select(clear=True)

    def pre_build(self):
        for i, each in enumerate([self.config.asset_name, 'RIG', 'MDL']):
            if i > 0:
                grp = mc.createNode('transform', n=each, p=self.config.asset_name)
            else:
                grp = mc.createNode('transform', n=each)
            self.data.append(grp)
        # self.data['top_grp'] = mc.createNode('transform', n=self.config.asset_name)
        # self.data['rig_grp'] = mc.createNode('transform', n='RIG', p=self.data.top_grp)
        # self.data['mdl_grp'] = mc.createNode('transform', n='MDL', p=self.data.top_grp)

    def build_chain(self):
        pass