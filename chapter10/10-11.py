a = [1, 2, 3]
b = a

print(id(a))
print(id(b))


a[0] = 5
print(a)
print(b)

print(b in a)

#Falseが返ってくる。。。
#わけが分からぬーーーーーーーー

#ver2,3の違いのせいかもしれない.
#調べた限りでは、verの違いについての
#記事は見つからなかった。