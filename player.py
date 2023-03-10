from abc import ABC, abstractmethod
from random import randint


class Player(ABC):
    TOTAL_DICE_COUNT = 0

    def __init__(self, name):
        self.name = name
        self.num_of_dice = 5
        self.player_dice = []
        self.roll_dice()
        self.total_dice = Player.TOTAL_DICE_COUNT

    def roll_dice(self):
        player_roll = []
        for _ in range(self.num_of_dice):
            roll = randint(1, 6)
            player_roll.append(roll)
        self.player_dice = player_roll
        return self.player_dice

    def count_total_dice(self):
        result = Player.TOTAL_DICE_COUNT
        Player.TOTAL_DICE_COUNT += self.num_of_dice
        return result

    def remove_die(self):
        if len(self.player_dice) > 0:
            self.player_dice.pop()
            self.num_of_dice -= 1
            Player.TOTAL_DICE_COUNT -= 1






