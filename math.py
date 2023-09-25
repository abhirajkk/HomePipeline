
import numpy as np
import pymel.core as pm


def create_circle(radius=5, center=(0, 0)):
    theta = np.linspace(0, 2 * np.pi, 10)
    for each in theta.tolist():
        x = center[0] + radius * np.cos(each)
        y = center[1] + radius * np.sin(each)

        pm.spaceLocator(p=(x, 0, y))


import maya.cmds as cmds
import math


def is_point_inside_capsule(point, capsule_start, capsule_end, radius):
    # Calculate the vector from the capsule start to the point
    vector_start_to_point = [point[0] - capsule_start[0], point[1] - capsule_start[1], point[2] - capsule_start[2]]

    # Calculate the vector along the capsule axis
    vector_capsule_axis = [capsule_end[0] - capsule_start[0], capsule_end[1] - capsule_start[1],
                           capsule_end[2] - capsule_start[2]]

    # Calculate the dot product of the two vectors
    dot_product = (vector_start_to_point[0] * vector_capsule_axis[0] +
                   vector_start_to_point[1] * vector_capsule_axis[1] +
                   vector_start_to_point[2] * vector_capsule_axis[2])

    # Calculate the length squared of the capsule axis
    axis_length_squared = (vector_capsule_axis[0] ** 2 +
                           vector_capsule_axis[1] ** 2 +
                           vector_capsule_axis[2] ** 2)

    # Calculate the parameter value along the capsule axis
    t = dot_product / axis_length_squared

    # Clamp the parameter value between 0 and 1
    t = max(0.0, min(1.0, t))

    # Calculate the closest point on the capsule axis to the input point
    closest_point_on_capsule = [capsule_start[0] + t * vector_capsule_axis[0],
                                capsule_start[1] + t * vector_capsule_axis[1],
                                capsule_start[2] + t * vector_capsule_axis[2]]

    # Calculate the distance between the input point and the closest point on the capsule axis
    distance_squared = (point[0] - closest_point_on_capsule[0]) ** 2 + \
                       (point[1] - closest_point_on_capsule[1]) ** 2 + \
                       (point[2] - closest_point_on_capsule[2]) ** 2

    return distance_squared <= radius ** 2


def points_inside_capsule(capsule_start, capsule_end, radius, resolution=0.1):
    # Calculate the bounding box of the capsule
    min_x = min(capsule_start[0], capsule_end[0]) - radius
    max_x = max(capsule_start[0], capsule_end[0]) + radius
    min_y = min(capsule_start[1], capsule_end[1]) - radius
    max_y = max(capsule_start[1], capsule_end[1]) + radius
    min_z = min(capsule_start[2], capsule_end[2]) - radius
    max_z = max(capsule_start[2], capsule_end[2]) + radius

    # Iterate through the points inside the bounding box and check if they are inside the capsule
    points_inside = []
    for x in cmds.floatRange(min_x, max_x, resolution):
        for y in cmds.floatRange(min_y, max_y, resolution):
            for z in cmds.floatRange(min_z, max_z, resolution):
                point = [x, y, z]
                if is_point_inside_capsule(point, capsule_start, capsule_end, radius):
                    points_inside.append(point)

    return points_inside


# Example usage:
capsule_start = [0, 0, 0]
capsule_end = [0, 3, 0]
radius = 1.0
points_inside = points_inside_capsule(capsule_start, capsule_end, radius)

print("Points inside the capsule:")
for point in points_inside:
    print(point)
