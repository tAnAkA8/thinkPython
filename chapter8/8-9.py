print('a' in 'banana')
#True

print('seed' in 'banana')
#False


def in_both(word1, word2):
  for letter in word1:
    if letter in word2:
      print(letter)

in_both('apples', 'oranges')