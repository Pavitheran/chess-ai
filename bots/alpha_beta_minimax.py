"""
Implementation of the minimax algorithm.

Optimized with alpha-beta pruning.
"""


# pylint: disable-msg=R0913
def minimax(board, depth, eval_func, alpha, beta, maximizing_player):
    """
    Minimax Algorithm implemented to work with chess.Board object.

    @param chess.Board board
    @param int depth
    @param float alpha
    @param float beta
    @param function eval #function to evaluate the board position
    @param boot maximizing_player
    @rtype: numeric, chess.Move
    """
    if depth == 0 or board.is_game_over():
        return eval_func(board), None

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = -1e+10
        best_move = ''
        for move in legal_moves:
            board.push(move)
            value, _ = minimax(board, depth-1, eval_func, alpha, beta, 0)

            if max_eval < value:
                max_eval = value
                best_move = move

            alpha = max(value, alpha)
            board.pop()

            if beta <= alpha:
                break
        return max_eval, best_move

    min_eval = 1e+10
    worst_move = ''

    for move in legal_moves:
        board.push(move)
        value, _ = minimax(board, depth-1, eval_func, alpha, beta, 1)

        if min_eval > value:
            min_eval = value
            worst_move = move

        beta = min(value, beta)
        board.pop()

        if beta <= alpha:
            break
        return min_eval, worst_move
