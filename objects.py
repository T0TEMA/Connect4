"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

File containing the game objects (Like the game grid).
"""
from constant import COLORS


class Grid:
    def __init__(self):
        self.grid = [[0 for i in range(7)] for j in range(6)]
        self.round = 0
        self.winner = None

    def show(self, showing):
        """
        Method that chows the grid if showing parameter is 'True'.
        """
        if showing:
            print()
            for i in range(6):  # y coordinate
                for j in range(7):  # x coordinate
                    if self.grid[i][j] == 1:
                        print(end=f'{COLORS["red"]}1 ')  # Displays a yellow '1' in the grid.
                    elif self.grid[i][j] == 2:
                        print(end=f'{COLORS["yellow"]}2 ')  # Displays a red '2' in the grid.
                    else:
                        print(end=f'{COLORS[""]}. ')  # Displays a dot in the game grid.
                print('\033[0m')
            print("_ _ _ _ _ _ _\n1 2 3 4 5 6 7")
        else:
            return

    def play_move(self, col, player):
        """
        Method that plays move from a given column. It changes the grid attribute of Grid class.
        Returns the position where the piece stopped in the grid.
        """
        i = 0
        j = col
        while True:
            try:
                if self.grid[i+1][j] == 0:
                    i += 1
                elif self.grid[i+1][j] != 0:
                    self.grid[i][j] = player
                    break
            except IndexError:
                i = 5
                self.grid[i][j] = player
                break
        return i, j

    def endgame(self, player, last_pos):
        """
        Method that checks if the game is finished, returns 'True'. Otherwise, 'False'.
        Changes the winner attribute into 'True' if there is a winner.
        """
        if not self.possible_moves():  # Checks if you can play in the grid, otherwise the game is finished.
            return True
        elif last_pos is not None:
            POSSIBLE_DIRECTION = (((-1, -1), (1, 1)), ((-1, 1), (1, -1)), ((0, -1), (0, 1)), ((1, 0)))
            for i in range(4):
                if i < 3:
                    concatenation = self.rec_check(POSSIBLE_DIRECTION[i][0],  last_pos, player, 1) + self.rec_check(POSSIBLE_DIRECTION[i][1], last_pos, player, 1) -1
                else:
                    concatenation = self.rec_check(POSSIBLE_DIRECTION[i],  last_pos, player, 1)
                if concatenation >= 4:
                    self.winner = True
                    return True
            return False
        elif last_pos is None:
            return False

    def rec_check(self, direction, last_pos, player, n):
        """
        Recursive method that checks, if there is a piece of "player" in "direction" + "last_pos" in the grid.
        If it is calls the method again (recursion) while "n" equals to 4 (means there are 4 pieces in a row,
        "player" has won) or when next position is out of the grid or not equals to "player".
        """
        i, a = last_pos[0], direction[0]
        j, b = last_pos[1], direction[1]

        try:
            if j+b < -1:  # Correcting issue #1 (github)
                raise IndexError
            elif self.grid[i+a][j+b] != player or n == 4:
                return n
            elif self.grid[i+a][j+b] == player:
                return self.rec_check(direction, (i+a, j+b), player, n+1)
        except IndexError:
            return n

    def possible_moves(self):
        possible_moves = []
        for i in range(7):
            if self.grid[0][i] == 0:
                possible_moves.append(i)
        return possible_moves
