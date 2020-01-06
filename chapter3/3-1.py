type(42)
#<class 'int'>

int('32')
#32

int('hello')
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ValueError: invalid literal for int() with base 10: 'hello'

int(3.99999)
#3

int(-2.3)
#-2

float(32)
#32.0

float('3.14159')
#3.1415899999999999

str(32)
#'32'

str(3.14159)
#'3.14159'