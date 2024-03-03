class people:
    def __init__(self,name):
        self.name=name
    def move(self):
        print(f"{self.name} move")
    def draw(self):
        print(f"{self.name} draw")
p1=people("Danding")
print(p1.name)
p1.draw()


class Children(people):
    pass
class Older(people):
    pass

o=Older("lA")
o.draw()