"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

File containing the script of a user, type player.
"""


class User:
    def __str__(self):
        return "User"

    @staticmethod
    def play(grid, color, last, possible):
        move = -1
        while move not in possible:
            try:
                move = int(input(f"Round player {color}\n"
                                 f"In which row do you want to play ?")) - 1
            except ValueError:
                pass
        return move

