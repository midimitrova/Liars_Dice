from abc import ABC, abstractmethod
from random import randint


class Player(ABC):
    TOTAL_DICE_COUNT = 0
    PLAYERS_DICE_VALUES = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

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
        if len(self.player_dice):
            self.player_dice.pop()
            self.num_of_dice -= 1
            Player.TOTAL_DICE_COUNT -= 1

    def collect_player_dice_values(self):
        for die in self.player_dice:
            Player.PLAYERS_DICE_VALUES[die] += 1

    @abstractmethod
    def make_decision(self):
        pass

    @abstractmethod
    def make_bet(self, bet):
        pass

    @abstractmethod
    def check_bet_is_valid(self, new_bet_dice_count, new_bet_dice_value, bet):
        pass
