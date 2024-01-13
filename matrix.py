matrix = [ [1, 2, 4, 29],
           [3, 4, 6, 1]]

# Summing all elements in the list
# Set counter
counter = 0
# Set outer loop to work with the number of rows
for i in range(len(matrix)):
  # Inner loop to work with the number of element in the row
  for j in range(len(matrix[i])):
    # Implement sum with the help of counter
    counter += matrix[i][j]

# Print counter
print(counter)



matrix = [ [1, 2, 4, 29],
           [3, 4, 6, 1],
          [10, -5, 0]]

# Set outer while loop to work with the number of rows
i = 0
while i < len(matrix):
  # Set inner while loop to work with the number of elements in the row
  j = 0
  while j < len(matrix[i]):
    # Change an element
    matrix[i][j] += 1
    # Print an element
    print(matrix[i][j], end = ' ')
    j +=1
  i += 1
  print('')


  text = 'ofsddsfadfjfojnanjinjudfninvjunjee'
vowels = 'aeiou'

# Set i
i = 0
# Set while loop to work with elements of the text
while i < len(text):
  # Set for loop to work with the elements of the vowels
  for j in range(len(vowels)):
    # If an element in the text is one of the elements in vowels
    if text[i] == vowels[j]:
      # Print an element
      print(text[i])
  i += 1


  matrix = [[' L', '#', 'o', 'o', '#', 's', 'i', 'n', 'g', ' ', '#', 'm', 'y '],
  ['r', 'e', '#', 'l', 'i','#', 'g', 'i', 'o', '#', 'n', '!', 'apspsasd']]

# Set for loop to work with the number of rows 
for i in range(len(matrix)):
  # Set for loop to work with the number of elements of the row
  for j in range(len(matrix[i])):
    # Set condition if an element is '#'
    if matrix[i][j] == '#':
      continue
    # Set condition if an element is '!'
    elif i == '!':
      break
    else:
      # Print an element
      print(matrix[i][j], end=' ')


      text = 'aew$^&hg32yy8wer3$#^*@#7ds983hn'
vowels = 'aeiou'

text_vowels = ''
text_consonants = ''
text_symbols = ''

# Set i
i = 0
# Set outer while loop to work with text
while i < len(text):
  # Set u
  u = 0
  # Set condition *if an element is a letter*
  if text[i].isalpha():
    # Set inner *while* loop to work with vowels
    while u < len(vowels):
      # Set condition *if a letter from the text is in the vowels* 
      if text[i] == vowels[u]:
        # Add the letter to the text_vowels
        text_vowels += text[i]
        break
      # Increase u
      u += 1
    else:
      # Add the letter to the text_consonants
      text_consonants += text[i]
  else:
    # Add the letter to the text_symbols
    text_symbols += text[i]
  i += 1
  
print('Vowels from the text: ', text_vowels)
print('Consonants from the text: ', text_consonants)
print('Symbols from the text: ', text_symbols)