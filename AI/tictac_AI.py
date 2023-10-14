import tictactoe as t3
import copy

def Make_Move(ai_board_state):
    move_to_make = []
    if (ai_board_state[1][1] == 0): #Center is open, go there
        move_to_make =  (1, 1)

    possible_moves = Count_Empty_Spaces(ai_board_state)
    for check_win in possible_moves:
        test_board = copy.deepcopy(ai_board_state)
        test_board[check_win[0]][check_win[1]] = 'O'
        simulatedgame_state = t3.check_win(test_board)
        if (simulatedgame_state[0] == True): #AI can win this move, go there
            move_to_make = check_win
            break
        else:
            test_board[check_win[0]][check_win[1]] = 'X'
            simulatedgame_state = t3.check_win(test_board)
            if (simulatedgame_state[0] == True): #Player will win next move, block there
                move_to_make = check_win
                break

    if not (move_to_make):
        best_move = [(),-10000]
        for check_win in possible_moves:
            test_board = copy.deepcopy(ai_board_state)
            test_board[check_win[0]][check_win[1]] = 'O'
            score = minimax(test_board, 4, 1, 0)
            if (score > best_move[1]):
                best_move = [check_win,score]
        move_to_make = best_move[0]

    return move_to_make

def minimax(board_state, depth, player, moves_taken):
    simulatedgame_state = t3.check_win(board_state)
    possible_moves = Count_Empty_Spaces(board_state)
    if (depth == 0 or simulatedgame_state[0] == True):
        if not (possible_moves):
            return 0
        return (10 if player == 2 else -10) / moves_taken

    if (player == 2):
        max_eval = -10000
        for possible_move in possible_moves:
            test_board = copy.deepcopy(board_state)
            test_board[possible_move[0]][possible_move[1]] = 'O'
            eval = minimax(test_board, depth - 1, 1, moves_taken + 1)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = 10000
        for possible_move in possible_moves:
            test_board = copy.deepcopy(board_state)
            test_board[possible_move[0]][possible_move[1]] = 'X'
            eval = minimax(test_board, depth - 1, 2, moves_taken + 1)
            min_eval = max(min_eval, eval)
        return min_eval

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