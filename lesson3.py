symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c
print(MAP)

result = "34 DF 56 AC E F".translate(MAP)
print(result)


for i in range(9, 4, -1):
  # Set inner loop for the number of elements in the row
  for j in range(1, i + 1):
    # Print '*'
    print("*", end=' ')
  print('')


  print('')

