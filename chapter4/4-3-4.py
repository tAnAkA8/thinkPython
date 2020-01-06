import turtle
import math

bob = turtle.Turtle()

def circle(t, r):
  for i in range(360):
    t.fd((2*r)*math.pi/360)
    t.lt(360/360)

circle(bob,20)

#半径r
#bob,delay = 0.01