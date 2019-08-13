word = input("Input a word to reverse: ")

for charachter in range(len(word) - 1, -1, -2):
  print(word[charachter], end="")
print("\n")