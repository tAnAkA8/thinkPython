from collections import Counter

count = Counter('parrot')
print(count)
print(count['d'])

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

count = Counter('parrot')
for val, freq in count.most_common(3):
    print(val, freq)