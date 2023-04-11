from helpers import clean_screen
from tkinter import Button, Entry
from canvas import root, frame


def activate_wild():
    clean_screen()
    wild_button = Button(
        root,
        text="Start Game",
        bg="green",
        fg="white",
        width=16,
        height=2,
        # command=start_game
    )
    frame.create_text(350, 230, text='Additional rule for advanced players: ', font=("Comic Sans MS", 10))
    frame.create_text(350, 250, text='The "ones" face of the dice is considered wild - ', font=("Comic Sans MS", 10))
    frame.create_text(350, 270, text='it always counts as the face of the current bid.', font=("Comic Sans MS", 10))

    frame.create_window(350, 290, window=wild_ones_box)
    frame.create_window(350, 330, window=wild_button)


wild_ones_box = Entry(root)

# def start_game():
#     game.add_players()
