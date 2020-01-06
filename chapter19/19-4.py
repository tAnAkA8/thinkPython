print(any([False, False, True]))
print(any(letter == 't' for letter in 'monty'))

def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

print(avoids('a', 'a'))
