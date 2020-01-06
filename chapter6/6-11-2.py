def ack(m,n):
  if m == 0:
    n = n + 1
    print(n)
  elif m > 0 and n == 0:
    m = m - 1
    n = 1
  elif m > 0 and n > 0:
    m = m - 1
    print(m)

ack(3, 4)
#2