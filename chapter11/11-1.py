eng2sp = dict()
print(eng2sp)


eng2sp['one'] = 'uno'
print(eng2sp)


eng2sp = {'one': 'uno', 'two': 'dos',
         'three': 'tres'}
print(eng2sp)


print(eng2sp['two'])

print(len(eng2sp))

print(eng2sp['four'])
#KeyError: 'four'

print('one' in eng2sp)
print('uno' in eng2sp)


vais = eng2sp.values()
'uno' in vais