from vector import vector
import pyglet

class Circle:
    def __init__(self, x, y, mass=1):
        self.pos = vector(x, y)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)

        self.mass = mass
        self.radius = mass * 10

        self.color = (255, 255, 255)
        self.shape = pyglet.shapes.Circle(self.pos.real, self.pos.imag, self.radius)

        self.border_collision = False
        self.coefficient_of_restitution = 1

    def apply_forces(self, *forces):
        if not forces:
            return

        self.acc += sum(forces) * self.mass # Net force times mass

    def collide(self):
        if self.border_collision:
            if self.pos.real <= self.radius:
                self.vel = vector(-self.vel.real * self.coefficient_of_restitution, self.vel.imag)
            elif self.pos.real >= (1024 - self.radius):
                self.vel = vector(-self.vel.real * self.coefficient_of_restitution, self.vel.imag)

            if self.pos.imag <= self.radius:
                self.vel = vector(self.vel.real, -self.vel.imag * self.coefficient_of_restitution)
            elif self.pos.imag >= (1024 - self.radius):
                self.vel = vector(self.vel.real, -self.vel.imag * self.coefficient_of_restitution)

    def update(self, dt):
        self.pos += self.vel * dt
        self.vel += self.acc * dt
        self.acc *= 0 # Reset

        # Update shape
        self.shape.x = self.pos.real
        self.shape.y = self.pos.imag
        self.shape.color = self.color

    def draw(self):
        self.shape.draw()

