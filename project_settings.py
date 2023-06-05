import maya.cmds as mc
import os
import json

PROJECT_PATH = r'D:\work\Home_project'

PROJECT_HIERARCHY = ('CHAR', 'PROP')

DEPT = ('MDL', 'RIG', 'SUR')
RIG = ('BUILD', 'DATA', 'RIG')
DATA = ('control', 'skeleton', 'mesh', 'deformer')


class PROJECT:
    def __init__(self):
        self.project = None
        self.assets = []
        self._asset = None

    def get(self, name):
        # self.project = self.create_folder(name, PROJECT_PATH)
        return self.project

    def get_asset(self, name):
        return os.path.join(self.project, self.assets[0], name)

    def get_build(self, asset):
        return os.path.join(self.get_asset(asset), 'RIG', 'BUILD')

    def create(self, name='RAIN'):
        self.project = self.create_folder(name, PROJECT_PATH)

        # assets
        for asset in PROJECT_HIERARCHY:
            self.assets.append(self.create_folder(asset, self.project))

    def add_asset(self, name='Rain', asset_type='CHAR'):

        if asset_type == 'CHAR':
            asset = self.create_folder(name, self.assets[0])
        else:
            asset = self.create_folder(name, self.assets[1])

        # mdl rig surf
        dept = []
        for stage in DEPT:
            dept.append(self.create_folder(stage, asset))
        # rig
        rig_stage = []
        for process in RIG:
            rig_stage.append(self.create_folder(process, dept[1]))

        for data in DATA:
            self.create_folder(data, rig_stage[1])

    @staticmethod
    def create_folder(name, root):
        path = os.path.join(root, name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def to_json(self):
        path = os.path.join(self.project, 'data.json')
        with open(path, 'w') as fh:
            json.dump(self.__dict__, fh, indent=4)

    @classmethod
    def from_json(cls, project_name):
        with open(os.path.join(PROJECT_PATH, project_name, 'data.json'), 'r') as fh:
            data = json.load(fh)
            cls_obj = cls()
            for key, value in data.items():
                cls_obj.__dict__[key] = value
            return cls_obj

