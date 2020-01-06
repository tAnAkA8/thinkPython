def find(word, letter):
  let = letter
  index = 0
  while index < len(word):
    if word[index] == let[index]:
      return index
    index = index + 1
  return - 1

print(find('letter', 'letter'))



def practiceFind(word, letter,index):
  let = letter
  while index < len(word):
    if word[index] == let[index]:
      return index
    index = index + 1
  return - 1

print(practiceFind('letter','leTter',2))