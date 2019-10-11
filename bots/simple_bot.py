"""
This example bot implementation uses the simple_eval measure of a Board.

which is the difference between the wieghted value of all the pieces on each

side
"""

from base_chess_bot import BaseChessBot
from alpha_beta_minimax import minimax
import chess

CHESS_PIECES = [chess.PAWN,
                chess.KNIGHT,
                chess.BISHOP,
                chess.ROOK,
                chess.QUEEN]


def eval_side(board, color):
    """
    Evaluate board for a player position.

    @param chess.Board board
    @param bool color
        0 - black
        1 - white
    @rtype int
    """
    pieces = [len(board.pieces(piece, color))*piece for piece in CHESS_PIECES]

    return sum(pieces)


class SimpleBot(BaseChessBot):
    """Simple bot class inherits from BaseChessBot interface."""

    def __init__(self, name, color):
        """
        Initilize SimpleBot.

        @param str name
        @param bool color
            - black: 0
            - white: 1
        """
        super().__init__()

        self.name = name
        self.color = color

    def get_name(self):
        """Return name of bot."""
        return self.name

    def simple_eval(self, board):
        """
        Return evaluation for chess board.

        @param chess.Board board
        """
        if board.is_checkmate():
            return 1e+10

        val = eval_side(board, 1) - eval_side(board, 0)
        return val if self.color == 1 else -1*val

    def play_move(self, board):
        """Push move onto the board."""
        _, move = minimax(board, 3, self.simple_eval, -1e+10, 1e+10, 1)
        board.push(move)
