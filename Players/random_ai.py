"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

File containing the script of a random AI, type player.
"""

from random import choice


class RandomAI:
    def __str__(self):
        return "Random Ai"

    @staticmethod
    def play(grid, color, last, possible):
        return choice(possible)
