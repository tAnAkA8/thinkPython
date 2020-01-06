def histogram(s):
    d = dict()
    for c in s:
        if c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
    return d

def print_hist(h):
    for c in h:
        print(c, h[c])

h = histogram('parrot')
print_hist(h)