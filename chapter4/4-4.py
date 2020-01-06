import turtle

bob = turtle.Turtle()
alice = turtle.Turtle()

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)
square(bob)
square(alice)