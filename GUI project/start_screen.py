from tkinter import Entry, Button

from authentication import add_player
from canvas import root, frame


def start():
    entry_button = Button(
        root,
        text="Start Game",
        bg="green",
        fg="white",
        width=16,
        height=2,
        command=start_game
    )
    frame.create_window(350, 330, window=entry_button)


frame.create_text(350, 230, text='Welcome!', font=("Comic Sans MS", 10))
frame.create_text(350, 250, text='This is Liar\'s Dice Game!', font=("Comic Sans MS", 10))
frame.create_text(350, 270, text='Let\'s play!', font=("Comic Sans MS", 10))


def start_game():
    add_player()

