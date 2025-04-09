# Task 1 Harrison Macdonald
# Student number: 28958802

#All Imports to be placed here.
import random
import time

#Constants
max_guesses = 6

#Allows user to input a username 
def username_input():
    global username
    username = input("Pick a username\n> ")
    
    return username
# Function to load words from the dictionary.txt file
def load_words():
    dictionary = open(r"C:\A UNIWORK\python\Final peices\dictionary.txt", mode="r")
    #reading the file and giving it a variable name: text
    text = dictionary.readlines()
    dictionary.close()
    #list of all words in the dictionary
    wordset = []
    for strip in text:
        wordset.append(strip.strip().lower())
    return wordset

# Function to select a random word of the specified length from the words_list
def select_random_word(wordset):
    global valid_five_letters
    five_letter = []
    for word in wordset:
        if len(word) == 5:
            five_letter.append(word)
    valid_five_letters = five_letter
    return random.choice(five_letter)


# Function to get the user's guess and ensure it is valid
def get_guess():
    global guess
    while True:
        guess = input("Please make your guess\n>")
        guess = guess.lower()
        return guess

# Function to provide feedback on the guess (clue generation)
def provide_clue(guess):
    #checking for the correct characters in every slot ["*"]
    handle_turns(guess, actual_word)
    clue = list("_____")
    for i in range(len(guess)):
        if guess[i] == actual_word[i]:
            clue[i] = '*'

    #checking for right letter wrong position ["+"]
    for i in range(len(guess)):
        #check the character if it isnt already marked "*"
        if clue[i] == '_': 
            if guess[i] in actual_word:
                clue[i] = '+' 
    return "".join(clue)

# Function to handle the player's turn.
# It can return if the guess was correct.
# The clue and previous guesses.
def handle_turns(guess, actual_word):
   while True:
        if len(guess) != len(actual_word):
           return print("Error: Guess needs to be five letters long.")
        elif guess not in valid_five_letters:
            return print(f"Error: Word not found in dictionary.")
        elif guess == actual_word:
            return print("Congratulations, the word is correct")


# Function to display the game result (win/loss)
def display_result(is_winner, answer):
    global time_taken
    # Win condition
    if is_winner:
        time_end = time.time() 
        print("Congratulations! You have won the game")
        time_taken = int(time_end - time_start)
        print(f"Time taken:", time_taken, "Seconds")

        # Opens the winners.txt file and enters the username and timetaken to solve the game.
        leaderboard_Winners = []
        with open(r"C:\A UNIWORK\python\Final peices\winners.txt", "r") as temp:
            leaderboard_Winners = [line.replace("\n", " ") for line in temp.readlines()]
            for i in leaderboard_Winners:
                return i
    else:
        time_end = time.time()
        time_taken = int(time_end - time_start)
        print("You have lost the game")
        print(f"The correct word was", answer)
        with open(r"C:\A UNIWORK\python\Final peices\Losers.txt", "a") as leaderboard_Losers:
            leaderboard_Losers.write(f"{username} | {time_taken} seconds\n")

# Function to handle the player's decision to give up
def give_up(actual_word):
    print("\nYou have chosen to exit, Thanks for playing")
    print("The correct word was", actual_word)



# Function to handle the main game loop
def main():
    global actual_word
    global time_start
    print("<| Welcome to Wordle |>")
    print("\n<<|To exit the game please type: [exit] |>>\n  ")
    username_input()

    # Getting the actual word for guessing
    actual_word = select_random_word(load_words())

    # Debug answer
    print(actual_word)
    
    # Starting a timer for the winning.txt file.
    time_start = time.time()

    # Guessing system for the game
    guess_count = max_guesses
    while guess_count != 0:
        print("You have", guess_count, "guesses left")
        guess = get_guess()
        if guess == actual_word:
            display_result(True, actual_word)
            return
        elif guess == "exit":
            give_up(actual_word)
            return
        else:
            print(provide_clue(guess))
        guess_count -= 1

    display_result(False, actual_word)

main()
