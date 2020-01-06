class Point(object):
    """Represents a point in 2-D space"""

class Rectangle(object):
    """Represents a rectangle

    attributes:width, height, corner
    """

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))


p1 = Point()
box = Rectangle()
box.corner = Point()

p1.x = 3.0
p1.y = 4.0

import copy

p2 = copy.copy(p1)

print_point(p1)
print_point(p2)

print(p1 is p2)
print(p1 == p2)

box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)