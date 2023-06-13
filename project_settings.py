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
        self._project = None
        self.rig_type = []
        self._asset = None

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, asset_name):
        asset_path = os.path.join(self.rig_type[0], asset_name, 'RIG', 'BUILD')
        if os.path.exists(asset_path):
            self._asset = asset_path
        else:
            self.add_asset(asset_name)

    @property
    def project(self):
        return self._project

    @project.setter
    def project(self, project_name):
        inst = self.from_json(project_name)
        if inst:
            self._project = inst._project
            self.rig_type = inst.rig_type
        else:
            self.create(project_name)

    def get_asset(self, name):
        return os.path.join(self._project, self.rig_type[0], name)

    def get_build(self, asset):
        return os.path.join(self.get_asset(asset), 'RIG', 'BUILD')

    def create(self, name='RAIN'):
        self._project = self.create_folder(name, PROJECT_PATH)

        # rig_type
        for asset in PROJECT_HIERARCHY:
            self.rig_type.append(self.create_folder(asset, self._project))
        self.to_json()

    def add_asset(self, name='Rain', asset_type='CHAR'):
        if asset_type == 'CHAR':
            asset = self.create_folder(name, self.rig_type[0])
        else:
            asset = self.create_folder(name, self.rig_type[1])

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
        self.to_json()

    @staticmethod
    def create_folder(name, root):
        path = os.path.join(root, name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def to_json(self):
        path = os.path.join(self._project, 'data.json')
        with open(path, 'w') as fh:
            json.dump(self.__dict__, fh, indent=4)

    @classmethod
    def from_json(cls, project_name):
        path = os.path.join(PROJECT_PATH, project_name, 'data.json')
        if os.path.exists(path):
            with open(path, 'r') as fh:
                data = json.load(fh)
                cls_obj = cls()
                for key, value in data.items():
                    cls_obj.__dict__[key] = value
                return cls_obj
        else:
            return None
