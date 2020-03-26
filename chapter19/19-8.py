class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return '(%g, %g)' % (self.x, self.y)


print(Point)
#-><class '__main__.Point'>

p = Point(1, 2)
print(p)
#->(1, 2)

print(p.x, p.y)
#->1 2
