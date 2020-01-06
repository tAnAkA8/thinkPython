def cumsum(t):
  hoge = 0
  hogehoge = []
  for i in t:
    hoge += i
    hogehoge.append(hoge)
  print(hogehoge)

t = [1, 2, 3]
cumsum(t)

#翻訳が翻訳で、累積の定義が訳分からんから,
#取り敢えず足した