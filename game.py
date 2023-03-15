from player import Player
from human_player import HumanPlayer
from computer_player import ComputerPlayer
from random import choice


class Game:

    def __init__(self):
        self.list_of_players = []
        self.bet = {"dice_count": 0, "dice_value": 0}
        self.current_player = ''
        self.previous_player = ''
        self.answer_wild_ones = ''
        self.is_loser = ''

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
        print('\nAdditional rule for advanced players: '
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
            self.answer_wild_ones = result

        return result

    def choose_starting_player(self):
        if self.current_player == '':
            self.current_player = choice(self.list_of_players)
            if self.check_is_player_human(self.current_player):
                self.turn_on_additional_rules(self.current_player)
                print(f'Your dice are: {self.current_player.player_dice}')

    def choose_next_player(self):
        current_player_index = self.list_of_players.index(self.current_player)
        next_player_index = (current_player_index + 1) % len(self.list_of_players)
        next_player = self.list_of_players[next_player_index]

        self.previous_player = self.current_player
        self.current_player = next_player

    def check_is_player_winner(self):
        all_current_dice_count = self.collect_wild_ones()

        if all_current_dice_count >= self.bet['dice_count']:
            print(f"{self.current_player.name} loses a die")
            self.current_player.remove_die()
            self.is_loser = self.current_player
        else:
            print(f"{self.previous_player.name} loses a die")
            self.previous_player.remove_die()
            self.is_loser = self.previous_player

    def collect_wild_ones(self):
        face_value = self.bet['dice_value']
        collect_all_dice = self.count_dice(face_value)
        if self.answer_wild_ones == 'yes' and face_value != 1:
            collect_all_dice += Player.PLAYERS_DICE_VALUES[1]
            return collect_all_dice
        else:
            return collect_all_dice

    @staticmethod
    def count_dice(face_value):
        count = 0
        for value in Player.PLAYERS_DICE_VALUES:
            if value == face_value:
                count += Player.PLAYERS_DICE_VALUES[face_value]
        return count

    @staticmethod
    def remove_player_dice_values():
        for value in Player.PLAYERS_DICE_VALUES:
            Player.PLAYERS_DICE_VALUES[value] = 0

    def reroll_player_dice(self):
        self.remove_player_dice_values()
        if self.list_of_players:
            for player in self.list_of_players:
                player.roll_dice()

    def round_result(self):
        while len(self.current_player.player_dice) == 0:
            self.choose_next_player()

        self.current_player = self.is_loser

        for player in self.list_of_players:
            if len(player.player_dice) == 0:
                print(f"{player.name} is out of the game")
                self.choose_next_player()

        self.list_of_players = [player for player in self.list_of_players if not len(player.player_dice) == 0]

        if len(self.list_of_players) == 1:
            self.get_winner()

    def print_valid_combinations(self, bet, player):
        is_human = self.check_is_player_human(player)
        if is_human:
            to_print_combinations = []
            print('\nYou can choose from these combinations: ')
            valid_combinations = Player.choose_valid_dice_combination(bet)
            for comb in valid_combinations:
                dice_count, dice_value = comb
                to_print_combinations.append(f'{dice_count} X {dice_value}')
            print(', '.join(to_print_combinations))

    def start_new_round(self):
        print("\n\nStart new round\n")
        self.reroll_player_dice()
        self.bet = {"dice_count": 0, "dice_value": 0}
        if self.check_is_player_human(self.current_player):
            self.turn_on_additional_rules(self.current_player)
            print(f'Your dice are: {self.current_player.player_dice}')

    def get_winner(self):
        print(f"{self.list_of_players[0].name} is the winner!")
        exit()

    def reveal_hands(self):
        for player in self.list_of_players:
            print(f"{player.name}'s hand is: {player.player_dice}")

    def play_game(self):

        self.add_players()
        self.choose_starting_player()
        self.print_valid_combinations(self.bet, self.current_player)
        self.bet.update(self.current_player.make_bet(self.bet))
        print(f"{self.current_player.name}'s bid is: {self.bet['dice_count']} X {self.bet['dice_value']}")
        self.choose_next_player()

        while True:
            player_decision = self.current_player.make_decision(self.bet)

            if player_decision == "liar":
                print(f"\n{self.current_player.name} accused that {self.previous_player.name} is a liar!")
                print("Revealing all players hands: ")
                self.reveal_hands()
                self.check_is_player_winner()
                self.round_result()
                self.start_new_round()
                player_decision = "bid"
            if player_decision == "bid":
                self.print_valid_combinations(self.bet, self.current_player)
                self.bet.update(self.current_player.make_bet(self.bet))
                print(f"{self.current_player.name}'s bid is: {self.bet['dice_count']} X {self.bet['dice_value']}")
                self.choose_next_player()


if __name__ == "__main__":
    my_game = Game()
    my_game.play_game()
