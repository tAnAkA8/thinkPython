def is_abecedarisn(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print(is_abecedarisn('abc'))



def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

print(is_abecedarian('ba'))




#whileを使うと以下のようになる
def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True