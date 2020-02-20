import turtle as t

def koch(t, length):
    angle = 60
    if length < 3:
        t.fd(length)
        return
    koch(t, length / 3)
    t.lt(angle)
    koch(t, length / 3)
    t.rt(angle*2)
    koch(t, length / 3)
    t.lt(angle)
    koch(t, length / 3)

koch(t, 250)
t.mainloop()