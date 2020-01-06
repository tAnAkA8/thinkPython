def factorial(n):
  if n == 0:
    return 1
  else:
    recurse = factorial(n - 1)
    result = n * recurse
    return result

#factorial(1.5)
#Traceback (most recent call last):
#  File "6-8.py", line 9, in <module>
#    factorial(1.5)
#  File "6-8.py", line 5, in factorial
#    recurse = factorial(n - 1)
#  File "6-8.py", line 5, in factorial
#    recurse = factorial(n - 1)
#  File "6-8.py", line 5, in factorial
#    recurse = factorial(n - 1)
#  [Previous line repeated 995 more times]
#  File "6-8.py", line 2, in factorial
#    if n == 0:
#RecursionError: maximum recursion depth exceeded in comparison


def factorial1(n):
  if not isinstance(n, int):
    print('Factorial is only defined for integers.')
    return None
  elif n < 0:
    print('Factorial is not defined for negative integers.')
    return None
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

print(factorial1(1.5))
#Factorial is only defined for integers.
#None

print(factorial1(-2))
#Factorial is not defined for negative integers.
#None