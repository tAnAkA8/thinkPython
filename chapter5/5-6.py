#x < y  True program
x = 1
y = 2
if x < y:
  print('x is less than y')
elif x > y:
  print('x is greater than y')
else:
  print('x and y are equal')
#x is less than y



#choice = 'b'  True program
choice = 'b'

def draw_b():
  print('b == True program  OK!!')

if choice == 'a':
  draw_a()
elif choice == 'b':
  draw_b()
elif choice == 'c':
  draw_c()

#b == True program  OK!!