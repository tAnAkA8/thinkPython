class Grid():
  def __init__(self,line=0,column=0):
    self.line=line
    self.column=column
    self.cnt = line
    if line < 3:
      self.adjustment=3
      for ad1 in range(line):
        self.adjustment -= 1
    elif line > 3:
      self.adjustment=3
      for ad2 in range(line):
        self.adjustment -= 1
    else:
      self.adjustment = 0

  def side(self):
    print(end='+')
    for i in range(self.line):
      print(' — ',end='')
      if i == self.line-1:
        print('+')
      else:
        print(end='+')

  def vertical(self):
    print('|', end='')
    for hoge in range(self.column):
      for i in range(self.line +self.adjustment):
        print(end=' ')
      if hoge == self.column-1:
        print('|')
      else:
        print(end='|')

  def printGrid(self):
    for i in range(self.cnt):
      grid.side()
      grid.vertical()
    grid.side()

grid=Grid(3,3)
grid.printGrid()

#line   = 行
#column = 列
"""  格子の長さを指定された時用のプログラム。
   指定されてなかったら、print()の方が直観的に出来ると思うので
   自分のやりやすいほうで.
   line == column
   lineとcolumnを変数で分けているのは、プログラムを読みやすくするためです。
   """