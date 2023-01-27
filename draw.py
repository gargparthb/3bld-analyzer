import pyglet
from pyglet import shapes
import sys
from cubie import make_cube

color_scheme = {
    "white": (255, 255, 255),
    "green": (0, 155, 72),
    "red": (183, 18, 52),
    "blue": (0, 70, 173),
    "orange": (255, 88, 0),
    "yellow": (255, 213, 0)
}

black = (0, 0, 0)

size = 40
border = 5


def scale(n):
    return size * n


window = pyglet.window.Window(size * 12, size * 9)
batch = pyglet.graphics.Batch()

stickers = [0 for x in range(56)]


def place_faces(cube):
    draw_face(cube, lambda c: c.y() == 1, lambda qb: (qb.x() + 4, qb.z() + 7), (0, 1, 0), 0)
    draw_face(cube, lambda c: c.y() == -1, lambda qb: (qb.x() + 4, qb.z() + 1), (0, -1, 0), 9)
    draw_face(cube, lambda c: c.x() == -1, lambda qb: (qb.z() + 1, qb.y() + 4), (-1, 0, 0), 18)
    draw_face(cube, lambda c: c.x() == 1, lambda qb: (qb.z() + 7, qb.y() + 4), (1, 0, 0), 27)
    draw_face(cube, lambda c: c.z() == 1, lambda qb: (qb.x() + 4, qb.y() + 4), (0, 0, 1), 36)
    draw_face(cube, lambda c: c.z() == -1, lambda qb: (qb.x() + 10, qb.y() + 4), (0, 0, -1), 45)


def draw_face(cube, cond, pos_func, norm, index):
    for qb in filter(cond, cube):
        draw_tile(pos_func(qb), qb.get_colors(color_scheme)[norm], index)
        index += 1


def draw_tile(pos, color, index):
    stickers[index] = shapes.BorderedRectangle(scale(pos[0]), scale(pos[1]), size, size,
                                               border=border, color=color, border_color=black, batch=batch)


@window.event
def on_draw():
    window.clear()
    batch.draw()

place_faces(eval(sys.argv[1]))

pyglet.app.run()
