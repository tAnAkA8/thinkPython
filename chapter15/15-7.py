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


p = Point()
box = Rectangle()
box.corner = Point()

p.x = 3
p.y = 4
#p.z
#'Point' object has no attribute 'z'

print(type(p))

print(hasattr(p, 'x'))
print(hasattr(p, 'z'))