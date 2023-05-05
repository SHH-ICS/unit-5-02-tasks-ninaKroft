# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

done = False

while done == False:
    word = input("Please enter your word: ")
    number = len(word)
    print("The length of", word, "is", number, "characters.")
    z = input("Would you like to exit the program? Enter 'quit' for yes. Otherwise, enter anything and the program will run again.")
    if z == 'quit':
        done = True
    