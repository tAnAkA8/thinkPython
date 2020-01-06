d = {'a': 0, 'b': 1, 'c': 2}
t = d.items()
print(t)


for key, value in d.items():
    print(key, value)


t = [('a', 0), ('b', 1), ('c', 2)]
d = dict(t)
print(d)


d = dict(zip('abc', range(3)))
print(d)


dictionary = dict()
last = 0
first = 0

number = (1,2)
dictionary[last, first] = number
for last, first in dictionary:
    print(first, last, dictionary[last, first])
