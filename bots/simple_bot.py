from bots.base_chess_bot import BaseChessBot
from bots.alpha_beta_minimax import minimax
import chess
import random
import numpy as np
"""
This example bot implementation uses the simple_eval measure of a Board
which is the difference between the wieghted value of all the pieces on each
side
"""

CHESS_PIECES = [chess.PAWN,
                chess.KNIGHT,
                chess.BISHOP,
                chess.ROOK,
                chess.QUEEN]

def eval_side(board, color):
    '''
    @param chess.Board board
    @param bool color
        0 - black
        1 - white
    @rtype int
    '''

    pieces = [len(board.pieces(piece,color))*piece for piece in CHESS_PIECES]

    return sum(pieces)


class SimpleBot(BaseChessBot):

    def __init__(self, name, color):

        super().__init__()

        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def simple_eval(self, board):
        if board.is_checkmate():
            return 1e+10
        else:
            val = eval_side(board, 1) - eval_side(board, 0)
            return val if self.color==1 else -1*val

    def play_move(self, board):

        value, move = minimax(board, 2, self.simple_eval, -1e+10, 1e+10, 1)
        board.push(move)
