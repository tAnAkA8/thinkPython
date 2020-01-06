def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(-1, 0)

#Traceback (most recent call last):
#  File "5-14-4.py", line 6, in <module>
#    recurse(-1, 0)
#  File "5-14-4.py", line 5, in recurse
#    recurse(n-1, n+s)
#  File "5-14-4.py", line 5, in recurse
#    recurse(n-1, n+s)
#  File "5-14-4.py", line 5, in recurse
#    recurse(n-1, n+s)
#  [Previous line repeated 995 more times]
#  File "5-14-4.py", line 2, in recurse
#    if n == 0:
#RecursionError: maximum recursion depth exceeded in comparison
