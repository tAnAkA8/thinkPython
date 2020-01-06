import math

class Point(object):
    """Represents a point in 2-D space"""

blank = Point()

blank.x = 3.0
blank.y = 4.0
print(blank.x, blank.y)

print('(%g, %g)' % (blank.x, blank.y))

distance = math.sqrt(blank.x ** 2 + blank.y ** 2)
print(distance)


def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(blank)


def distance_between_points(p):
    distance = math.sqrt(blank.x ** 2 + blank.y ** 2)
    return distance

print(distance_between_points(blank))