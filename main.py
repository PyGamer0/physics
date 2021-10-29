import pyglet
from rigidbody import Circle
from consts import GRAVITY, LEFTWARD_WIND, RIGHTWARD_WIND
from vector import vector

win = pyglet.window.Window(1024, 512)

cir1 = Circle(315, 150, 1.25)
cir1.color = (128, 201, 234)

cir2 = Circle(300, 300)
cir2.color = (73, 234, 124)

def update(dt):
    # Forces
    cir1.apply_forces(GRAVITY)
    cir2.apply_forces(GRAVITY)

    # Update
    cir1.update(dt)
    cir2.update(dt)

    # Collision
    cir1.border_collide()
    cir1.collide(cir2)

    cir2.border_collide()
    cir2.collide(cir1)

@win.event
def on_draw():
    win.clear()

    cir1.draw()
    cir2.draw()

pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
