from unittest import TestCase, main
from unittest.mock import patch

from game_project.computer_player import ComputerPlayer
from game_project.game import Game
from game_project.human_player import HumanPlayer


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



if __name__ == '__main__':
    main()
