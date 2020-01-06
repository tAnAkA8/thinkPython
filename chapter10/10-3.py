cheeses = ['Cheddar', 'Edam', 'Gouda']
for cheese in cheeses:
    print(cheese)
#Cheddar
#Edam
#Gouda


numbers = [17, 123]
for i in range(len(numbers)):
    numbers[i] = numbers[i]*2
    print(numbers[i])
#34
#246


for x in []:
    print('This never happens')