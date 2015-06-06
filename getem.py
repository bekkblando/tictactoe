import sys
import numpy


def debug_print(whattoprint, information):
    print("DEBUG: ", whattoprint, information, file=sys.stderr)

# get your team & get your board
board = []
team = input()
first_row = input()
first_row = list(first_row)
second_row = input()
second_row = list(second_row)
third_row = input()
third_row = list(third_row)
board = [first_row, second_row, third_row]

# print out the inputs you're getting
debug_print("Your Team is ", team)
debug_print("Your First row ", first_row)
debug_print("Your Second row ", second_row)
debug_print("Your third row ", third_row)
debug_print("Your board ", board)
# Outputting the coordinates of your board"""


def get_col(board, which):
    answer = []
    init_list = [0 for x in range(len(board))]
    for n, num in enumerate(board):
        for number, value in enumerate(num):
            init_list[n] = num[which]
    return init_list


def get_row(board, which):
    return board[which]


def get_diags(board):
    diagonal = numpy.diagonal(board)
    new_diagonal = numpy.diagonal(board[::-1])
    return (diagonal, new_diagonal)


def check_team(board, team):
    debug_print("Check Team", "Ran")
    if team == 'X':
        check_if_going(board, 'X', 'O')
    if team == 'O':
        check_if_going(board, 'O', 'X')


def check_if_going(board, team, enemy_team):
    debug_print("Check if Going", "Ran")
    for item in board:
        if item.count(team) == 0 and item.count(enemy_team) != 0:
            debug_print("Row", item)
            debug_print("number counted team", item.count(team))
            debug_print("number counted enemy", + item.count(enemy_team))
            go_second(board, team, enemy_team)
            return None
    go_first()

def early_game(board, team):
    

def go_first():
    debug_print("Go First ", "Ran")
    print(1, 1)


def go_second(board, team, enemy_team):
    debug_print("Go Second ", "Ran")
    check_for_team_win(board, team)
    check_for_enemy_win(board, enemy_team)


def check_for_team_win(board, team):
    debug_print("Check for Team Win ", "Ran")
    left = list(get_diags(board)[0])
    right = list(get_diags(board)[1])
    row0 = get_row(board, 0)
    row1 = get_row(board, 1)
    row2 = get_row(board, 2)
    col0 = get_col(board, 0)
    col1 = get_col(board, 1)
    col2 = get_col(board, 2)
    if left.count(team) == 2:
        execute_diag_win(board, team, left)
    if right.count(team) == 2:
        execute_diag_win(board, team, right)
    if row0.count(team) == 2:
        execute_row_win(board, team, 0)
    if row1.count(team) == 2:
        execute_row_win(board, team, 1)
    if row2.count(team) == 2:
        execute_row_win(board, team, 2)
    if col0.count(team) == 2:
        execute_col_win(board, team, 0)
    if col1.count(team) == 2:
        execute_col_win(board, team, 1)
    if col2.count(team) == 2:
        execute_col_win(board, team, 2)


def check_for_enemy_win(board, enemy_team):
    debug_print("Check for Enemy Team Win", "Ran")
    left = list(get_diags(board)[0])
    right = list(get_diags(board)[1])
    row0 = get_row(board, 0)
    row1 = get_row(board, 1)
    row2 = get_row(board, 2)
    col0 = get_col(board, 0)
    col1 = get_col(board, 1)
    col2 = get_col(board, 2)
    if left.count(team) == 2:
        execute_diag_block(board, enemy_team, left)
    if right.count(team) == 2:
        execute_diag_block(board, enemy_team, right)
    if row0.count(team) == 2:
        execute_row_block(board, enemy_team, 0)
    if row1.count(team) == 2:
        execute_row_block(board, enemy_team, 1)
    if row2.count(team) == 2:
        execute_row_block(board, enemy_team, 2)
    if col0.count(team) == 2:
        execute_col_block(board, enemy_team, 0)
    if col1.count(team) == 2:
        execute_col_block(board, enemy_team, 1)
    if col2.count(team) == 2:
        execute_col_block(board, enemy_team, 2)
    else:


def execute_diag_win(board, team, side):
    if side == "left":
        place_move(find_diag_spot(get_diags(board)[0]))
    if side == "right":
        place_move(find_diag_spot(get_diags(board)[1]))


def execute_row_win(board, team, row_num):
    place_move(find_row_spot(get_row(board, row), row_num))


def execute_col_win(board, team, col_num):
    place_move(find_col_spot(get_row(board, col), col_num))


def execute_row_block(board, team, row_num):
    place_move(find_row_spot(get_row(board, row), row_num))


def execute_col_block(board, team, col_num):
    place_move(find_col_spot(get_row(board, col), col_num))


def execute_diag_block(board, team, side):
    if side == "left":
        place_move(find_diag_spot(get_diags(board)[0]), "left")
    if side == "right":
        place_move(find_diag_spot(get_diags(board)[1]), "right")


def place_move(cords):
    x_cord = cords[0]
    y_cord = cords[1]
    print(str(x_card) + str(y_cord))


def find_row_spot(list, row_num):
    for spot_number, spot in enumerate(list):
        if spot == '_':
            return (spot_number, row_num)


def find_col_spot(list, col_num):
    for spot_number, spot in enumerate(list):
        if spot == '_':
            return(col_num, spot_number)


def find_diag_spot(list, side):
    if side == "right":
        for spot_number, spot in enumerate(list):
            if spot == '_':
                if spot_number == 1:
                    return(1, 1)
                if spot_number == 0:
                    return(2, 0)
                if spot_number == 2:
                    return(0, 2)

    if side == "left":
        for spot_number, spot in enumerate(list):
            if spot == '_':
                if spot_number == 1:
                    return(1, 1)
                if spot_number == 0:
                    return(0, 0)
                if spot_number == 2:
                    return(2, 2)

check_team(board, team)
