# Olivia Adamic
# this program is designed to simulate the popular game of Wordle
# however, this version is called Wordie instead because lawsuits are not bueno
# essentially, this program allows the user to guess what the five-letter word is
# they get 6 chances to accomplish this
# if they guess a letter correctly, then the it will be marked with an 
# * - if it's in the right location or 
# ? - if the letter is right, but in the wrong location and
# x - if the letter is not in the word

import random

#functions
def print_heading(): 
    print("*" * 75)
    print("WORDIE".center(75))
    print("*" * 75)
    print()
    print()
    print("Welcome to WORDIE, the game everyone is playing. Your job is to guess")
    print("a five-letter word. You start with a completely blank set of five letter")
    print("tiles. As you guess a letter that is in the word, it will appear, either")
    print("out of place, in which case it will be marked with a | symbol, or in its")
    print("proper place, where it will be marked with a * symbol. The fewer tries")
    print("it takes you to get all the letters in the right place, the faster you")
    print("will guess the entire word. Only guesses that are actually words in the")
    print("word list will be accepted. Good luck!")
    print()



def game_board(guess_list, word): #takes in the list of guess and target word to compare
    print("Here is the board so far: ")

    for guess in guess_list: #goes through each guess in the guess_list
        vars = [] #this is where the symbols will go
        for ch in range(5): #for every character in range(5) of guess

            if guess[ch] == word[ch]: #if the guess at character 0, 1, 2, 3, or 4 equals that of the word's character at the same spot
                vars.append("*") # then append * to vars

            elif guess[ch] in word and guess[ch] != word:  #if the guess at ch 0, 1, 2, 3, or 4 is in word BUT is not at the same spot
                vars.append("?") # then append ? to vars
                
            else: 
                vars.append("x") #if not in the word at all then it's just x
                    
        print("%-16s%s%16s%16s%16s" % (vars[0], vars[1],vars[2], vars[3], vars[4]))
        print("%-16s%s%16s%16s%16s" % (guess[0], guess[1], guess[2], guess[3], guess[4])) #prints out each character of guess spaced out
        print()
    

#main 
print_heading()


#opening the text file for 5 letter words
fname = "words.txt"
fvar = open(fname, "r")
words = []
for line in fvar:
    line = line.strip()
    words.append(line)
#print(words) 


do_again = "y"

while do_again == "y": 
    guess_list = [] #guesses will be appended to this list
    word = random.choice(words) #randomly selects a word from the file
    num_tries = 0
    guess = ""
    while guess != word and num_tries < 6: 
        print()
        guess = input("Enter your guess: ")
        if guess not in words: 
            print("That word is not in the list.")
        else: 
            guess_list.append(guess)
            num_tries += 1
            game_board(guess_list, word) #calls function to display game board with guesses and symbols
            
    if guess == word:
        print(f"Congratulations. You solved the puzzle in {num_tries} tries.")
        print()
    else: 
        print(f"I'm sorry. You did not guess the word, which was {word}.")
        print()
    do_again = input("Would you like to play again? ")
print()
print("Thank you for playing Wordie!")
print()