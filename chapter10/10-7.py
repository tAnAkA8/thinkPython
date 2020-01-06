def add_all(t):
    total = 0
    for x in t:
        total += x
    return x

t1 = [1,2,3,4,5]
print(add_all(t1))

print(sum(t1))


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

t2 = ['a','i','u']
print(capitalize_all(t2))