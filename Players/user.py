"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

File containing the script of a user, type player.
"""


class User:
    def __str__(self):
        return "User"

    @staticmethod
    def play(grid, player):
        move = -1
        while move > 7 or move < 1:
            try:
                move = int(input(f"Round player {player}\n"
                                 f"In which row do you want to play ?"))
                break
            except ValueError:
                pass
        return move-1

