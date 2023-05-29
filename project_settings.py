import maya.cmds as mc
import os
import json
PROJECT_PATH = r'D:\work\Home_project'
PROJECT_HIERARCHY = {
                     'assets': ['CHAR', 'PROP'],
                     'dept': ['MDL', 'RIG', 'SUR'],
                     'build': ['build'],
                     'data': ['control', 'skeleton', 'mesh', 'deformer']
                     }


class PROJECT:
    def __init__(self):
        self.project = None
        self.assets = []
        self.dept = []
        self.data = None
        self.rig_data = []
        self.build_data = None

    def get_project(self):
        return self.project

    def get_char(self):
        return self.assets[0]

    def get_prop(self):
        return self.assets[1]

    def get_build(self):
        return self.build_data

    def get_data(self):
        return self.data

    def get_control(self):
        return self.rig_data[0]

    def get_skeleton(self):
        return self.rig_data[1]

    def get_mesh(self):
        return self.rig_data[2]

    def get_deformer(self):
        return self.rig_data[-1]

    def add_project(self, name='RAIN'):
        self.project = self.create_folder(name, PROJECT_PATH)

        # assets
        for asset in PROJECT_HIERARCHY['assets']:
            self.assets.append(self.create_folder(asset, self.project))

    def add_asset(self, name='Rain', asset_type='CHAR'):

        if asset_type == 'CHAR':
            asset = self.create_folder(name, self.assets[0])
        else:
            asset = self.create_folder(name, self.assets[1])

        for stage in PROJECT_HIERARCHY['dept']:
            self.dept.append(self.create_folder(stage, asset))

        for data in PROJECT_HIERARCHY['data']:
            self.data = self.create_folder('DATA', self.dept[1])
            self.rig_data.append(self.create_folder(data, self.data))

        # for bld in PROJECT_HIERARCHY['build']:
        self.build_data = self.create_folder('BUILD', self.dept[1])

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

