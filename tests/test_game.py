from unittest import TestCase, main
from unittest.mock import patch, call

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
        self.game.list_of_players.extend([human_player, first_computer_player, second_computer_player])
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

    def test_check_is_player_winner(self):
        human = HumanPlayer('Maria')
        computer = ComputerPlayer('Emma')
        self.game.list_of_players = [human, computer]
        self.game.current_player = human
        self.game.bet = {"dice_count": 3, "dice_value": 5}
        self.game.current_player = computer
        self.game.previous_player = human
        human.player_dice = [5, 5, 5, 2, 3]
        computer.player_dice = [2, 2, 2, 3, 4]

        self.game.check_is_player_winner()

        self.assertIn(computer, self.game.list_of_players)
        self.assertEqual(4, len(computer.player_dice))
        self.assertEqual(computer, self.game.is_loser)

    def test_collect_wild_ones_with_yes_answer(self):
        self.game.bet = {"dice_count": 3, "dice_value": 3}
        self.game.answer_wild_ones = 'yes'
        self.game.current_player = HumanPlayer('Maria')
        expected = self.game.collect_wild_ones()
        result = Player.PLAYERS_DICE_VALUES[3] + Player.PLAYERS_DICE_VALUES[1]
        self.assertEqual(result, expected)

    def test_collect_wild_ones_with_no_answer(self):
        self.game.bet = {"dice_count": 3, "dice_value": 3}
        self.game.answer_wild_ones = 'no'
        self.game.current_player = HumanPlayer('Maria')
        expected = self.game.collect_wild_ones()
        result = Player.PLAYERS_DICE_VALUES[3]
        self.assertEqual(result, expected)

    def test_count_dice_correct(self):
        human = HumanPlayer('Maria')
        self.game.list_of_players = [human]
        self.game.current_player = human
        human.player_dice = [1, 1, 2, 3, 4]
        Player.PLAYERS_DICE_VALUES = {1: 2, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0}

        self.assertEqual(2, self.game.count_dice(1))
        self.assertEqual(1, self.game.count_dice(2))
        self.assertEqual(0, self.game.count_dice(5))

    def test_remove_players_dice_correct(self):
        human = HumanPlayer('Maria')
        self.game.list_of_players = [human]
        self.game.current_player = human
        human.player_dice = [1, 1, 2, 3, 4]
        Player.PLAYERS_DICE_VALUES = {1: 2, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0}

        self.game.remove_player_dice_values()

        self.assertEqual(0, Player.PLAYERS_DICE_VALUES[2])
        self.assertNotEqual(2, Player.PLAYERS_DICE_VALUES[1])
        self.assertEqual(0, Player.PLAYERS_DICE_VALUES[4])

    def test_roll_again_players_dice(self):
        Player.PLAYERS_DICE_VALUES = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        human = HumanPlayer('Maria')
        self.game.list_of_players = [human]
        self.game.current_player = human
        rolls = human.roll_dice()
        self.assertEqual(len(rolls), human.num_of_dice)
        for roll in rolls:
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 6)

    def test_round_result(self):
        human_player = HumanPlayer('Maria')
        first_computer_player = ComputerPlayer('Emma')
        second_computer_player = ComputerPlayer('Liam')
        human_player.player_dice = [1, 2]
        first_computer_player.player_dice = []
        second_computer_player.player_dice = [4, 5]
        self.game.list_of_players = [human_player, first_computer_player, second_computer_player]
        self.game.current_player = first_computer_player
        self.game.is_loser = first_computer_player

        self.game.round_result()

        self.assertNotIn(first_computer_player, self.game.list_of_players)
        self.assertEqual(second_computer_player, self.game.current_player)
        self.assertIn(second_computer_player, self.game.list_of_players)
        self.assertEqual(2, len(self.game.list_of_players))

    def test_print_valid_combinations(self):
        human_player = HumanPlayer('Maria')
        self.game.list_of_players = [human_player]
        bet = {"dice_count": 2, "dice_value": 4}
        player = self.game.list_of_players[0]
        self.game.print_valid_combinations(bet, player)

    def test_show_human_dice_correct(self):
        human_player = HumanPlayer('Maria')
        first_computer_player = ComputerPlayer('Emma')
        second_computer_player = ComputerPlayer('Liam')
        self.game.list_of_players = [human_player, first_computer_player, second_computer_player]
        human_player.player_dice = [1, 2, 3]
        with patch("builtins.print") as mock_print:
            self.game.show_human_dice()
            mock_print.assert_called_with(f"\nYour dice are: {human_player.player_dice}\n")

    def test_start_new_round_correct(self):
        human_player = HumanPlayer('Maria')
        first_computer_player = ComputerPlayer('Emma')
        second_computer_player = ComputerPlayer('Liam')
        self.game.list_of_players = [human_player, first_computer_player, second_computer_player]
        human_player.player_dice = [1, 2, 3, 4, 5]
        self.game.bet = {"dice_count": 2, "dice_value": 3}
        self.game.start_new_round()
        self.assertEqual(self.game.bet, {"dice_count": 0, "dice_value": 0})
        self.assertNotEqual(human_player.player_dice, [1, 2, 3, 4, 5])

    @patch('builtins.exit')
    def test_get_winner_correct(self, mock_exit):
        human_player = HumanPlayer('Maria')
        self.game.list_of_players = [human_player]
        self.game.get_winner()
        mock_exit.assert_called_once()

    @patch('builtins.print')
    def test_reveal_players_hands_correct(self, mock_print):
        human_player = HumanPlayer('Maria')
        computer_player = ComputerPlayer('Emma')
        human_player.player_dice = [1, 2, 3, 4, 5]
        computer_player.player_dice = [1, 2, 3, 4, 5]
        self.game.list_of_players = [human_player, computer_player]
        self.game.reveal_hands()
        expected_output = [call("Maria's hand is: [1, 2, 3, 4, 5]"),
                           call("Emma's hand is: [1, 2, 3, 4, 5]")]
        mock_print.assert_has_calls(expected_output)


if __name__ == '__main__':
    main()
