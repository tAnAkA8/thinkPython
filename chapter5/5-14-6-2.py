import turtle
t = turtle.Turtle()

def koch(t, length):

  angle = 60
  if length < 3:
    t.fd(length)
    return

  koch(t,length / 3)
  t.lt(angle)
  koch(t,length / 3)
  t.rt(angle * 2)
  koch(t,length / 3)
  t.lt(angle)
  koch(t, length / 3)


def right(t,n):
  for i in range(3):
    koch(t, n)
    t.rt(120)


right(t,300)
turtle.done()