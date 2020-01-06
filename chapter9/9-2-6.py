fin = open('words.txt')

def is_abecedarian(t):
  x = 0
  old = 0
  for i in t:
    for u in i:
      new = ord(u)
      if new - old == 1:
        x = x + 1
        print('True')
      else:
        break
    old = new
  print(x)

is_abecedarian(fin)

#1305個ある