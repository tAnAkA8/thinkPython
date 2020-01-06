a = 'spam'
t = list(a)
print(t)
#[’s’, ’p’, ’a’, ’m’]


s = 'pining for the fjords'
t = s.split()
print(t)
#[’pining’, ’for’, ’the’, ’fjords’]


s = 'spam-spam-spam'
delimiter = '-'
t = s.split(delimiter)
print(t)
#['spam', 'spam', 'spam']


t = ['pining', 'for', 'the', 'fjords']
delimi = ' '
s = delimi.join(t)
print(s)
#pining for the fjords