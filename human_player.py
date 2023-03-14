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

    def make_decision(self):
        while True:

            user_input = input('\nWould you like to make a higher bid or calling last bidder a liar? '
                               'Choose "b" for bid or "l" for liar: ').strip().lower()

            if user_input == 'b':
                return 'bid'
            elif user_input == 'l':
                return 'liar'

    def make_bet(self, bet, player):
        new_user_bet = {'dice_count': 0, 'dice_value': 0}

        to_print_combinations = []
        print('\nYou can choose from these combinations: ')
        valid_combinations = self.choose_valid_dice_combination(bet)
        for comb in valid_combinations:
            dice_count, dice_value = comb
            to_print_combinations.append(f'{dice_count} X {dice_value}')
        print(', '.join(to_print_combinations))
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
                    print(f"{player.name}'s bid is: {new_user_bet['dice_count']} X {new_user_bet['dice_value']}")
                    return new_user_bet

