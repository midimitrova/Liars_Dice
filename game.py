from human_player import HumanPlayer
from computer_player import ComputerPlayer
from random import choice

from player import Player


class Game:

    def __init__(self):
        self.list_of_players = []
        self.bet = {"dice_count": 3, "dice_value": 2}

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
                if computer_players < 1 or computer_players > 10:
                    raise ValueError
                break
            except ValueError:
                print('Please enter a valid number!')

        while computer_players:
            random_computer_player = ComputerPlayer(choice(ComputerPlayer.computer_name_list))
            if random_computer_player.name not in ComputerPlayer.get_player_name(self.list_of_players):
                self.list_of_players.append(random_computer_player)
                computer_players -= 1
            else:
                continue

    def turn_on_additional_rules(self):
        result = ''
        for current_player in self.list_of_players:
            if current_player.__class__.__name__ == 'HumanPlayer':
                result = current_player.activating_wild_ones()
        return result

    # def choose_dice_combination(self):
    #     choose from dice combination if make_decision is bid, and with or no wild ones




