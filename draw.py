import pyglet
from pyglet import shapes

color_scheme = {
    "white": (255, 255, 255),
    "green": (0, 155, 72),
    "red": (183, 18, 52),
    "blue": (0, 70, 173),
    "orange": (255, 88, 0),
    "yellow": (255, 213, 0)
}

black = (0, 0, 0)

size = 50
border = 1


def scale(n):
    return size * n


def draw_cube(cube):
    window = pyglet.window.Window(size * 12, size * 9)
    batch = pyglet.graphics.Batch()

    stickers = [0 for _ in range(56)]

    def draw_face(cond, pos_func, norm, index):
        for qb in filter(cond, cube):
            draw_tile(pos_func(qb), qb.get_colors(color_scheme)[norm], index)
            index += 1

    def draw_tile(pos, color, index):
        stickers[index] = shapes.BorderedRectangle(scale(pos[0]), scale(pos[1]), size, size,
                                                   border=border, color=color, border_color=black, batch=batch)
    # U, D, L, R, F, B
    draw_face(lambda c: c.y() == 1, lambda qb: (qb.x() + 4, -qb.z() + 7), (0, 1, 0), 0)
    draw_face(lambda c: c.y() == -1, lambda qb: (qb.x() + 4, qb.z() + 1), (0, -1, 0), 9)
    draw_face(lambda c: c.x() == -1, lambda qb: (qb.z() + 1, qb.y() + 4), (-1, 0, 0), 18)
    draw_face(lambda c: c.x() == 1, lambda qb: (-qb.z() + 7, qb.y() + 4), (1, 0, 0), 27)
    draw_face(lambda c: c.z() == 1, lambda qb: (qb.x() + 4, qb.y() + 4), (0, 0, 1), 36)
    draw_face(lambda c: c.z() == -1, lambda qb: (-qb.x() + 10, qb.y() + 4), (0, 0, -1), 45)

    @window.event
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.app.run()
