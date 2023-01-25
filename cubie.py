import numpy as np

class Cubie:
    def __init__(self, current_position, solved_position, normals):
        self.current_position = current_position
        self.solved_position = solved_position
        self.normals = normals

    def __str__(self):
        return f"Cubie from {self.solved_position} at {self.current_position} with normals: {self.normals}"

def make_cube():
    cube = []
    default_normals = [np.array([0, 1, 0]), np.array([0, 0, 1])]
    for x in range(-1, 2, 1):
        for y in range(-1, 2, 1):
            for z in range(-1, 2, 1):
                pos = np.array([x, y, z])
                cube.append(Cubie(pos, pos, default_normals))
    return cube
