def minimax(board, depth, eval, maximizing_player):
    '''
    @param chess.Board board
    @param int depth
    @param function eval #function to evaluate the board position
    @param boot maximizing_player
    @rtype: chess.Move
    '''
    if depth == 0 or board.is_game_over():
        return eval(board)

    legal_moves = list(board.legal_moves)

    if maximizing_player:
        max_eval = -1e+10
        for move in legal_moves:
            board.push(move)
            value = minimax(board, depth-1, eval, 0)
            max_eval = max(max_eval, value)
            board.pop()
        return max_eval

    else:
        min_eval = 1e+10
        for move in legal_moves:
            board.push(move)
            value = minimax(board, depth-1, eval, 1)
            min_eval = min(min_eval, value)
            board.pop()
        return min_eval
