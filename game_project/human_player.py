from game_project.player import Player


class HumanPlayer(Player):

    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError('Your name should contain only letters!')

        self.__name = value.title()

    def make_decision(self, bet):
        while True:
            try:
                user_input = input('\nWould you like to make a higher bid or calling last bidder a liar? '
                                   'Choose "b" for bid or "l" for liar: ').strip().lower()

                if user_input == 'b' and self.choose_valid_dice_combination(bet) is None:
                    raise ValueError

            except ValueError:
                print("There aro no more valid combinations to choose. Please enter 'l' for liar.")
                continue

            else:
                if user_input == 'b':
                    return 'bid'
                elif user_input == 'l':
                    return 'liar'

    def make_bet(self, bet):
        new_user_bet = {'dice_count': 0, 'dice_value': 0}

        while True:
            try:
                new_user_bet['dice_count'] = int(input('Please, enter number of dice: '))
                new_user_bet['dice_value'] = int(input('Please, enter face value of dice: '))

                if not self.check_bet_is_valid(new_user_bet['dice_count'], new_user_bet['dice_value'], bet):
                    raise ValueError

            except ValueError:
                print("You should bid a higher quantity of the same face or any particular quantity of a higher face.\n"
                      f"You can't bid a number of dice larger than all dice on table: {Player.TOTAL_DICE_COUNT}, "
                      f"or a face value of die lower than 1 and higher than 6.")
                continue

            else:
                if self.check_bet_is_valid(new_user_bet['dice_count'], new_user_bet['dice_value'], bet):
                    return new_user_bet
