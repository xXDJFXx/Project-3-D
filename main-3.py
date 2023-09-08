word = ['h','e','c','t','o','r']
good_letters = ['_','_','_','_','_','_']
bad_letters = []
while len(bad_letters) !=6:
  letter = input('Enter a letter: ')
  if letter in word:
    index = word.index(letter)
    good_letters[index] = letter
    print(good_letters)
    print(bad_letters)
    print()
    if good_letters == word:
      print('Victory Royale')
      break
  else:
    bad_letters.append(letter)
    print('That letter is not in the word!')
    print(good_letters)
    print(bad_letters)
    print()
print('Game Over')