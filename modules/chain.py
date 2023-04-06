from importlib import reload
from .. utility import fileInOut
reload(fileInOut)
from .. static import directories
reload(directories)
import pymel.core as pm


class Chain:
    def __init__(self):
        pass

    @classmethod
    def export_chain(cls, name):
        fileInOut.export_as_maya_file(name, directories.CHAIN)

    @classmethod
    def import_chain(cls, name):
        fileInOut.import_maya_file(name, directories.CHAIN)

    @classmethod
    def get_chain_from_scene(cls, name):
        chain = pm.ls('{}_*_JNT'.format(name), type='joint')
        if chain:
            return chain
        else:
            return None
