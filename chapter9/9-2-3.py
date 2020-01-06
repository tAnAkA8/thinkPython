import re
fin = open('words.txt')

def avoids(t):
  x = 0
  one = input()
  two = input()
  three = input()
  four = input()
  five = input()
  for i in t:
    if re.search(one, i) or re.search(two, i) or re.search(three, i) or re.search(four, i) or re.search(five, i):
      x = x + 1
    else:
      word = i.strip()
      print(word)
  print('True *',x)

avoids(fin)

#最小になる組み合わせ
#a,e,o,s,n