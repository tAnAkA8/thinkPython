fruit = 'banana'
index = 0
while index < len(fruit):
  letter = fruit[index]
  print(letter)
  index = index + 1



def bk_fruit(bk=''):
  letter = bk
  print(letter[::-1])

bk_fruit('banana')



prefixes = 'JKLMNOPQ'
sufix = 'ack'
for letter in prefixes:
  if letter == 'O' or letter =='Q':
    print(letter + 'u' + sufix)
  else:
    print(letter + sufix)