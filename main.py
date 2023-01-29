import move as m
from cubie import make_cube
from draw import draw_cube

cube = make_cube()
scramble = "B2"
m.apply_scramble(cube, scramble)
for q in cube:
    print(q)
draw_cube(cube)