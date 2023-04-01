# Liar's Dice
Python implementation of Liar's Dice game.


### Rules of the Game

The game is played by two or more players. Five dice are used per player with dice cups used for concealment. 
The game is round-based. Each round, each player rolls a “hand” of dice under their cup and looks at their hand while 
keeping it concealed from the other players. The first player begins his turn by bidding. A bid consists of announcing 
any face value and a number of dice. This bid is the player’s claim as to how many dice with that particular value there 
are on the whole table. Turns rotate among the players in a clockwise order.

Each player has two choices during their turn:
 - to make a higher bid; 
 - to challenge the previous bid, by calling the last bidder 'liar'. 

Raising the bid means that the player may bid a higher quantity of the same face, or any particular quantity of a higher
face. If the current player challenges the previous bid, all dice are revealed. If the bid is valid (there are at least
as many of the face value as were bid), the bidder wins. Otherwise, the challenger wins. The player who loses a round 
loses one of their dice. The loser of the last round starts the 
bidding on the next round. If the loser of the last round was eliminated, the next player starts the new round.

Additional rule for advanced players: The 'ones' face of the dice is considered wild – it always counts as the face 
of the current bid.


### How to win Liar's Dice

The winner of the game is the last player who have any dice remaining.


### Built With

 - Python 3.11
 - Pycharm


### Live Demo

Play with the code and game at: https://replit.com/@mpopova/LiarsDiceGame?fbclid=IwAR2oErqs-nK1BdT8oRrk0m-_yKxdzREjsTmgmms6GewGILkIgNQPzEMbF60

### TODO

Building a GUI Liar's Game with Tkinter.


