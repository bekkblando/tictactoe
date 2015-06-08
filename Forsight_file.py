import numpy
import random
import sys


class Forsight:
    team = 'X'
    enemy_team = 'O'
    board = [['O', '_', 'X'],
             ['_', '_', '_'],
             ['_', '_', '_']]

    def debug_print(self, whattoprint, information):
        print("DEBUG: ", whattoprint, information, file=sys.stderr)

    def forsight(self, test_board, team, enemy_team):
        pass

    def generate_attack(self, test_board, team, enemy_team):
        pass

    def generate_defense(self, board, team, enemy_team):
        pass

    def check_possible_moves(self, board, team, enemy_team):
        self.left = list(self.get_diags(board)[0])
        self.right = list(self.get_diags(board)[1])
        self.row0 = self.get_row(self.board, 0)
        self.row1 = self.get_row(self.board, 1)
        self.row2 = self.get_row(self.board, 2)
        self.col0 = self.get_col(self.board, 0)
        # self.debug_print("Col0", self.col0)
        self.col1 = self.get_col(board, 1)
        self.debug_print("Col1", self.col1)
        self.col2 = self.get_col(board, 2)
        self.debug_print("Col2", self.col2)
        self.moves = []
        for self.num in range(self.right.count('_')):
            self.moves.append(self.find_diag_spot(self.right, "right"))
            # self.debug_print("Possible Moves Right ", self.moves)
        for self.num in range(self.left.count('_')):
            self.moves.append(self.find_diag_spot(self.left, "left"))
            # self.debug_print("Possible Moves Left ", self.moves)
        for self.num in range(self.row0.count('_')):
            self.moves.append(self.find_row_spot(self.row0, 0))
            # self.debug_print("Possible Moves Row0 ", self.moves)
        for self.num in range(self.row1.count('_')):
            self.moves.append(self.find_row_spot(self.row1, 1))
            # self.debug_print("Possible Moves Row1 ", self.moves)
        for self.num in range(self.row2.count('_')):
            self.moves.append(self.find_row_spot(self.row2, 2))
            # self.debug_print("Possible Moves row2 ", self.moves)
        for self.num in range(self.col0.count('_')):
            self.moves.append(self.find_col_spot(self.col0, 0))
            # self.debug_print("Possible Moves Col0 ", self.moves)
        for self.num in range(self.col1.count('_')):
            self.moves.append(self.find_col_spot(self.col1, 1))
            # self.debug_print("Possible Moves Col1 ", self.moves)
        for self.num in range(self.col2.count('_')):
            self.moves.append(self.find_col_spot(self.col2, 2))
            # self.debug_print("Possible Moves ", self.moves)
        # self.debug_print("Possible Moves ", self.moves)
        return self.moves
        # self.check_forced_moves_agro(board, team, enemy_team, self.moves)

    def __init__(self, board):
        self.board = board

    def check_forced_moves_agro(self, board, team, enemy_team):
        self.debug_print("Test Board", board)
        moves = self.check_possible_moves(board, team, enemy_team)
        next_move = []
        for item in moves:

            self.debug_print("Start ", board)
            # self.board = self.hold_org_board()
            self.debug_print(self.board, board)

            self.board[item[1]][item[0]] = team
            self.debug_print("Test Board", self.board)
            self.cord = self.check_for_team_win(self.board, self.team)
            self.debug_print("Next Cord", self.cord)
            self.debug_print("Test Board with Cord", self.board)
            if self.cord is not None:
                next_move.append(self.cord)
                self.new_cord = self.check_for_enemy_win(
                    self.board, team, enemy_team)
                self.debug_print("Block Cord", self.new_cord)
                try:
                    self.board[self.new_cord[1]][self.new_cord[0]] = enemy_team
                    self.debug_print("Blocked Board", self.board)
                except:
                    return "cant"
                # if self.check_for_enemy_win(board, team, enemy_team) != None:
                new_moves = self.check_possible_moves(board, team, enemy_team)
                self.debug_print("New Moves", new_moves)
                for items in new_moves:
                    self.test_board = self.board
                    self.debug_print("Org Board", self.board)
                    self.board[items[1]][items[0]] = team
                    self.test_board = self.board
                    self.debug_print("Test Board", self.test_board)
                    try:
                        self.newest_cord = self.check_for_enemy_win(
                                self.test_board, team, enemy_team)
                        self.debug_print("New Cord", item)
                        self.debug_print("Block 1 Move Later", self.newest_cord)
                        self.test_board[self.newest_cord[1]][self.newest_cord[0]] = enemy_team
                        self.debug_print("Blocked Board 1 Move Later", self.test_board)
                    except:
                        self.debug_print("No need to ","Block")
                    if not self.check_for_team_win(self.test_board, team):
                        self.debug_print("Winning Move", items)
                        return items
        return "cant"
    def check_forced_moves_defense(self, board, team, enemy_team):
        pass

    def check_for_team_win(self, board, team):
        self.debug_print("Check for Team Win ", "Ran")
        self.left = list(self.get_diags(board)[0])
        self.right = list(self.get_diags(board)[1])
        self.row0 = self.get_row(board, 0)
        self.row1 = self.get_row(board, 1)
        self.row2 = self.get_row(board, 2)
        self.col0 = self.get_col(board, 0)
        self.debug_print("Col0", self.col0)
        self.col1 = self.get_col(board, 1)
        self.debug_print("Col1", self.col1)
        self.col2 = self.get_col(board, 2)
        self.debug_print("Col2", self.col2)
        if self.left.count(team) == 2:
            if self.check_empty(self.left):
                self.debug_print("Left Win Possible", self.left.count(team))
                return self.execute_diag_win(board, team, "left")
        if self.right.count(team) == 2:
            if self.check_empty(self.right):
                return self.execute_diag_win(board, team, "right")
        if self.row0.count(team) == 2:
            if self.check_empty(self.row0):
                return self.execute_row_win(board, team, 0)
        if self.row1.count(team) == 2:
            if self.check_empty(self.row1):
                return self.execute_row_win(board, team, 1)
        if self.row2.count(team) == 2:
            if self.check_empty(self.row2):
                return self.execute_row_win(board, team, 2)
        if self.col0.count(team) == 2:
            self.debug_print("win check", "col0")
            if self.check_empty(self.col0):
                return self.execute_col_win(board, team, 0)
        if self.col1.count(team) == 2:
            self.debug_print("win check", "col1")
            if self.check_empty(self.col1):
                return self.execute_col_win(board, team, 1)
        if self.col2.count(team) == 2:
            self.debug_print("win check", "col2")
            if self.check_empty(self.col2):
                return self.execute_col_win(board, team, 2)
        else:
            return False

    def check_for_enemy_win(self, board, enemy_team, team):
        self.debug_print("Check for Enemy Team Win", "Ran")
        self.debug_print("Enemy", enemy_team)
        self.debug_print("team", team)
        self.left = list(self.get_diags(board)[0])
        self.right = list(self.get_diags(board)[1])
        self.row0 = self.get_row(board, 0)
        self.row1 = self.get_row(board, 1)
        self.row2 = self.get_row(board, 2)
        self.col0 = self.get_col(board, 0)
        self.debug_print("Col0 b", self.col0)
        self.col1 = self.get_col(board, 1)
        self.debug_print("Col1 b", self.col1)
        self.col2 = self.get_col(board, 2)
        self.debug_print("Col2 b", self.col2)
        if self.left.count(enemy_team) == 2:
            if self.check_empty(self.left):
                self.debug_print("block", "Left diag")
                return self.execute_diag_block(board, enemy_team, "left")
        if self.right.count(enemy_team) == 2:
            if self.check_empty(self.right):
                self.debug_print("block", "right diag")
                return self.execute_diag_block(board, enemy_team, "right")
        if self.row0.count(enemy_team) == 2:
            if self.check_empty(self.row0):
                self.debug_print("block", "row0")
                return self.execute_row_block(board, enemy_team, 0)
        if self.row1.count(enemy_team) == 2:
            if self.check_empty(self.row1):
                self.debug_print("block", "row1")
                return self.execute_row_block(board, enemy_team, 1)
        if self.row2.count(enemy_team) == 2:
            if self.check_empty(self.row2):
                self.debug_print("block", "row2")
                return self.execute_row_block(board, enemy_team, 2)
        if self.col0.count(enemy_team) == 2:
            self.debug_print("block check", "col2")
            if self.check_empty(self.col0):
                self.debug_print("block", "col0")
                return self.execute_col_block(board, enemy_team, 0)
        if self.col1.count(enemy_team) == 2:
            self.debug_print("block check", "col2")
            if self.check_empty(self.col1):
                self.debug_print("block", "col1")
                return self.execute_col_block(board, enemy_team, 1)
        if self.col2.count(enemy_team) == 2:
            self.debug_print("block check", "col2")
            if self.check_empty(self.col2):
                self.debug_print("block", "col2")
                return self.execute_col_block(board, enemy_team, 2)

    def execute_diag_win(self, board, team, side):
        self.debug_print("Execute diagonal", "Win")
        if side == "left":
            self.debug_print("Left", "Win")
            return self.find_diag_spot(self.get_diags(board)[0], "left")
        if side == "right":
            self.debug_print("Right", "Win")
            return self.find_diag_spot(self.get_diags(board)[1], "right")

    def execute_row_win(self, board, team, row_num):
            return self.find_row_spot(self.get_row(board, row_num), row_num)

    def execute_col_win(self, board, team, col_num):
            return self.find_col_spot(self.get_col(board, col_num), col_num)

    def execute_row_block(self, board, team, row_num):
            return self.find_row_spot(self.get_row(board, row_num), row_num)

    def execute_col_block(self, board, team, col_num):
            return self.find_col_spot(self.get_col(board, col_num), col_num)

    def execute_diag_block(self, board, team, side):
        if side == "left":
            return self.find_diag_spot(self.get_diags(board)[0], "left")
        if side == "right":
            return self.find_diag_spot(self.get_diags(board)[1], "right")

    def find_row_spot(self, list, row_num):
        for spot_number, spot in enumerate(list):
            if spot == '_':
                return (spot_number, row_num)

    def find_col_spot(self, list, col_num):
        for spot_number, spot in enumerate(list):
            if spot == '_':
                return(col_num, spot_number)

    def find_diag_spot(self, list, side):
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

    def get_col(self, board, which):
        self.answer = []
        self.init_list = [0 for x in range(len(board))]
        for n, num in enumerate(board):
            for number, value in enumerate(num):
                self.init_list[n] = num[which]
        return self.init_list

    def get_row(self, board, which):
        return board[which]

    def get_diags(self, board):
        self.diagonal = numpy.diagonal(board)
        self.new_diagonal = numpy.diagonal(board[::-1])
        return (self.diagonal, self.new_diagonal)

    def check_empty(self, vector):
        if vector.count('_') == 0:
            return False
        if vector.count('_') > 0:
            return True
