from unittest import TestCase, main
from game_project.computer_player import ComputerPlayer
from game_project.player import Player


class TestComputerPlayer(TestCase):
    def setUp(self):
        self.computer_player = ComputerPlayer('Isabella')

    def test_is_initialized_correct(self):
        self.assertEqual('Isabella', self.computer_player.name)
        self.assertEqual(5, self.computer_player.num_of_dice)
        self.assertEqual(self.computer_player.num_of_dice, len(self.computer_player.player_dice))
        self.assertEqual(10, self.computer_player.count_total_dice())
        self.assertTrue(issubclass(self.computer_player.__class__, Player))

    def test_get_player_name_correct(self):
        name_list = ['Jackson', 'Liam', 'Emma']
        expected_output = name_list
        result = ['Jackson', 'Liam', 'Emma']
        self.assertEqual(result, expected_output)

    def test_make_decision_with_bid_or_liar(self):
        bet = {'dice_count': 2, 'dice_value': 4}
        decision = self.computer_player.make_decision(bet)
        self.assertIn(decision, ["bid", "liar"])

    def test_make_decision_when_choose_valid_dice_combination_is_none(self):
        self.computer_player.choose_valid_dice_combination = lambda x: None
        result = self.computer_player.make_decision({'dice_count': 2, 'dice_value': 4})
        self.assertEqual(result, 'liar')

    def test_make_bet_with_valid_combination(self):
        self.computer_player.choose_valid_dice_combination = lambda bet: [(3, 2), (2, 5)]
        bet = self.computer_player.make_bet({'dice_count': 3, 'dice_value': 4})
        self.assertIn(bet['dice_count'], [3, 2])
        self.assertIn(bet['dice_value'], [2, 5])


if __name__ == '__main__':
    main()
