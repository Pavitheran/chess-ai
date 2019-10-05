from bots.base_chess_bot import BaseChessBot
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


def simple_eval(board): return eval_side(board, 1) - eval_side(board, 0)

class SimpleBot(BaseChessBot):

    def __init__(self, name, color):

        super().__init__()

        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def play_move(self, board):

        legal_moves = list(board.legal_moves)
        move_values = [0 for i in legal_moves]
        check_board = board
        for i,move in enumerate(legal_moves):
            check_board.push(move)
            value = simple_eval(board)
            value = value if self.color == 1 else -1*value
            move_values[i] += value
            check_board.pop()

        select_move = np.argmax(move_values)
        board.push(legal_moves[select_move])
