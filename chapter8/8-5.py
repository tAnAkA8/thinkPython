greeting = 'Hello World!'
greeting[0] = 'J'
#TypeError: 'str' object does not support item assignment


greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print(new_greeting)
#Jello, world!