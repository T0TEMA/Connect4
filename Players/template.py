"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

File containing a template of what a 'player type' class must be.
"""


class Template:
    def __str__(self):
        return "Template AI"

    @staticmethod
    def play(self, grid, current, last, possible):
        """
        Method that returns a move (value between 1 and 7 included), corresponding to one of
        the columns of the grid.

        Parameters :
            grid = 6 lists of [7 values]
                Values can be equal to 0 (empty place), 1 (player 1 token) or 2 (player 2 token).
            player = 1 or 2
                PLayer, is the value representing the color of the players (this class) token.
        """
        # Calculate move
        # Return move
