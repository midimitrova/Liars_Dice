from player import Player


class ComputerPlayer(Player):
    computer_name_list = 'Sophia, Ethan, Ava, Jackson, Isabella, Liam, Emma, Noah, Olivia, Lucas'.split(', ')

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def get_player_name(name_list):
        players_names = []
        for new_player in name_list:
            players_names.append(new_player.name)
        return players_names




