import pyglet
from rigidbody import Circle
from consts import GRAVITY, RIGHTWARD_WIND

win = pyglet.window.Window(1024, 512)

circle = Circle(200, 300)
circle.border_collision = True
circle.coefficient_of_restitution = 0.9

def update(dt):
    # Forces
    circle.apply_forces(GRAVITY, RIGHTWARD_WIND)

    # Update
    circle.update(dt)

    # Collision
    circle.collide()

@win.event
def on_draw():
    win.clear()

    circle.draw()

pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
