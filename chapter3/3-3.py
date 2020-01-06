import math
degrees = 45
x = math.sin(degrees / 360 * 2 * math.pi)
print(x)
#0.7071067811865476


y = math.exp(math.log(x + 1))
print(y)
#1.7071067811865475


hours = 1
minutes = hours * 60
print(minutes)
#60


hours * 60 = minute
#hours = 1
minutes = hours * 60
print(minutes)
#  File "3-3.py", line 19
#    hours * 60 = minute
#    ^
#SyntaxError: can't assign to operator