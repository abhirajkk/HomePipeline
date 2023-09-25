import numpy
from scipy.spatial import KDTree
import pymel.core as pm


def get_left_vertices(mesh, tolerance=0.001, as_numpy=False):
    mesh_shape = pm.PyNode(mesh)
    points = numpy.array(mesh_shape.getPoints())
    ids = numpy.argwhere(points[:, 0] < tolerance)
    if as_numpy:
        return ids
    else:
        return ids.flatten().tolist()


def get_right_vertices(mesh, tolerance=0.001, as_numpy=False):
    mesh_shape = pm.PyNode(mesh)
    points = numpy.array(mesh_shape.getPoints())
    ids = numpy.argwhere(points[:, 0] < (tolerance*-1))
    if as_numpy:
        return ids
    else:
        return ids.flatten().tolist()


def get_mid_vertices(mesh, tolerance=0.001, as_numpy=False):
    pass


def get_closest_vertices(mesh, positions, tolerance=1.0):
    mesh_shape = pm.PyNode(mesh)
    mesh_pnts = numpy.array(mesh_shape.getPoints())

    all_positions = []
    for each in positions:
        all_positions.append(pm.xform(each, q=1, t=1, ws=1))

    np_transform = numpy.array(all_positions)

    mesh_tree = KDTree(mesh_pnts)

    dist, ids = mesh_tree.query(np_transform)

    vert_ids = ids.flatten()

    return vert_ids
