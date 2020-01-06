import re
fin = open('uses_only.txt')

def uses_only(t, judge):
  for i in t:
    if re.search(judge,i):
      return print(True)
    else:
      print(i)

uses_only(fin, 'acefhlo')