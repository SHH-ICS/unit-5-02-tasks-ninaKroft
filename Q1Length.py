# Create a program that will accept a word from a user and return the length of that word. 
# Make this program in a loop with option to exit when the use types in quit.

done = False

while done == False:
    word = input("Please enter your word: ")
    word = len(word)
    print("The length of your word is", word, "characters.")
    z = input("Would you like to exit the program? Enter 'quit' for yes or 'continue' for no. ")
    if z == 'quit':
        done = True
    else:
        print("Please enter 'y' for yes or 'n' for no.")