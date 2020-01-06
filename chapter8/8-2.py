fruit = 'banana'
print(len(fruit))
#6

length = len(fruit)
last = fruit[length]
#IndexError: string index out of range

last = fruit[length - 1]
print(last)
#a