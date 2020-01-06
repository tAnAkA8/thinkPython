import math

def distance(xc, yc, xp, yp):
    return 0.0

def area(radius):
    a = math.pi * radius ** 2
    return a

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

area(30)
circle_area(1, 2, 4, 6)

radius = distance(1, 2, 4, 6)
result = area(radius)

print(radius)
print(result)