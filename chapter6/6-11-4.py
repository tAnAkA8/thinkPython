def is_power(a, b):
  if a % b == 0:
    if b < a:
      for i in range(1000):
        debug_b = b ** i
        if debug_b == a:
          return True
      else:
        return "not_power"
    else:
      return "b==a"
  else:
    return "not_int"

print(is_power(19683,3))