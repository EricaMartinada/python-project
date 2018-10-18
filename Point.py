#Class Definition
class Point:
    
    def __init__(self, x =0.0, y = 0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})". format (self.x, self.y)

    def distance_from_origin (self):
        d + sqrt (self.x ** 2 + self.y ** 2)
        return d

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

#Object Instantation
p = Point()
print ("p.x={}, p.y= {}". format (p.x, p.y))
print ("p = {}". format (p))

p = Point (x=3.5, y=4.5)
print ("p.x={}, p.y= {}". format (p.x, p.y))
print ("p = {}". format (p))

class Person



