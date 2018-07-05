class Triangle:
    def __init__(self, l, h):
        self.len = l
        self.high = h

    def area(self):
        return self.len * self.high / 2

    def change_size(self, l, h):
        self.len = l
        self.high = h

triangle = Triangle(2, 2)
print(triangle.area())
triangle.change_size(1, 3)
print(triangle.area())
