import time

print(time.time())
#1572688198.327228


def check_fermat(a,b,c,n):
  if a**n + b**n == c**n:
    print('おやまあ、フェルマーは間違っている')
  else:
    print('だめだ。成り立たない')

check_fermat(5, 3, 9, 15)
#だめだ。成り立たない