from random import randint


class Player:

    def __init__(self, name):
        self.name = name
        self.num_of_dice = 5
        self.player_dice = []
        self.roll_dice()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise ValueError('Your name should contain only letters!')

        self.__name = value.title()

    def roll_dice(self):
        player_dice = []
        for _ in range(self.num_of_dice):
            roll = randint(1, 6)
            player_dice.append(roll)
        return player_dice
