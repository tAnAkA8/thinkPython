def rotate_word(word, t):
  for i in word:
    if ord(i) + t > 122:
      dev = (ord(i) + t) - 122
      nextWord = 64 + dev
      print(chr(nextWord))
    else:
      nextWord = ord(i) + t
      print(chr(nextWord))


rotate_word('z',5)