import pyglet
from rigidbody import Circle
from consts import GRAVITY, LEFTWARD_WIND

win = pyglet.window.Window(1024, 512, "Physics")

batch = pyglet.graphics.Batch()

bodies = [Circle(315, 150, 1.75, color=(128, 201, 234), batch=batch),
    Circle(300, 300, 1, color=(73, 234, 124), batch=batch),
    Circle(300, 400, 0.75, color=(234, 123, 123), batch=batch)]

for body in bodies:
    body.coefficient_of_restitution = 0.99

def update(dt):
    # Forces
    for body in bodies:
        body.apply_forces(GRAVITY, LEFTWARD_WIND)

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
