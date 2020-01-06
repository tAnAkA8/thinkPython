import math
import turtle

bob = turtle.Turtle()

def arc(t, r, angle):
  cnt = 0
  for i in range(angle):
    cnt += 1
    t.fd(2 * r * math.pi / angle)
    t.lt(angle / angle)
    if cnt == angle:
      t.lt(90+45)
      for i in range(angle):
        t.fd(2 * r * math.pi / angle)
        t.lt(angle / angle)
  t.rt(22.5)

def call_def(repeat):
  for i in range(repeat):
    arc(bob, 20, 45)

call_def(7)

#bob.mainloop()