def is_anagram(t, t1):
    if sorted(t) == sorted(t1):
        print('True')
    else:
        print('False')

t = [1,2,3]
t1 = [2,3,1]
is_anagram(t, t1)
#True

t = [1,2,3]
t1 = [2,3,1,4]
is_anagram(t, t1)
#False