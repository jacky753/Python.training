class Hexagon:
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 6

hexagon = Hexagon(1)
print(hexagon.calculate_perimeter())    
