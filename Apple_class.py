class Apple:
    def __init__(self, w, c, t, m):
        self.weight = w
        self.color = c
        self.taste = t
        self.maker = m
        print("Created!")


ap1 = Apple(100, "red", "sweet", "japanese")
print(ap1.color)
