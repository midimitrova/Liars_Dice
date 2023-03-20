from unittest import TestCase, main
from unittest.mock import patch

from game_project.computer_player import ComputerPlayer
from game_project.game import Game
from game_project.human_player import HumanPlayer
from game_project.player import Player


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_is_game_initialized_correct(self):
        self.assertEqual([], self.game.list_of_players)
        self.assertEqual({"dice_count": 0, "dice_value": 0}, self.game.bet)
        self.assertEqual('', self.game.current_player)
        self.assertEqual('', self.game.previous_player)
        self.assertEqual('', self.game.answer_wild_ones)
        self.assertEqual('', self.game.is_loser)

    def test_add_human_player_correct(self):
        with patch('builtins.input', side_effect=['Maria', '1']):
            self.game.add_players()
        self.assertIsInstance(self.game.list_of_players[0], HumanPlayer)

    def test_add_computer_players_correct(self):
        with patch('builtins.input', side_effect=['John', '3']):
            self.game.add_players()
        self.assertEqual(4, len(self.game.list_of_players))
        result = [comp_player for comp_player in self.game.list_of_players if type(comp_player) == ComputerPlayer]
        self.assertEqual(3, len(result))

    @patch('builtins.input', side_effect=['123', 'John', '2'])
    def test_add_players_with_invalid_name(self, mock_input):
        self.game.add_players()
        self.assertEqual(3, len(self.game.list_of_players))

    def test_add_computer_player_with_invalid_input(self):
        with patch('builtins.input', side_effect=['John', '0', '11', '3']):
            self.game.add_players()
        self.assertEqual(4, len(self.game.list_of_players))
        result = [comp_player for comp_player in self.game.list_of_players if type(comp_player) == ComputerPlayer]
        self.assertEqual(3, len(result))

    @patch('builtins.input', side_effect=['yes'])
    def test_activating_wild_ones_with_positive_input(self, mock_input):
        result = self.game.activating_wild_ones()
        self.assertEqual('yes', result)

    @patch('builtins.input', side_effect=['no'])
    def test_activating_wild_ones_with_negative_input(self, mock_input):
        result = self.game.activating_wild_ones()
        self.assertEqual('no', result)

    def test_activating_wild_ones_with_invalid_input(self):
        with patch('builtins.input', side_effect=['hey', 'yes']):
            result = self.game.activating_wild_ones()
        self.assertEqual('yes', result)

    def test_check_is_player_human(self):
        human_player = HumanPlayer('Maria')
        computer_player = ComputerPlayer('Liam')
        result_true = self.game.check_is_player_human(human_player)
        result_false = self.game.check_is_player_human(computer_player)
        self.assertTrue(result_true)
        self.assertFalse(result_false)

    def test_turn_on_additional_rules_with_positive_answer_correct(self):
        human_player = HumanPlayer('Maria')

        with patch('builtins.input', side_effect=['yes']):
            result = self.game.turn_on_additional_rules(human_player)
        self.assertEqual(result, 'yes')

    def test_turn_on_additional_rules_with_negative_answer_correct(self):
        human_player = HumanPlayer('Maria')

        with patch('builtins.input', side_effect=['no']):
            result = self.game.turn_on_additional_rules(human_player)
        self.assertEqual(result, 'no')

    def test_choose_starting_player_correct(self):
        self.game.list_of_players = ['Maria', 'Liam', 'Emma']
        self.game.choose_starting_player()
        self.assertIn(self.game.current_player, self.game.list_of_players)
        result = self.game.check_is_player_human(self.game.current_player)
        self.assertFalse(result)

    def test_choose_next_player_correct(self):
        human_player = HumanPlayer('Maria')
        first_computer_player = ComputerPlayer('Emma')
        second_computer_player = ComputerPlayer('Liam')
        self.game.list_of_players = (human_player, first_computer_player, second_computer_player)
        self.game.current_player = human_player

        self.game.choose_next_player()
        result = self.game.current_player
        self.assertEqual(result, first_computer_player)

        self.game.choose_next_player()
        result = self.game.current_player
        self.assertEqual(result, second_computer_player)

        self.game.choose_next_player()
        result = self.game.current_player
        self.assertEqual(result, human_player)

    def test_collect_wild_ones_with_yes_answer(self):
        self.game.bet = {"dice_count": 3, "dice_value": 3}
        self.game.answer_wild_ones = 'yes'
        self.game.current_player = HumanPlayer('Maria')
        result = self.game.collect_wild_ones()
        expected = Player.PLAYERS_DICE_VALUES[3] + Player.PLAYERS_DICE_VALUES[1]
        self.assertEqual(result, expected)

    def test_collect_wild_ones_with_no_answer(self):
        self.game.bet = {"dice_count": 3, "dice_value": 3}
        self.game.answer_wild_ones = 'no'
        self.game.current_player = HumanPlayer('Maria')
        result = self.game.collect_wild_ones()
        expected = Player.PLAYERS_DICE_VALUES[3]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
