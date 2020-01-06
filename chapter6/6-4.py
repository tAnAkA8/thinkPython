#function0 is True program
def is_divisible0(x, y):
  if x % y == 0:
    return True
  else:
    return False

print(is_divisible0(2, 2))


#function1 is return program
def is_divisible1(x, y):
  return x % y == 0

if is_divisible1(2,2):
  print('x is divisible by y')