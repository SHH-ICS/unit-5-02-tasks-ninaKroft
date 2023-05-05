# Create a program that will accept a word and output the word one letter at a time in reverse.

word = input("Please enter your word: ")

number = len(word)

for x in range(1, number + 1):
    letter = word[-x]
    print(letter)
