import os
cwd = os.getcwd()

print(cwd)
print(os.path.abspath('test_python.txt'))
print(os.path.exists('test_python.txt'))
print(os.path.isdir('test_python.txt'))

print(os.path.listdir(cwd))
#私の使っているパソコンではlistdirを
#使うことが出来なかった

#一応、サンプルの関数を書いておく
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)