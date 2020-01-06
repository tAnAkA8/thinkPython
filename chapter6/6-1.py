import math

def area(radius):
    a = math.pi * radius ** 2
    return a
print(area(30))
#2827.4333882308138


def area(radius):
    return math.pi * radius ** 2
print(area(30))
#2827.4333882308138


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
print(absolute_value(-10))
#10