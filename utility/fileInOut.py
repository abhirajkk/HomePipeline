import os
import shutil
import json
import pymel.core as pm


def export_as_json(name, path):
    pass


def export_as_maya_file(name, path):
    version_check(name+'.mb', path)
    # file -force -options "v=0;" -typ "mayaBinary" -pr -es "D:/work/Home_project/DATA/skeleton/chain.mb";
    file_name = os.path.join(path, name+'.mb')
    pm.exportSelected(file_name)


def import_maya_file(name, path):
    file_name = os.path.join(path, name + '.mb')
    pm.importFile(file_name)


def version_check(name, path):
    if os.path.exists(os.path.join(path, name)):
        # check if version folder exist or not
        if not os.path.exists(os.path.join(path, 'version')):
            os.makedirs(os.path.join(path, 'version'))
        # check if there is a version file exists or not
        if os.path.exists(os.path.join(path, 'version', name)):
            file_name = os.path.basename(os.path.join(path, 'version', name)).split('.')[0]
            version = file_name.split('_')[-1]
            if not isinstance(version, str):
                # if len(version) > 1:
                increment = int(version) + 1
                os.rename(
                    (os.path.join(path, 'version', name),
                     (os.path.join(path, 'version', '{}_v{}'.format(name, increment)))))
            else:
                tmp = name.split('.')[0]
                version_name = '{}_{}.mb'.format(tmp, 1)
                current_name = os.path.join(path, 'version', name)
                new_name = (os.path.join(path, 'version', version_name))
                os.rename(current_name, new_name)
            shutil.move(os.path.join(path, name), os.path.join(path, 'version', name))
        else:
            shutil.move(os.path.join(path, name), os.path.join(path, 'version', name))

