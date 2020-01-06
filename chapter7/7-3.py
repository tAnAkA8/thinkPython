def countdown(n):
  while n > 0:
    print(n)
    n = n - 1
    print('Blastoff!')

countdown(5)
#5
#Blastoff!
#4
#Blastoff!
#3
#Blastoff!
#2
#Blastoff!
#1
#Blastoff!


def sequence(n):
  while n != 1:
    print(n)
    if n % 2 == 0:
      n = n / 2
    else:
      n = n * 3 + 1

sequence(10)
#10
#5.0
#16.0
#8.0
#4.0
#2.0