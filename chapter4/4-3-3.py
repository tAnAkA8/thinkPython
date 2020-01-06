import turtle

bob = turtle.Turtle()

def polygon(t,n):
	for i in range(n):
		t.fd(50)
		t.lt(360/n)

polygon(bob, 12)