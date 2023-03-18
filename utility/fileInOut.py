import os
import shutil
import json


def export_as_json(name, path):
    pass


def export_as_maya_file(name, path):
    pass


def version_check(name, path):
    if os.path.exists(os.path.join(path, name)):
        # check if version folder exist or not
        if not os.path.exists(os.path.join(path, 'version')):
            os.makedirs(os.path.join(path, 'version'))
        # check if there is a version file exists or not
        if os.path.exists(os.path.join(path, 'version', name)):
            file_name = os.path.basename(os.path.join(path, 'version', name)).split('.')[0]
            version = file_name.split('_')[-1]
            if len(version) > 1:
                increment = int(version) + 1
                os.rename(
                    (os.path.join(path, 'version', name),
                     (os.path.join(path, 'version', '{}_v{}'.format(name, increment)))))
            else:
                os.rename(
                    (os.path.join(path, 'version', name), (os.path.join(path, 'version', '{}_v{}'.format(name, 1)))))
            shutil.move(os.path.join(path, name), os.path.join(path, 'version', name))
