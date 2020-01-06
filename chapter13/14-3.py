f = open('test_python.txt','w')

x = 32
f.write(str(x))

camels = 42
print('%d' % camels)
print('I hava spotted %d camels' % camels)
print('In %d yrears I have spotted %g %s'
        % (3, 0.1, 'camels'))

'%d %d %d' % (1, 2)
'%d' % 'doliara'
#TypeError: not enough arguments for format string
#TypeError: %d format: a number is required, not str
