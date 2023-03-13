import itertools
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

    def choose_valid_dice_combination(self, bet):
        rolls = range(1, Player.TOTAL_DICE_COUNT + 1)
        combinations = list(itertools.product(rolls, repeat=2))
        valid_combinations = []
        for combination in combinations:
            if self.check_bet_is_valid(combination[0], combination[1], bet):
                valid_combinations.append(combination)

        return valid_combinations

    @staticmethod
    def check_bet_is_valid(new_bet_dice_count, new_bet_dice_value, bet):
        if not (1 <= new_bet_dice_count <= Player.TOTAL_DICE_COUNT) or not (1 <= new_bet_dice_value <= 6):
            return False

        if not ((new_bet_dice_count >= bet['dice_count'])
                and ((new_bet_dice_value > bet['dice_value']) or (new_bet_dice_count > bet['dice_count']))):
            return False

        return True

    @abstractmethod
    def make_decision(self):
        pass

    @abstractmethod
    def make_bet(self, bet):
        pass
