import pyglet
from pyglet import shapes

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()

rectangle = shapes.Rectangle(250, 300, 50, 50, color=(255, 255, 255), batch=batch)


label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    window.clear()
    label.draw()
    batch.draw()


pyglet.app.run()
