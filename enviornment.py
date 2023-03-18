import os

PROJECT_RIG_PATH = r'D:\work\Home_project'


class ENV:
    def __init__(self):
        self.data_path = None
        self.control_path = None
        self.deformer_path = None
        self.mesh_path = None
        self.skeleton_path = None

        self.create_data_folder()
        self.create_sub_folders()

    @property
    def data(self):
        return self.data_path

    @property
    def control(self):
        return self.control_path

    @property
    def deformer(self):
        return self.deformer_path

    @property
    def mesh(self):
        return self.mesh_path

    @property
    def skeleton(self):
        return self.skeleton_path

    def create_data_folder(self):
        if os.path.exists(PROJECT_RIG_PATH):
            self.data_path = self.create_folder('DATA', PROJECT_RIG_PATH)

    def create_sub_folders(self):
        self.control_path = self.create_folder('control', self.data_path)
        self.deformer_path = self.create_folder('deformer', self.data_path)
        self.mesh_path = self.create_folder('mesh', self.data_path)
        self.skeleton_path = self.create_folder('skeleton', self.data_path)

    @staticmethod
    def create_folder(name, root):
        path = os.path.join(root, name)
        if not os.path.exists(path):
            os.makedirs(path)
        return path
