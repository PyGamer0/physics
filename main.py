import pyglet
from rigidbody import Circle
from consts import GRAVITY, LEFTWARD_WIND, RIGHTWARD_WIND

win = pyglet.window.Window(1024, 512)

cir1 = Circle(200, 300)
cir1.border_collision = True
cir1.color = (124, 56, 234)

cir2 = Circle(250, 300)
cir2.border_collision = True
cir1.color = (56, 234, 124)


def update(dt):
    # Forces
    cir1.apply_forces(GRAVITY, RIGHTWARD_WIND)
    cir2.apply_forces(GRAVITY, LEFTWARD_WIND)

    # Update
    cir1.update(dt)
    cir2.update(dt)

    # Collision
    cir1.collide(cir2)
    cir2.collide(cir1)

@win.event
def on_draw():
    win.clear()

    cir1.draw()
    cir2.draw()

pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
