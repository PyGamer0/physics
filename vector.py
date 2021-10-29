class vector:
    def __init__(self, *args):
        if len(args) == 0:
            self.x = 0
            self.y = 0
        elif len(args) == 1:
            self.x = args[0]
            self.y = args[0]
        else:
            self.x = args[0]
            self.y = args[1]

    def __repr__(self):
        return f'vector({self.x}, {self.y})'

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        if type(other) == vector:
            return vector(self.x * other.x, self.y * other.y)
        return vector(self.x * other, self.y * other)
    
    def __imul__(self, other):
        if type(other) == vector:
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self

    def __div__(self, other):
        if type(other) == vector:
            return vector(self.x / other.x, self.y / other.y)
        return vector(self.x / other, self.y / other)

    def __idiv__(self, other):
        if type(other) == vector:
            self.x /= other.x
            self.y /= other.y
        else:
            self.x /= other
            self.y /= other
        return self

    def __iter__(self):
        yield self.x
        yield self.y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def normal(self):
        return vector(self.x / abs(self), self.y / abs(self))

    def dot(self, other):
        return self.y * other.x + self.x * other.y
