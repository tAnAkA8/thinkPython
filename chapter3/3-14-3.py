def grid():
  cnt = 0
  while cnt < 5:
    cnt += 1
    for side in range(0,22):
      if side % 5 == 0:
        print('+',end='')
      elif side % 21 == 0:
        print('')
      else:
        print('-',end='')
    if cnt != 5:
      for vertical in range(0,20):
        if vertical % 2 == 0:
          print('¦',end='')
        elif vertical %9 == 0:
          print('')
        elif vertical % 19 == 0:
          print('')
        else:
          print('    ',end='')

grid()