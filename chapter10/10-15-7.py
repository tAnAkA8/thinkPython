def has_duplicated(t):
  t.sort()
  for i in range(len(t)-1):
    if t[i] == t[i + 1]:
      return True
    else:
      return False

t = [1,2,3,1]
print(has_duplicated(t))