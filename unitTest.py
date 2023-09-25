import sys
from importlib import reload
from . import project_settings
reload(project_settings)

from .modules import fk
reload(fk)

from .modules import placer
reload(placer)

from .core import build
reload(build)


def main():

    env = project_settings.PROJECT()
    env.project = 'RAIN'
    env.asset = 'Rain'

    rig = build.Build()
    rig.env = env.asset

    # #
    placer_obj = placer.Placer(name='placer', module='FK', side="M", shape='circle', asset_name='RAIN')
    rig.add_module(placer_obj)

    fk_test = fk.FK(name='Hip', module='FK', side="L", shape='square', has_chain=True)
    fk_test.attach_module = placer_obj.controls[-1]
    rig.add_module(fk_test)

    rig.build()


if __name__ == '__main__':
    main()
