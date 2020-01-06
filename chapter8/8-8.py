word = 'banana'
new_word = word.upper()
print(new_word)
#BANANA

index = word.find('a')
print(index)
#1

index = word.find('na')
print(index)
#2

index = word.find('na', 3)
print(index)
#4

name = 'bob'
print(name.find('b', 1, 2))
#-1

