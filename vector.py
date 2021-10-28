class vector(complex):
    def __init__(self, *args):
        super().__init__()

    def __repr__(self):
        return f'vector({self.real}, {self.imag})'

    def __iter__(self):
        yield self.real
        yield self.imag

    def normal(self):
        return vector(self.real / abs(self), self.imag / abs(self))

    def dot(self, other):
        return self.real * other.real + self.imag * other.imag
