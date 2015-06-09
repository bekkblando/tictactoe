import sys
import numpy
import random
import Forsight_file
from Forsight_file import Forsight

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
# test_board = board
see = Forsight(board)
# print out the inputs you're getting
debug_print("Your Team is ", team)
debug_print("Your First row ", first_row)
debug_print("Your Second row ", second_row)
debug_print("Your third row ", third_row)
debug_print("Your board ", board)
# Outputting the coordinates of your board"""


# Forsight
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
    counter = 0
    for item in board:
        if item.count(team) != 0 or item.count(enemy_team) != 0:
            debug_print("Row", item)
            debug_print("number counted team", item.count(team))
            debug_print("number counted enemy", + item.count(enemy_team))
            go_second(board, team, enemy_team)
            return "Second"
        counter += 1
        debug_print("Check Counter ", counter)
    if counter == 3:
        go_first()
        return "First"


def early_game(board, team, enemy_team):
    random_rc = random.randint(0, 2)
    # see.hold_org_board(board)
    forsee = see.check_forced_moves_agro(board, team, enemy_team)
    debug_print("For see", forsee)
    if forsee != "cant":
        place_move(forsee)
    if board[1][1] == '_':
        debug_print("Center", "Ran")
        print('1 1')
        exit()
    if check_empty(list(get_diags(board)[0])):
        debug_print("Diag", "ran")
        place_move(find_diag_spot(get_diags(board)[0], "left"))
    if check_empty(get_row(board, random_rc)):
        debug_print("Row", "Ran")
        place_move(find_row_spot(get_row(board, random_rc), random_rc))
    if check_empty(get_col(board, random_rc)):
        debug_print("col", "Ran")
        place_move(find_col_spot(get_col(board, random_rc), random_rc))
    else:
        debug_print("Place", "Empty")
        place_empty(board)

def place_empty(board):
    for number, row in enumerate(board):
        debug_print(number, row)
        if check_empty(row):
            place_move(find_row_spot(get_row(board, number), number))
def go_first():
    debug_print("Go First ", "Ran")
    print("1 1")


def go_second(board, team, enemy_team):
    debug_print("Go Second ", "Ran")
    check_for_team_win(board, team)
    check_for_enemy_win(board, enemy_team, team)


def check_for_team_win(board, team):
    debug_print("Check for Team Win ", "Ran")
    left = list(get_diags(board)[0])
    right = list(get_diags(board)[1])
    row0 = get_row(board, 0)
    row1 = get_row(board, 1)
    row2 = get_row(board, 2)
    col0 = get_col(board, 0)
    debug_print("Col0", col0)
    col1 = get_col(board, 1)
    debug_print("Col1", col1)
    col2 = get_col(board, 2)
    debug_print("Col2", col2)
    if left.count(team) == 2:
        if check_empty(left):
            debug_print("Left Win Possible", left.count(team))
            execute_diag_win(board, team, "left")
            return "diag_win"
    if right.count(team) == 2:
        if check_empty(right):
            execute_diag_win(board, team, "right")
    if row0.count(team) == 2:
        if check_empty(row0):
            execute_row_win(board, team, 0)
    if row1.count(team) == 2:
        if check_empty(row1):
            execute_row_win(board, team, 1)
    if row2.count(team) == 2:
        if check_empty(row2):
            execute_row_win(board, team, 2)
    if col0.count(team) == 2:
        debug_print("win check", "col0")
        if check_empty(col0):
            execute_col_win(board, team, 0)
    if col1.count(team) == 2:
        debug_print("win check", "col1")
        if check_empty(col1):
            execute_col_win(board, team, 1)
    if col2.count(team) == 2:
        debug_print("win check", "col2")
        if check_empty(col2):
            execute_col_win(board, team, 2)


def check_for_enemy_win(board, enemy_team, team):
    debug_print("Check for Enemy Team Win", "Ran")
    debug_print("Enemy", enemy_team)
    debug_print("team", team)
    left = list(get_diags(board)[0])
    right = list(get_diags(board)[1])
    row0 = get_row(board, 0)
    row1 = get_row(board, 1)
    row2 = get_row(board, 2)
    col0 = get_col(board, 0)
    debug_print("Col0 b", col0)
    col1 = get_col(board, 1)
    debug_print("Col1 b", col1)
    col2 = get_col(board, 2)
    debug_print("Col2 b", col2)
    if left.count(enemy_team) == 2:
        if check_empty(left):
            debug_print("block", "Left diag")
            execute_diag_block(board, enemy_team, "left")
            return("Left")
    if right.count(enemy_team) == 2:
        if check_empty(right):
            debug_print("block", "right diag")
            execute_diag_block(board, enemy_team, "right")
            return("Right")
    if row0.count(enemy_team) == 2:
        if check_empty(row0):
            debug_print("block", "row0")
            execute_row_block(board, enemy_team, 0)
            return("row0")
    if row1.count(enemy_team) == 2:
        if check_empty(row1):
            debug_print("block", "row1")
            execute_row_block(board, enemy_team, 1)
            return("row1")
    if row2.count(enemy_team) == 2:
        if check_empty(row2):
            debug_print("block", "row2")
            execute_row_block(board, enemy_team, 2)
            return("row2")
    if col0.count(enemy_team) == 2:
        debug_print("block check", "col2")
        if check_empty(col0):
            debug_print("block", "col0")
            execute_col_block(board, enemy_team, 0)
            return("Col0")
    if col1.count(enemy_team) == 2:
        debug_print("block check", "col2")
        if check_empty(col1):
            debug_print("block", "col1")
            execute_col_block(board, enemy_team, 1)
            return("Col1")
    if col2.count(enemy_team) == 2:
        debug_print("block check", "col2")
        if check_empty(col2):
            debug_print("block", "col2")
            execute_col_block(board, enemy_team, 2)
            return("Col2")
    debug_print("Early", "Game")
    early_game(board, team, enemy_team)
    debug_print("Made", "It")


def execute_diag_win(board, team, side):
    debug_print("Execute diagonal", "Win")
    if side == "left":
        debug_print("Left", "Win")
        place_move(find_diag_spot(get_diags(board)[0], "left"))
    if side == "right":
        debug_print("Right", "Win")
        place_move(find_diag_spot(get_diags(board)[1], "right"))


def execute_row_win(board, team, row_num):
    place_move(find_row_spot(get_row(board, row_num), row_num))


def execute_col_win(board, team, col_num):
    place_move(find_col_spot(get_col(board, col_num), col_num))


def execute_row_block(board, team, row_num):
    place_move(find_row_spot(get_row(board, row_num), row_num))


def execute_col_block(board, team, col_num):
    place_move(find_col_spot(get_col(board, col_num), col_num))


def execute_diag_block(board, team, side):
    if side == "left":
        place_move(find_diag_spot(get_diags(board)[0], "left"))
    if side == "right":
        place_move(find_diag_spot(get_diags(board)[1], "right"))


def check_empty(vector):
    if vector.count('_') == 0:
        return False
    if vector.count('_') > 0:
        return True


def place_move(cords):
    debug_print("Cords", cords)
    debug_print("X Cords", type(cords[0]))
    debug_print("Y Cords", type(cords[1]))
    debug_print(cords[0], cords[1])
    x_cord = cords[0]
    y_cord = cords[1]
    print('{} {}'.format(cords[1], cords[0]))
    exit()


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
                    return(0, 2)
                if spot_number == 2:
                    return(2, 0)

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
