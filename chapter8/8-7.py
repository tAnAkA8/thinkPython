word = 'banana'
count = 0
for letter in word:
  if letter == 'a':
    count = count + 1
print(count)


#-------練習問題-------#

def count(index,word, search):
  cnt = 0
  Search = search
  for letter in word[index:]:
    if letter == Search:
      cnt = cnt + 1
  return cnt
print(count(3,'banana', 'a'))