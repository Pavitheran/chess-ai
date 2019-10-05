import chess
import chess.pgn
import numpy as np


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
