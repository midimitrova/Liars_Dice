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
