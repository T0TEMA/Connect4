"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

File containing the script of a minimax AI, player type.
"""
from random import choice
from objects import Grid


class MinimaxAI:
    def __init__(self):
        self.DEPTH = int(input("Minimax depth of search :"))
        self.WIN_SCORE = 100
        self.minimax_grid = Grid()

    def __str__(self):
        return "Minimax AI"

    def play(self, grid, current, last, possible):
        """
        Method that's called from the mainloop.
        Method that launch 'i' amount of searches depending on the "possible moves" at a beginning of "search"
        and a given moment of "search".
        """
        self.minimax_grid.grid = grid
        best_score = None
        best_move = None
        for move in possible:
            last_pos = self.minimax_grid.play_move(move, current)
            score = self.minimax(self.DEPTH, current, last_pos)
            self.undo_move(move)
            if best_score is None or score > best_score:
                best_score = score
                best_move = [move]
            elif score == best_score:
                best_move.append(move)
            print(move+1, score)
        return choice(best_move)

    def minimax(self, depth, current, last_pos):
        """
        Returns a score depending on victory (100) or if the maximal depth has been reached (0).
        """
        if self.minimax_grid.endgame(current, last_pos):
            if self.minimax_grid.winner:
                return self.WIN_SCORE + depth
            else:
                return 0
        if depth == 0:
            return 0

        possible_moves = self.minimax_grid.possible_moves()
        for move in possible_moves:
            score = 0
            last_pos = self.minimax_grid.play_move(move, current)
            score += self.minimax(depth - 1, 3 - current, last_pos)
            self.undo_move(move)
        return score

    def undo_move(self, pos):
        i = -1
        while True:
            i += 1
            if self.minimax_grid.grid[i][pos] != 0:
                self.minimax_grid.grid[i][pos] = 0
                break
