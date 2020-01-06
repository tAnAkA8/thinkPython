def delete_head(t):
  del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)

t1 = [1, 2]
t2 = t1.append(3)
print(t1)
print(t2)

t4 = t1 + [4]
print(t4)



def bad_delete_head(t):
  t = t[1:]

t4 = [1, 2, 3]
bad_delete_head(t4)
print(t4)



def tail(t):
  return t[1:]

letter = ['a', 'b', 'c']
rest = tail(letter)
print(rest)