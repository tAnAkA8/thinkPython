def nested_sum(t):
  hoge = 0
  for i in t:
    hoge += sum(i)
  print(hoge)

t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)