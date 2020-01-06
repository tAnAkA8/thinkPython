def grid():
  cnt = 0
  while cnt < 3:
    cnt += 1
    for side in range(0,12):
      if side % 5 == 0:
        print('+',end='')
      elif side % 11 == 0:
        print('')
      else:
        print('-',end='')
    if cnt != 3:
      for vertical in range(0,12):
        if vertical % 2 == 0:
          print('¦',end='')
        elif vertical == 5 or vertical == 11:
          print('')
        else:
          print('    ',end='')

grid()