class Grid:
    def __init__(self):
        self.grid = [[0 for i in range(7)] for j in range(6)]
        self.round = 0
        self.winner = None

    def show(self):
        for i in range(6):  # y coordinate
            for j in range(7):  # x coordinate
                print(self.grid[i][j], end=' ')
            print()
        print("_ _ _ _ _ _ _\n0 1 2 3 4 5 6")

    def play_move(self, col, player):
        """
        Method which plays move from a given column.
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
                self.grid[5][j] = player
                break

    def endgame(self, player, last_pos):
        """
        Method which checks if the game is finished, returns 'True'. Otherwise, 'False'.
        Changes the winner attribute into 'True' if there is a winner.
        """
        print("test finish")
        if last_pos is not None:
            POSSIBLE_DIRECTION = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
            for direction in POSSIBLE_DIRECTION:
                if self.rec_check(direction,  last_pos, player, 0):
                    print("Finish True")
                    return True
                else:
                    return False
        else:
            return False

    def rec_check(self, direction, last_pos, player, n):
        i, a = last_pos[0], direction[0]
        j, b = last_pos[1], direction[1]

        if n == 4:
            return True
        elif self.grid[i+a][j+b] != player:
            return False
        elif self.grid[i+a][j+b] == player:
            return self.rec_check(direction, (i+a, j+b), player, n+1)

