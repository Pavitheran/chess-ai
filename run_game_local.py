from bots.random_bot import RandomBot
from bots.simple_bot import SimpleBot
import chess
import chess.svg
import click

"""
Method consumes two ChessBot implementations and returns
"BLACK" if black wins and "WHITE" if white wins. Along with the
representation of the bord in standard chess notation.
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
		# When loop terminates by loop condition,
		# the previous player who moved wins.
		if board.is_checkmate():
			if turn % 2 == 0:
				return "BLACK ({})".format(black.get_name()), board
			else:
				return "WHITE ({})".format(white.get_name()), board
		else:
			return "DRAW", board
@click.command()
@click.option("--svg_board", default=1,
			  help="0 if you want to print the board in the terminal, 1 if you want an svg render")
def main(svg_board):
	print("Starting chess match between two bots")
	# Replace below RandomBot instantiations with custom Bot implementations
	white = SimpleBot("Simple Bot",1)
	black = RandomBot("Random Bot")
	winner, board = run_game(white, black)
	#Using chess libray graphics interface to render board
	if svg_board:
		chess.svg.board(board=board)
	else:
		print(board)

	print("RESULT: " + winner)

if __name__ == '__main__':
	main()
