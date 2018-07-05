class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14
    
    def change_size(self, r):
        self.radius = r


circle = Circle(1)
print(circle.area())
circle.change_size(2)
print(circle.area())
        
