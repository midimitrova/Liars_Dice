from player import Player
from random import choice


class ComputerPlayer(Player):
    computer_name_list = 'Sophia, Ethan, Ava, Jackson, Isabella, Liam, Emma, Noah, Olivia, Lucas'.split(', ')

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_player_name(name_list):
        players_names = []
        for new_player in name_list:
            players_names.append(new_player.name)
        return players_names

    def make_decision(self):
        computer_options = ['bid', 'liar']
        computer_decision = choice(computer_options)

        return 'bid' if computer_decision == "bid" else "liar"

    def make_bet(self, bet):
        pass

    def check_bet_is_valid(self, new_bet_dice_count, new_bet_dice_value, bet):
        pass
