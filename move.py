from scipy.spatial.transform import Rotation


class Move:
    def __init__(self, selector, axis=None, angle=None, rotation=None):
        self.selector = selector
        if rotation is None:
            self.rotation = Rotation.from_euler(axis, angle, degrees=True)
        else:
            self.rotation = rotation

    def apply(self, cube):
        for qb in filter(self.selector, cube):
            qb.apply_rotation(self.rotation)

    def inverse(self):
        return Move(selector=self.selector, rotation=self.rotation.inv())

    def double(self):
        return Move(selector=self.selector, rotation=self.rotation.concatenate([self.rotation]))


moves = {
    "R": Move(lambda q: q.x() == 1, 'x', -90),
    "Rw": Move(lambda q: q.x() == 1 or q.x() == 0, 'x', -90),
    "L": Move(lambda q: q.x() == -1, 'x', 90),
    "D": Move(lambda q: q.y() == -1, 'y', 90),
    "U": Move(lambda q: q.y() == 1, 'y', -90),
    "Uw": Move(lambda q: q.y() == 1 or q.y() == 0, 'y', -90),
    "F": Move(lambda q: q.z() == 1, 'z', -90),
    "Fw": Move(lambda q: q.z() == 1 or q.z() == 0, 'z', -90),
    "B": Move(lambda q: q.z() == -1, 'z', 90),
}

inverse_moves = {}
double_moves = {}

for key in moves:
    inverse_moves[key + "'"] = moves[key].inverse()
    double_moves[key + '2'] = moves[key].double()

moves.update(inverse_moves)
moves.update(double_moves)

print(moves['B2'])


def apply_scramble(cube, scramble):
    sequence = [moves[x] for x in scramble.split()]
    for move in sequence:
        moves['B2'].apply(cube)