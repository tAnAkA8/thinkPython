def recures():
  recures()

recures()

#Traceback (most recent call last):
#  File "5-10.py", line 5, in <module>
#    recures()
#  File "5-10.py", line 2, in recures
#    recures()
#  File "5-10.py", line 2, in recures
#    recures()
#  File "5-10.py", line 2, in recures
#    recures()
#  [Previous line repeated 996 more times]
#RecursionError: maximum recursion depth exceeded