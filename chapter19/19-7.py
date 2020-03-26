from collections import defaultdict
d = defaultdict(list)

t = d['new key']
print(t)

t.append('new calue')
print(d)

def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        d.setdefault(t, []).append(word)
    return d

