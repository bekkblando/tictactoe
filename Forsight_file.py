import numpy
import random
import sys


class Forsight:
    team = 'X'
    enemy_team = 'O'
    board = [['_', '_', 'X'],
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
        self.debug_print("Col0", self.col0)
        self.col1 = self.get_col(board, 1)
        self.debug_print("Col1", self.col1)
        self.col2 = self.get_col(board, 2)
        self.debug_print("Col2", self.col2)
        self.moves = []
        for self.num in range(self.right.count('_')):
            self.moves.append(self.find_diag_spot(self.right, "right"))
            self.debug_print("Possible Moves Right ", self.moves)
        for self.num in range(self.left.count('_')):
            self.moves.append(self.find_diag_spot(self.left, "left"))
            self.debug_print("Possible Moves Left ", self.moves)
        for self.num in range(self.row0.count('_')):
            self.moves.append(self.find_row_spot(self.row0, 0))
            self.debug_print("Possible Moves Row0 ", self.moves)
        for self.num in range(self.row1.count('_')):
            self.moves.append(self.find_row_spot(self.row1, 1))
            self.debug_print("Possible Moves Row1 ", self.moves)
        for self.num in range(self.row2.count('_')):
            self.moves.append(self.find_row_spot(self.row2, 2))
            self.debug_print("Possible Moves row2 ", self.moves)
        for self.num in range(self.col0.count('_')):
            self.moves.append(self.find_col_spot(self.col0, 0))
            self.debug_print("Possible Moves Col0 ", self.moves)
        for self.num in range(self.col1.count('_')):
            self.moves.append(self.find_col_spot(self.col1, 1))
            self.debug_print("Possible Moves Col1 ", self.moves)
        for self.num in range(self.col2.count('_')):
            self.moves.append(self.find_col_spot(self.col2, 2))
            self.debug_print("Possible Moves ", self.moves)
        self.moves = filter(None, self.moves)
        self.debug_print("Possible Moves ", self.moves)
        self.check_forced_moves_agro(board, team, enemy_team, self.moves)

    def check_forced_moves_agro(self, board, team, enemy_team, moves):
        self.debug_print("Test Board", self.board)
        for item in moves:
            self.board[item[0]][item[1]] = 'X'
            self.debug_print("Test Board", self.board)
            self.cord = self.check_for_team_win(self.board, self.team)
            self.debug_print("Next Cord", self.cord)


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
            if self.check_empty(left):
                self.debug_print("Left Win Possible", self.left.count(team))
                self.execute_diag_win(board, team, "left")
                return "diag_win"
        if self.right.count(team) == 2:
            if self.check_empty(self.right):
                self.execute_diag_win(board, team, "right")
        if self.row0.count(team) == 2:
            if self.check_empty(self.row0):
                self.execute_row_win(board, team, 0)
        if self.row1.count(team) == 2:
            if self.check_empty(row1):
                self.execute_row_win(board, team, 1)
        if self.row2.count(team) == 2:
            if self.check_empty(self.row2):
                self.execute_row_win(board, team, 2)
        if self.col0.count(team) == 2:
            self.debug_print("win check", "col0")
            if self.check_empty(self.col0):
                self.execute_col_win(board, team, 0)
        if self.col1.count(team) == 2:
            self.debug_print("win check", "col1")
            if self.check_empty(col1):
                self.execute_col_win(board, team, 1)
        if self.col2.count(team) == 2:
            self.debug_print("win check", "col2")
            if self.check_empty(col2):
                self.execute_col_win(board, team, 2)
        else:
            return None

    def check_for_enemy_win(self, board, enemy_team, team):
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
        early_game(board, team)
        debug_print("Made", "It")

    def execute_diag_win(self, board, team, side):
        debug_print("Execute diagonal", "Win")
        if side == "left":
            debug_print("Left", "Win")
            return find_diag_spot(get_diags(board)[0], "left")
        if side == "right":
            debug_print("Right", "Win")
            return find_diag_spot(get_diags(board)[1], "right")

    def execute_row_win(self, board, team, row_num):
            return find_row_spot(get_row(board, row_num), row_num)

    def execute_col_win(self, board, team, col_num):
            return find_col_spot(get_col(board, col_num), col_num)

    def execute_row_block(self, board, team, row_num):
            return find_row_spot(get_row(board, row_num), row_num)

    def execute_col_block(self, board, team, col_num):
            return find_col_spot(get_col(board, col_num), col_num)

    def execute_diag_block(self, board, team, side):
        if side == "left":
            return find_diag_spot(get_diags(board)[0], "left")
        if side == "right":
            return find_diag_spot(get_diags(board)[1], "right")

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

test = Forsight()
test.check_possible_moves(test.board, test.team, test.enemy_team)
