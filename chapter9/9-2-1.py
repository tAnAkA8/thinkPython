fin = open('words.txt')
for line in fin:
    if len(line) >= 20:
        word = line.strip()
        print(word)