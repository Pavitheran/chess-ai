from bots.base_chess_bot import BaseChessBot
import chess
import random

"""
This example bot implementation makes random legal moves each turn.
It is pretty bad but serves as an example of how to push moves onto the board.
Most games between two RandomBots end in a DRAW.
"""

class RandomBot(BaseChessBot):
	def __init__(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def play_move(self, board):
		legal_moves = list(board.legal_moves)
		random_move = random.choice(legal_moves)
		board.push(random_move)
