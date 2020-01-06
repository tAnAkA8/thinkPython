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

box.width = box.width + 50
box.height = box.height + 100


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)


def move_rectangle(rect, dx, dy):
    rect.x += dx
    rect.y += dy

move_rectangle(box.corner, 50, 100)
print(box.corner.x,box.corner.y)