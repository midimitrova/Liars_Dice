from game_project.player import Player
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

    def make_decision(self, bet):
        computer_options = ['bid', 'liar']
        computer_decision = choice(computer_options)

        if self.choose_valid_dice_combination(bet) is None:
            return 'liar'

        else:
            return 'bid' if computer_decision == "bid" else "liar"

    def make_bet(self, bet):
        valid_combinations = self.choose_valid_dice_combination(bet)
        if valid_combinations:
            computer_combinations = choice(valid_combinations)
            dice_count, dice_value = computer_combinations
            return {'dice_count': dice_count, 'dice_value': dice_value}
