fin = open('words.txt')
print(fin.readline())
print(fin.readline())


line = fin.readline()
word = line.strip()
print(word)


fin = open('words.txt')
for line in fin:
    word = line.strip()
    print(word)