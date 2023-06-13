from maya import cmds
from maya.api import OpenMaya
import pymel.core as pm


def parent_constraint(source, target):
    source_matrix = pm.xform(source, q=1, m=1, ws=1)
    target_matrix = pm.xform(target, q=1, m=1, ws=1)

    offset_matrix = OpenMaya.MMatrix(source_matrix) * OpenMaya.MMatrix(target_matrix).inverse()

    mult_matrix = pm.createNode('multMatrix', n='{}_{}'.format(target, 'PM'))
    mult_matrix.matrixIn[0].set(offset_matrix)

    pm.connectAttr('{}.worldMatrix[0]'.format(source), mult_matrix.matrixIn[1])

    pm.connectAttr(mult_matrix.matrixSum, '{}.offsetParentMatrix'.format(target))


parent_constraint('pSphere1', 'pSphere2')