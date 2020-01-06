def subtract(d1, d2):
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def subtract(d1, d2):
    return set(d1) - set(d2)

def has_duplicates(t):
    return len(set(t)) < len(t)

def uses_only(word, available):
    return set(word) <= set(available)