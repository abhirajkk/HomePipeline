import maya.cmds as mc


def set_shape_color(shape, index):
    mc.setAttr(f'{shape}.overrideEnabled', True)
    mc.setAttr(f'{shape}.overrideColor', index)
