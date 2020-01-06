class Point(object):
    """Represents a point in 2-D space"""

blank = Point()

class Rectangle(object):
    """Represents a rectangle

    attributes:width, height, corner
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0