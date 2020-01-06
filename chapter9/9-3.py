def has_no_e(word):
  for letter in word:
    if letter == 'e':
      return False
    return True

print(has_no_e('e'))
#False


def avoids(word, forbidden):
  for letter in word:
    if letter in forbidden:
      return False
    return True

print(avoids('a', 'e'))
#eが含まれているかどうかの判定
#True


def uses_only(word, available):
  for letter in word:
    if letter not in available:
      return False
  return True

print(uses_only('e', 'e'))
#avoidsの条件の反転


def uses_all(word, required):
  for letter in required:
    if letter not in word:
      return False
  return True