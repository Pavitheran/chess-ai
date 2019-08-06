from bots.random_bot import RandomBot

import chess

"""
Method consumes two ChessBot implementations and returns 
"BLACK" if black wins and "WHITE" if white wins.
"""
def run_game(white, black):
	board = chess.Board()
	turn = 0
	# Board.is_game_over() checks for stalemates, 
	# insufficient material and repetition.
	while not board.is_checkmate() and not board.is_game_over():
		# White plays on even turns and black plays on odd turns.
		# TODO: validate bot's moves are legal, game loss if not.
		if turn % 2 == 0:
			white.play_move(board)
		else:
			black.play_move(board)
		turn += 1
	else:
		print(board)
		# When loop terminates by loop condition, 
		# the previous player who moved wins.
		if board.is_checkmate():
			if turn % 2 == 0:
				return "BLACK ({})".format(black.get_name())
			else:
				return "WHITE ({})".format(white.get_name())
		else:
			return "DRAW"


if __name__ == '__main__':
	print("Starting chess match between two bots")
	# Replace below RandomBot instantiations with custom Bot implementations
	white = RandomBot("Random Bot 1")
	black = RandomBot("Random Bot 2")
	winner = run_game(white, black)
	print("RESULT: " + winner)