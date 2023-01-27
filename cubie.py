import numpy as np


class Cubie:
    def __init__(self, current_position, solved_position, normals):
        self.current_position = current_position
        self.solved_position = solved_position
        # array of white and green normals
        self.normals = normals

    def __str__(self):
        return f"Cubie from {self.solved_position} at {self.current_position} with normals: {self.normals}"

    def get_colors(self, shades):
        colors = {
                  tuple(self.normals[0]): shades["white"],
                  tuple(self.normals[0].__mul__(-1)): shades["yellow"],
                  tuple(self.normals[1]): shades["green"],
                  tuple(self.normals[1].__mul__(-1)): shades["blue"]}
        normals_cross = np.cross(self.normals[0],
                                 self.normals[1])
        colors[tuple(normals_cross)] = shades["red"]
        colors[tuple(normals_cross.__mul__(-1))] = shades["orange"]
        return colors

    def x(self):
        return self.current_position[0]

    def y(self):
        return self.current_position[1]

    def z(self):
        return self.current_position[2]


def make_cube():
    cube = []
    default_normals = [np.array([0, 1, 0]), np.array([0, 0, 1])]
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            for z in range(-1, 2, 1):
                pos = np.array([x, y, z])
                cube.append(Cubie(pos, pos, default_normals))
    return cube
