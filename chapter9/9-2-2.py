fin = open('Cadsby.txt')

def has_no_e(t):
  for line in t:
    if line != 'e':
      return True

print(has_no_e(fin))




fan = open('words.txt')

def print_no_e(t):
  x = 0
  for line in t:
    if 'e' in line:
      x = x +1
    else:
      word = line.strip()
      print(word)
  percent = 113809 / 100
  ans = x // percent
  return ans

print(print_no_e(fan))