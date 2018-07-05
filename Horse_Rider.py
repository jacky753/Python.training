class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

jacky = Rider("jacky753")
john = Horse("john", "hunter", jacky)
print(john.owner.name)
