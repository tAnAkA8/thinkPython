def gcd(a, b):
  for i in range(a + b):
    if i != 0:
      if a % i == 0 and b % i == 0:
        r = i
  return r

print(gcd(4480, 8960))
#4480