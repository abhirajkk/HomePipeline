import sys
from importlib import reload
from . import project_settings
reload(project_settings)

from .modules import fk
reload(fk)


def main():

    env = project_settings.PROJECT()
    # env.create('Rain')
    # env.add_asset('Rain')
    # env.to_json()
    # env = x.from_json('RAIN')
    # print(env.get_build('Rain'))

    env.project = 'RAIN'
    env.asset = 'Rain'

    # #

    root_fk = fk.FK(name='Root', module='FK', side="M", shape='square')
    root_fk.config['build'] = env.asset
    root_fk.build()

    fk_test = fk.FK(name='Hip', module='FK', side="L", shape='square')
    fk_test.config['build'] = env.asset
    fk_test.build()


if __name__ == '__main__':
    main()