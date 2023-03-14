from human_player import HumanPlayer
from computer_player import ComputerPlayer
from random import choice

from player import Player


class Game:

    def __init__(self):
        self.list_of_players = []
        self.bet = {"dice_count": 0, "dice_value": 0}
        self.current_player = ''
        self.previous_player = ''

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

    @staticmethod
    def activating_wild_ones():
        print('Additional rule for advanced players: '
              'The "ones" face of the dice is considered wild - it always counts as the face of the current bid.')

        while True:
            try:
                user_input = input('Do you want to activate "wild ones" mode? '
                                   'Choose "yes" or "no": ').strip().lower()

                if user_input not in ['yes', 'no']:
                    raise ValueError
                break

            except ValueError:
                print('Please enter "yes" or "no"!')

        return user_input

    @staticmethod
    def check_is_player_human(player):
        if player.__class__.__name__ == 'HumanPlayer':
            return True
        return False

    def turn_on_additional_rules(self, player):
        result = ''
        if self.check_is_player_human(player):
            result = self.activating_wild_ones()

        return result

    def choose_starting_player(self):
        if self.current_player == '':
            self.current_player = choice(self.list_of_players)
            if self.check_is_player_human(self.current_player):
                self.turn_on_additional_rules(self.current_player)

    def choose_next_player(self):
        current_player_index = self.list_of_players.index(self.current_player)
        next_player_index = (current_player_index + 1) % len(self.list_of_players)
        next_player = self.list_of_players[next_player_index]

        self.previous_player = self.current_player
        self.current_player = next_player

    def check_liar_mode(self):
        pass

    def collect_wild_ones(self):
        collect_all_dice = self.bet["dice_count"]
        if self.turn_on_additional_rules == 'yes':
            collect_all_dice += Player.PLAYERS_DICE_VALUES[1]

        return collect_all_dice
