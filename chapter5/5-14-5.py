import turtle
t = turtle.Turtle()
n = 28

def draw(t, length):

  angle = 60
  if length < 3:
    t.fd(length)
    return

  draw(t,length / 3)
  t.lt(angle)
  draw(t,length / 3)
  t.rt(angle * 2)
  draw(t,length / 3)
  t.lt(angle)
  draw(t, length / 3)

draw(t,100)
turtle.done()