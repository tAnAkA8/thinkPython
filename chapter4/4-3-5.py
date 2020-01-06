import turtle
import math

bob = turtle.Turtle()

def arc(t, r,angle):
  for i in range(angle):
    t.fd((2*r)*math.pi/angle)
    t.lt(angle/angle)

arc(bob,20,90)

#半径r
#bob,delay = 0.01