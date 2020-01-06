t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
#['b', 'c']

print(t[:4])
#['a', 'b', 'c', 'd']

print(t[3:])
#[’d’, ’e’, ’f’]

print(t[:])
#[’a’, ’b’, ’c’, ’d’, ’e’, ’f’]


t[1:3] = ['x', 'y']
print(t)
#[’a’, ’x’, ’y’, ’d’, ’e’, ’f’]