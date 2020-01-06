t = ['a', 'b', 'c']
t.append('d')
print(t)
#['a', 'b', 'c', 'd']


t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)
#['a', 'b', 'c', 'd', 'e']

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)
#['a', 'b', 'c', 'd', 'e']