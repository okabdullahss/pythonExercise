import math


# slope y2-y1 / x2- x1
class Line:

    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)


l1 = Line((3, 2), (8, 10))

print(l1.distance())
print(l1.slope())


class Clyndir:

    def __init__(self, height, radius):
        self.height = height
        self.radius = radius
        self.pi = 3.14

    def volume(self):
        return (self.pi*(self.radius**2)*self.height)

    def surface_area(self):
        return (2*self.pi*self.radius*self.height)+2*self.pi*(self.radius** 2)


c1 = Clyndir(2, 3)
print(f"the volume  of a clyndir with r= {c1.radius} and h={c1.height} is: "+ str(c1.volume()))
print(f"surface area of a clyndir with r= {c1.radius} and h={c1.height} is: " +str(c1.surface_area()))
