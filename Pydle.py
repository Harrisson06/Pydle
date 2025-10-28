# Task 1 Harrison Macdonald
# Student number: 28958802

# All Imports to be placed here.
import random
import time
import tkinter as tk
from tkinter import messagebox

# Constants
MaxGuesses = 6
Word_Length = 5
BUTTON_COLOR = "#D3D6DA"
CORRECT_COLOR = "#6AAA64"
PRESENT_COLOR = "#C9B458"
ABSENT_COLOR = "#787C7E"

class WordleGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pydle")
        self.window.resizable(False, False)

        self.current_row = 0
        self.current_col = 0
        self.game_over = False

        # Load words and select target word
        self.word_list = load_words()
        self.target_word = select_random_word(self.word_list)
        self.time_start = time.time()

        # Create the grid.
        self.cells = []
        for i in range(MaxGuesses):
            row = []
            for j in range(Word_Length):
                cell = tk.Label(
                    self.window,
                    width=4,
                    height=2,
                    relief="solid",
                    font=("Arial", 24, "bold"),
                    bg=BUTTON_COLOR
                )
                cell.grid(row=i, column=j, padx=2, pady=2)
                row.append(cell)
            self.cells.append(row)

        # Creates keyboard
        self.create_keyboard()

        # Bind key presses
        self.window.bind("<Key>", self.key_press)
        self.window.bind("<Return>", self.check_guess)
        self.window.bind("<BackSpace>", self.backspace)

    def create_keyboard(self):
        keyboard_layout = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"]
        ]

        keyboard_frame = tk.Frame(self.window)
        keyboard_frame.grid(row=MaxGuesses+1, columnspan=Word_Length)

        for i, row in enumerate(keyboard_layout):
            row_frame = tk.Frame(keyboard_frame)
            row_frame.grid(row=i,column=0)

            for letter in row:
                button = tk.Button(
                    row_frame,
                    text=letter,
                    width=4,
                    height=2,
                    bg=BUTTON_COLOR,
                    command=lambda l=letter: self.key_press(type('Event', (), {'char' : l.lower()}))
                )
                button.pack(side=tk.LEFT, padx=1, pady=1)
    
    def key_press(self, event):
        if self.game_over:
            return
        
        if event.char.isalpha() and self.current_col < Word_Length:
            self.cells[self.current_row][self.current_col].config(text=event.char.upper())
            self.current_col += 1
    
    def backspace(self, event):
        if self.game_over:
            return
        
        if self.current_col > 0:
            self.current_col -= 1
            self.cells[self.current_row][self.current_col].config(text="")
    
    def check_guess(self, event):
        if self.game_over or self.current_col < Word_Length:
            return

        guess = "".join(cell["text"].lower() for cell in self.cells[self.current_row])

        if guess not in self.word_list:
            messagebox.showwarning("Error", "Word not found in dictionary.")
            return
        
        # Check letters and update colors
        for i in range(Word_Length):
            if guess[i] == self.target_word[i]:
                self.cells[self.current_row][i].config(bg=CORRECT_COLOR, fg="white")

            elif guess[i] in self.target_word:
                self.cells[self.current_row][i].config(bg=PRESENT_COLOR, fg="white")
            else:
                self.cells[self.current_row][i].config(bg=ABSENT_COLOR, fg="white")
            

        if guess == self.target_word:
            self.game_over = True
            time_taken = int(time.time() - self.time_start)
            messagebox.showinfo("Congratulations!", f"You've guessed the word in {time_taken} seconds!")
            return
        
        self.current_row += 1
        self.current_col = 0

        if self.current_row >= MaxGuesses:
            self.game_over = True
            messagebox.showinfo("Game Over", f"The correct word was: {self.target_word}")

    def run(self):
        self.window.mainloop()


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

# Function to handle the main game loop
def main():
    print("<| Welcome to Wordle |>")
    print("\nYou have 6 attempts to guess the 5-letter word.\n")

    game = WordleGUI()

    # Debug answer
    print(game.target_word)
    game.run()

if __name__ == "__main__":
    main()
