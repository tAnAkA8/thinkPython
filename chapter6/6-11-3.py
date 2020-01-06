def is_palindrome(word):
  if len(word) >= 3:
    for i in range(len(word)):
      if word[0+i] == word[-1-i]:
        return True
      else:
        return False
  else:
    return "lengthMiss"

print(is_palindrome("noon"))