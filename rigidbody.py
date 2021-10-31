from functools import reduce
from vector import vector
import pyglet

class Rigidbody:
    def __init__(self, x, y, mass=1, color=(255, 255, 255), batch=None):
        self.pos = vector(x, y)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)

        self.mass = mass
        if self.mass == 0:
            self.inv_mass = 0
        else:
            self.inv_mass = 1 / mass

        self.color = color

        self.coefficient_of_restitution = 1

    def apply_forces(self, *forces):
        if not forces:
            return
        self.acc += reduce(lambda x, y: x + y, forces) * self.inv_mass

    def border_collide(self):
        raise NotImplemented

    def collide(self, other):
        raise NotImplemented

    def update(self, dt):
        self.pos += self.vel * dt
        self.vel += self.acc * dt
        self.acc *= 0 # Reset

    def draw(self):
        raise NotImplemented

class Circle(Rigidbody):
    def __init__(self, x, y, mass=1, color=(255, 255, 255), batch=None):
        super().__init__(x, y, mass, color)

        self.radius = mass * 10
        self.shape = pyglet.shapes.Circle(self.pos.x, self.pos.y, self.radius, batch=batch)

    def border_collide(self):
        if self.pos.x <= self.radius:
            self.vel.x *= -1 * self.coefficient_of_restitution
        elif self.pos.x >= (1024 - self.radius):
            self.vel.x *= -1 * self.coefficient_of_restitution

        if self.pos.y <= self.radius:
            self.vel.y *= -1 * self.coefficient_of_restitution
        elif self.pos.y >= (512 - self.radius):
            self.vel.y *= -1 * self.coefficient_of_restitution

    def collide(self, other):
        if type(other) == Circle:
            if abs(self.pos - other.pos) <= self.radius + other.radius:
                penetration_depth = other.pos - self.pos
                collision_normal = penetration_depth.normal()

                self.vel += collision_normal * self.inv_mass * other.coefficient_of_restitution * -1

                self.pos += penetration_depth * self.inv_mass * -0.01

    def update(self, dt):
        super().update(dt)

        # Update shape
        self.shape.x = self.pos.x
        self.shape.y = self.pos.y
        self.shape.color = self.color

    def draw(self):
        self.shape.draw()

class Polygon(Rigidbody):
    ...
