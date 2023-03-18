from unittest import TestCase, main
from unittest.mock import patch

from game_project.human_player import HumanPlayer
from game_project.player import Player


class TestHumanPlayer(TestCase):
    def setUp(self):
        self.human_player = HumanPlayer('Angela')

    def test_is_initialized_correct(self):
        self.assertEqual('Angela', self.human_player.name)
        self.assertEqual(5, self.human_player.num_of_dice)
        self.assertEqual(self.human_player.num_of_dice, len(self.human_player.player_dice))
        self.assertEqual(10, self.human_player.count_total_dice())
        self.assertTrue(issubclass(self.human_player.__class__, Player))

    def test_is_name_is_correctly_written(self):
        self.assertEqual('Angela', self.human_player.name)

    def test_is_name_is_not_correctly_written(self):
        with self.assertRaises(ValueError) as ve:
            self.human_player.name = 'Ange11$.'
        self.assertEqual('Your name should contain only letters!', str(ve.exception))
        # test if name is the same after thrown error
        self.assertEqual('Angela', self.human_player.name)

    @patch('builtins.input', side_effect=['b'])
    def test_make_decision_is_taken_correctly_with_bid(self, mock_input):
        bet = {'dice_count': 2, 'dice_value': 3}
        result = self.human_player.make_decision(bet)
        self.assertEqual(result, 'bid')

    @patch('builtins.input', side_effect=['l'])
    def test_make_decision_is_taken_correctly_with_liar(self, mock_input):
        bet = {'dice_count': 2, 'dice_value': 3}
        result = self.human_player.make_decision(bet)
        self.assertEqual(result, 'liar')

    @patch('builtins.input', side_effect=['b', 'l'])
    def test_are_there_more_valid_combination_to_choose_when_player_set_bid(self, mock_input):
        bet = {'dice_count': 2, 'dice_value': 3}
        self.human_player.choose_valid_dice_combination = lambda x: None
        self.assertEqual(self.human_player.make_decision(bet), 'liar')

    @patch('builtins.input', side_effect=['3', '4'])
    def test_make_bet_with_valid_bet(self, mock_input):
        bet = {'dice_count': 2, 'dice_value': 3}
        expected_result = {'dice_count': 3, 'dice_value': 4}
        result = self.human_player.make_bet(bet)
        self.assertEqual(result, expected_result)

    @patch('builtins.input')
    def test_make_bet_with_invalid_user_input(self, mock_input):
        mock_input.side_effect = ['0', '7', '3', '4']
        bet = {'dice_count': 2, 'dice_value': 3}
        result = self.human_player.make_bet(bet)
        self.assertEqual(result, {'dice_count': 3, 'dice_value': 4})

    def test_make_bet_with_invalid_and_valid_bet_for_check_bet_is_valid_method(self):
        bet = {'dice_count': 3, 'dice_value': 4}
        self.assertFalse(self.human_player.check_bet_is_valid(2, 1, bet))
        self.assertFalse(self.human_player.check_bet_is_valid(3, 2, bet))
        self.assertTrue(self.human_player.check_bet_is_valid(4, 4, bet))
        self.assertTrue(self.human_player.check_bet_is_valid(3, 5, bet))


if __name__ == '__main__':
    main()
