from scipy.spatial.transform import Rotation
import cubie
import utils

class Move:
    def __init__(self, selector, axis, angle):
        self.selector = selector
        self.rotation = Rotation.from_euler(axis, angle, degrees=True)

    def apply(self, cube):
        for qb in filter(self.selector, cube):
            qb.apply_rotation(self.rotation)


