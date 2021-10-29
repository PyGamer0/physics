import pyglet
from rigidbody import Circle
from consts import GRAVITY, LEFTWARD_WIND, RIGHTWARD_WIND
from vector import vector
from random import random

win = pyglet.window.Window(1024, 512, "Physics")

batch = pyglet.graphics.Batch()

bodies = [Circle(315, 150, 1.25, color=(128, 201, 234), batch=batch),
    Circle(300, 300, color=(73, 234, 124), batch=batch),
    Circle(300, 400, 2, color=(234, 123, 123), batch=batch)]

def update(dt):
    # Forces
    for body in bodies:
        body.apply_forces(GRAVITY)

        # Update
        body.update(dt)

        # Collision
        body.border_collide()
        
        for body2 in bodies:
            if not body is body2:
                body.collide(body2)

@win.event
def on_draw():
    win.clear()
    batch.draw()

pyglet.clock.schedule_interval(update, 1 / 60)
pyglet.app.run()
