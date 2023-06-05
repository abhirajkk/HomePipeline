import sys
from importlib import reload
from . import project_settings
reload(project_settings)

from .modules import fk
reload(fk)


def main():

    x = project_settings.PROJECT()
    # x.create('Rain')
    # x.add_asset('Rain')
    # x.to_json()
    env = x.from_json('RAIN')
    print(env.get_build('Rain'))
    #
    fk_test = fk.FK(name='Hip', component='arm', module='FK', side="L", shape='square')
    fk_test.config['build'] = env.get_build('Rain')
    fk_test.build()


if __name__ == '__main__':
    main()