from player import Player


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

    def make_decision(self):
        while True:

            user_input = input('Would you like to make a higher bid or calling last bidder a liar? '
                               'Choose "b" for bid or "l" for liar: ').strip().lower()

            if user_input == 'b':
                return 'bid'
            elif user_input == 'l':
                return 'liar'

    def make_bet(self, bet):
        new_user_bet = {'dice_count': 0, 'dice_value': 0}
        print('Place your bet.')

        while True:
            try:
                new_user_bet['dice_count'] = int(input('Please, enter number of dice: '))
                new_user_bet['dice_value'] = int(input('Please, enter face value of dice: '))

            except ValueError:
                print('Please, enter a digit')
                continue

            else:
                if self.check_bet_is_valid(new_user_bet['dice_count'], new_user_bet['dice_value'], bet):
                    return new_user_bet

    def check_bet_is_valid(self, new_bet_dice_count, new_bet_dice_value, bet):
        pass
