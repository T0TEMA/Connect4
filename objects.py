"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

File containing the game objects (Like the game grid).
"""


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
                    print(self.grid[i][j], end=' ')
                print()
            print("_ _ _ _ _ _ _\n1 2 3 4 5 6 7")
        else:
            return

    def play_move(self, col, player):
        """
        Method that plays move from a given column.
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
        if last_pos is not None:
            POSSIBLE_DIRECTION = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
            for direction in POSSIBLE_DIRECTION:
                if self.rec_check(direction,  last_pos, player, 1):
                    return True
            return False
        else:
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
            if 0 > j+b:  # Correcting issue #1 (github)
                raise IndexError
            if n == 4:
                self.winner = True
                return True
            elif self.grid[i+a][j+b] != player:
                return False
            elif self.grid[i+a][j+b] == player:
                return self.rec_check(direction, (i+a, j+b), player, n+1)
        except IndexError:
            return False
