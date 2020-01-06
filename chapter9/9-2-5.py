import re
fin = open('uses_all.txt')

def uses_all(t, judge):
  for i in t:
    for jud in judge:
      if re.search(jud,i):
        return print(True)
    else:
      print(i)


uses_all(fin,'qwpla')