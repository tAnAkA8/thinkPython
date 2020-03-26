def printall(*args):
  print(args)

printall(1, 2.0, '3')
#->(1, 2.0, '3')

def printall(*args, **kwargs):
  print(args, kwargs)

printall(1, 2.0, third='3')
#->(1, 2.0) {'third': '3'}


class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return '(%g, %g)' % (self.x, self.y)

d = dict(x=1, y=2)
print(Point(**d))
#->(1, 2)
