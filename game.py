from human_player import HumanPlayer
from computer_player import ComputerPlayer
from random import choice


class Game:

    def __init__(self):
        self.list_of_players = []

    def add_players(self):
        while True:
            try:
                user_input = HumanPlayer(input("Enter your name: ").strip())
                self.list_of_players.append(user_input)
                break

            except ValueError:
                print('Your name should contain only letters!')

        while True:
            try:
                computer_players = int(input("Enter a number between 1 and 10 to choose "
                                             "how many computer players to have: "))

            except ValueError:
                print('Please enter a digit!')

            else:
                if 1 <= computer_players <= 10:
                    break
                else:
                    print("Out of range. Try again!")

        while computer_players > 0:
            random_computer_player = ComputerPlayer(choice(ComputerPlayer.computer_name_list))
            if random_computer_player.name not in ComputerPlayer.get_player_name(self.list_of_players):
                self.list_of_players.append(random_computer_player)
                computer_players -= 1
            else:
                continue


