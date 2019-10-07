def minimax(board, depth, eval, alpha, beta, maximizing_player):
    '''
    @param chess.Board board
    @param int depth
    @param function eval #function to evaluate the board position
    @param boot maximizing_player
    @rtype: chess.Move
    '''
    if depth == 0 or board.is_game_over():
        return eval(board), None

    legal_moves = list(board.legal_moves)


    if maximizing_player:
        max_eval = -1e+10
        best_move = ''
        for move in legal_moves:
            board.push(move)
            value, _ = minimax(board, depth-1, eval, alpha, beta, 0)

            if max_eval < value:
                max_eval = value
                best_move = move

            alpha = max(max_eval, alpha)
            board.pop()
            if beta <= alpha:
                break
        return max_eval, best_move

    else:
        min_eval = 1e+10
        worst_move = ''
        for move in legal_moves:
            board.push(move)
            value, _ = minimax(board, depth-1, eval, alpha, beta, 1)

            if min_eval > value:
                min_eval = value
                worst_move = move

            beta = min(min_eval, beta)
            board.pop()
            if beta <= alpha:
                break
        return min_eval, worst_move
