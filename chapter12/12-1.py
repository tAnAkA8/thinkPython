t = 'a', 'b', 'c', 'd', 'e'
print(t)
t = ('a', 'b', 'c', 'd', 'e')
print(t)

t1 = 'a',
print(type(t1))

t2 = ('a')
print(type(t2))


t = tuple()
print(t)


t = tuple('Lupins')
print(t)

t = ('a', 'b', 'c', 'd', 'e')
print(t[0])

print(t[1:3])


t = ('A',) + t[1:]
print(t)

print((0, 1, 2) < (0, 3, 4))
print((0,1,2000000) < (0,3,4))