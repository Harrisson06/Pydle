# Task 1 Harrison Macdonald
# Student number: 28958802

# All Imports to be placed here.
import random
import time
import tkinter as tk
from tkinter import messagebox

# Constants
MaxGuesses = 6
BUTTON_COLOR = "#D3D6DA"
CORRECT_COLOR = "#6AAA64"
PRESENT_COLOR = "#C9B458"
ABSENT_COLOR = "#787C7E"

class WordLengthSelector:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pydle - Select Word Length")
        self.window.geometry("300x200")
        self.selected_length = None

        Welcome_lable = tk.Label(
            self.window,
            text="Welcome to Pydle\nSelect word Length:",
            font=("Arial", 14),
            pady=20
        )
        Welcome_lable.pack()

        for length in [4, 5, 6]:
            btn = tk.Button(
                self.window,
                text=f"{length} Letters",
                width=20,
                command=lambda l=length: self.select_length(l)
            )
            btn.pack(pady=5)

    def select_length(self, length):
        self.selected_length = length
        self.window.destroy()
        
    def get_selection(self):
        self.window.mainloop()
        return self.selected_length


class WordleGUI:

    # Initialize the GUIw
    def __init__(self, word_length):
        self.word_length = word_length

        self.window = tk.Tk()
        self.window.title(f"Pydle - {self.word_length} Letters")
        self.window.resizable(False, False)

        self.current_row = 0
        self.current_col = 0
        self.game_over = False

        if self.word_length == 4:
            fname = r"dictionary4.txt"
        elif self.word_length == 5:
            fname = r"dictionary5.txt"
        elif self.word_length == 6:
            fname = r"dictionary6.txt"

        with open(fname, "r") as f:
            self.word_list = [word.strip().lower() for word in f.readlines()]

        self.target_word = select_random_word(self.word_list, self.word_length)
        self.time_start = time.time()

                # Create the grid.
        self.cells = []
        for i in range(MaxGuesses):
            row = []
            for j in range(self.word_length):
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

    # Create a on-screen keyboard
    def create_keyboard(self):
        keyboard_layout = [
            ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
            ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
            ["Z", "X", "C", "V", "B", "N", "M"]
        ]

        # Create keyboard frame
        keyboard_frame = tk.Frame(self.window)
        keyboard_frame.grid(row=MaxGuesses+1, columnspan=self.word_length)

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
    
    # Handle key presses
    def key_press(self, event):
        if self.game_over:
            return

        if event.char.isalpha() and self.current_col < self.word_length:
            self.cells[self.current_row][self.current_col].config(text=event.char.upper())
            self.current_col += 1
    
    # handles backspace key presses
    def backspace(self, event=None):
        if self.game_over:
            return
        
        if self.current_col > 0:
            self.current_col -= 1
            self.cells[self.current_row][self.current_col].config(text="")

    # Checks the guess against the target word and updates the GUI.
    def check_guess(self, event=None):
        if self.game_over or self.current_col < self.word_length:
            return

        guess = "".join(cell["text"].lower() for cell in self.cells[self.current_row])

        if guess not in self.word_list:
            messagebox.showwarning("Error", "Word not found in dictionary.")
            return
        
        # Check letters and update colors
        for i in range(self.word_length):

            # Correct letter and location
            if guess[i] == self.target_word[i]:
                self.cells[self.current_row][i].config(bg=CORRECT_COLOR, fg="white")

            # Correct letter and wrong location
            elif guess[i] in self.target_word:
                self.cells[self.current_row][i].config(bg=PRESENT_COLOR, fg="white")

            # Letter not in word
            else:
                self.cells[self.current_row][i].config(bg=ABSENT_COLOR, fg="white")
            

        # Check for win condition
        if guess == self.target_word:
            self.game_over = True
            time_taken = int(time.time() - self.time_start)
            messagebox.showinfo("Congratulations!", f"You've guessed the word in {time_taken} seconds!")
            Winner_time = open(r"winners.txt", mode ="a")
            Winner_time.write(f"User: {time_taken} seconds\n")
            Winner_time.close()
            self.play_again()
            return
        
        self.current_row += 1
        self.current_col = 0

        # Check if the user has run out of guesses
        if self.current_row >= MaxGuesses:
            self.game_over = True
            time_taken = int(time.time() - self.time_start)
            messagebox.showinfo("Game Over", f"The correct word was: {self.target_word}")
            loser_time = open(r"Losers.txt", mode="a")
            loser_time.write(f"User: {time_taken} seconds\n")
            loser_time.close()
            self .play_again()


    # Asks the user if they want to play again
    def play_again(self):
        if messagebox.askyesno("Game Over", "Do you want to play again?"):
            self.window.destroy()
            main()
        else:
            self.window.destroy()

    def run(self, event=None):
        self.window.mainloop()

# Selected length is used to open, read and close dictionary to a variable
# Selected dict then makes a random word to a variable
def select_random_word(Wordset, length=None):
    if length is None:
        return random.choice(Wordset)

    if length == 4:
        dict4 = open(r"dictionary4.txt", mode="r")
        FourLetterWords = [word.strip().lower() for word in dict4.readlines()]
        dict4.close()
        return random.choice(FourLetterWords)
    
    elif length == 5:
        dict5 = open(r"dictionary5.txt", mode="r")
        FiveLetterWords = [word.strip().lower() for word in dict5.readlines()]
        dict5.close()
        return random.choice(FiveLetterWords)
    
    elif length == 6:
        dict6 = open(r"dictionary6.txt", mode="r")
        SixLetterWords = [word.strip().lower() for word in dict6.readlines()]
        dict6.close()
        return random.choice(SixLetterWords)

# Function to handle the main game loop
def main():
    Selector = WordLengthSelector()
    word_length = Selector.get_selection()
    
    if word_length:
        print("<| Welcome to Wordle |>")
        print(f"\nYou have 6 attempts to guess the {word_length}-letter word.\n")

        game = WordleGUI(word_length)

        # Debug answer
        print(game.target_word)
        game.run()

if __name__ == "__main__":
    main()