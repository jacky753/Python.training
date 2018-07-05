class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len =l

    def what_am_i():
        print("I am a shape")

class Rectangle(Shape):
    pass

class Square(Shape):
    pass

a_rectangle = Rectangle(10, 20)
print(a_rectangle.what_am_i())
