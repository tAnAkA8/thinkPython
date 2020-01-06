import math

def mysqrt(a, x):
  y = 0
  while True:
    y = (x + a / x) / 2
    if x == y:
      return y
    x = y
  auto = math.sqrt(a)
  diff = y - auto

  print(auto)
  print(diff)

mysqrt(8,7)