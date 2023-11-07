import copy, random

def Make_Move(ai_board_state):
    move_to_make = []
    possible_moves = Count_Empty_Spaces(ai_board_state)
    if not (possible_moves):
        return ()

    if (ai_board_state[1][1] == 0): #Center is open, go there
        move_to_make =  (1, 1)

    if len(possible_moves) == 2:
        for check_win in possible_moves:
            test_board = copy.deepcopy(ai_board_state)
            test_board[check_win[0]][check_win[1]] = 'O'
            simulatedgame_state = check_for_winner(test_board)
            if (simulatedgame_state[0] == True): #AI can win this move, go there
                move_to_make = check_win
                break
            else:
                test_board[check_win[0]][check_win[1]] = 'X'
                simulatedgame_state = check_for_winner(test_board)
                if (simulatedgame_state[0] == True): #Player will win next move, block there
                    move_to_make = check_win
                    break

    if not (move_to_make):
        moves_and_scores = []
        best_score = -10001
        for check_win in possible_moves:
            test_board = copy.deepcopy(ai_board_state)
            test_board[check_win[0]][check_win[1]] = 'O'
            score = -minimax(test_board, 10, 2, 1)
            if (score > best_score):
                best_score = score
            moves_and_scores.append([check_win,score])

        move_choices = []
        index = 0
        for move in moves_and_scores:
            if (move[1] == best_score):
                move_choices.append(index)
            index += 1

        move_to_make = moves_and_scores[random.choice(move_choices)][0]

    return move_to_make

def minimax(board_state, depth, player, moves_taken):
    simulatedgame_state = check_for_winner(board_state)
    possible_moves = Count_Empty_Spaces(board_state)
    if (depth == 0 or simulatedgame_state[0] == True or not possible_moves):
        if not (possible_moves):
            return 0
        return (10 if player == 1 else -10) / moves_taken

    if (player == 2):
        value = -10000
        for possible_move in possible_moves:
            test_board = copy.deepcopy(board_state)
            test_board[possible_move[0]][possible_move[1]] = 'X'
            eval = minimax(test_board, depth - 1, 1, moves_taken + 1)
            value = max([value, eval])
        return value
    else:
        value = 10000
        for possible_move in possible_moves:
            test_board = copy.deepcopy(board_state)
            test_board[possible_move[0]][possible_move[1]] = 'O'
            eval = minimax(test_board, depth - 1, 2, moves_taken + 1)
            value = min([value, eval])
        return value

def Count_Empty_Spaces(board_state):
    possible_moves = []
    row_idx = 0
    for row in board_state:
        col_idx = 0
        for col in row:
            if (col == 0):
                possible_moves.append((row_idx,col_idx))
            col_idx += 1
        row_idx += 1
    return possible_moves

def check_for_winner(board_state):
    diag = [[],[]]
    iter = 0
    for row in board_state:
        diag[0].append(row[0 + iter])
        diag[1].append(row[2 - iter])
        if (isOver(row) == True):
            return [True, row[0]]

        check_col = []
        for row_num in range(0,3):
            check_col.append(board_state[row_num][iter])
        if (isOver(check_col) == True):
            return [True, check_col[0]]
        iter += 1

    for diag_check in diag:
        if (isOver(diag_check) == True):
            return [True, diag_check[0]]

    return [False, ""]

def isOver(row_data):
    if (row_data == [0, 0, 0]):
        return -1
    return all(x == row_data[0] for x in row_data)