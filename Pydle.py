# Task 1 Harrison Macdonald
# Student number: 28958802

# All Imports to be placed here.
import random
import time
import tkinter
tkinter.BaseWidget = 100

# Constants
MaxGuesses = 6
WordsetSize4 = 4
WordsetSize5 = 5
WordsetSize6 = 6
# Allows user to input a username 
def username_input():
    global Username
    Username = input("Pick a username\n> ")
    
    return Username
# Function to load words from the dictionary.txt file
def load_words():
    Dictionary = open(r"dictionary.txt", mode="r")
    #reading the file and giving it a variable name: text
    text = Dictionary.readlines()
    Dictionary.close()
    #list of all words in the dictionary
    Wordset = []
    for strip in text:
        Wordset.append(strip.strip().lower())
    return Wordset

# Function to select a random word of the specified length from the words_list
def select_random_word(Wordset):
    global ValidFiveLetters
    FiveLetter = []
    for Word in Wordset:
        if len(Word) == 5:
            FiveLetter.append(Word)
    ValidFiveLetters = FiveLetter
    return random.choice(FiveLetter)


# Function to get the user's guess and ensure it is valid
def get_guess():
    global Guess
    while True:
        Guess = input("Please make your guess\n>")
        Guess = Guess.lower()
        return Guess

# Function to provide feedback on the guess (clue generation)
def provide_clue(Guess):
    #checking for the correct characters in every slot ["*"]
    handle_turns(Guess, ActualWord)
    Clue = list("_____")
    for i in range(len(Guess)):
        if Guess[i] == ActualWord[i]:
            Clue[i] = '*'

    #checking for right letter wrong position ["+"]
    for i in range(len(Guess)):
        #check the character if it isnt already marked "*"
        if Clue[i] == '_': 
            if Guess[i] in ActualWord:
                Clue[i] = '+' 
    return "".join(Clue)

# Function to handle the player's turn.
# It can return if the guess was correct.
# The clue and previous guesses.
def handle_turns(guess, ActualWord):
   while True:
        if len(guess) != len(ActualWord):
           return print("Error: Guess needs to be five letters long.")
        elif guess not in ValidFiveLetters:
            return print(f"Error: Word not found in dictionary.")
        elif guess == ActualWord:
            return print("Congratulations, the word is correct")

# Function to display the game result (win/loss)
def display_result(is_winner, answer):
    global TimeTaken

    # Win condition
    if is_winner:
        TimeEnd = time.time() 
        print("Congratulations! You have won the game")
        TimeTaken = int(TimeEnd - TimeStart)
        print(f"Time taken:", TimeTaken, "Seconds")

        # Opens the winners.txt file and enters the username and timetaken to solve the game.
        with open(r"winners.txt", "a") as leaderboard_Winners:
            leaderboard_Winners.write(f"{Username} | {TimeTaken} seconds\n")

    else:
        TimeEnd = time.time()
        TimeTaken = int(TimeEnd - TimeStart)
        print("You have lost the game")
        print(f"The correct word was", answer)

        # Opens the Losers.txt file and enters the username and timetaken at the attempt.
        with open(r"Losers.txt", "a") as leaderboard_Losers:
            leaderboard_Losers.write(f"{Username} | {TimeTaken} seconds\n")

# Function to handle the player's decision to give up
def give_up(ActualWord):
    print("\nYou have chosen to exit, Thanks for playing")
    print("The correct word was", ActualWord)



# Function to handle the main game loop
def main():
    global ActualWord
    global TimeStart
    print("<| Welcome to Wordle |>")
    print("\n<<|To exit the game please type: [exit] |>>\n  ")
    username_input()

    # Getting the actual word for guessing
    ActualWord = select_random_word(load_words())

    # Debug answer
    print(ActualWord)
    
    # Starting a timer for the winning.txt file.
    TimeStart = time.time()

    # Guessing system for the game
    GuessCount = MaxGuesses
    while GuessCount != 0:
        print("You have", GuessCount, "guesses left")
        guess = get_guess()
        if guess == ActualWord:
            display_result(True, ActualWord)
            return
        elif guess == "exit":
            give_up(ActualWord)
            return
        else:
            print(provide_clue(guess))
        GuessCount -= 1

    display_result(False, ActualWord)

main()
