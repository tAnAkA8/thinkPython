def countdown(n):
  if n == 0:
    print('Blastoff!')
  else:
    print(n)
    countdown(n - 1)

countdown(3)
#3
#2
#1
#Blastoff!



n = 0
def print_n(s, n):
  if n <= 0:
    return print(s)

print_n('ok', n - 1)
#ok