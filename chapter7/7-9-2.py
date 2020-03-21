#input関数の関係により、
#以下のプログラムはpython2で、動くプログラム

def evel_loop(text=''):
  if text != 'done':
    print(eval(text))
    evel_loop(input())
  else:
    print('done')

evel_loop(input())
