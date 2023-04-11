from tkinter import Entry, Button
from activating import activate_wild
from canvas import root, frame
from helpers import clean_screen


def add_player():
    clean_screen()
    entry_button = Button(
        root,
        text="Start Game",
        bg="green",
        fg="white",
        width=16,
        height=2,
        command=start_game
    )

    frame.create_text(350, 230, text="Please, enter your name: ", font=("Comic Sans MS", 10))
    frame.create_window(350, 250, window=human_player_name_box)
    frame.create_text(350, 270, text="Enter a number between 1 and 10 to choose "
                                     "how many computer players to have: ", font=("Comic Sans MS", 10))
    frame.create_window(350, 290, window=number_computer_players_box)
    frame.create_window(350, 330, window=entry_button)


human_player_name_box = Entry(root)
number_computer_players_box = Entry(root)


def start_game():
    activate_wild()
