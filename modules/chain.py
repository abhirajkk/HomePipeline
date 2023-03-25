from importlib import reload
from .. utility import fileInOut
reload(fileInOut)
from .. static import directories
reload(directories)


class Chain:
    def __init__(self):
        pass

    @classmethod
    def export_chain(cls, name):
        fileInOut.export_as_maya_file(name, directories.CHAIN)

    @classmethod
    def import_chain(cls):
        pass
