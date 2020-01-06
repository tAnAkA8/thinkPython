class Point(object):
    """Represents a point in 2-D space"""

blank = Point()

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


box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

center = find_center(box)
print_point(center)