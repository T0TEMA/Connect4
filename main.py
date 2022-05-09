"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

Root file of the "Connect 4" project.
"""
from objects import Grid
from Players.user import User
from Players.random_ai import RandomAI
from Players.minimax_ai import MinimaxAI
from Players.other_minimax import Minimax
from constant import COLORS


def game_options():
    """
    Function that returns the chosen game options.
    (Actually you can only choose the two players).
    """
    print(f"Choose the players :\n0 : user\n1 : ai random\n2 : ai minimax\n")
    player1, player2 = -1, -1
    while player1 < 0 or player1 > 3 or player2 < 0 or player2 > 3:
        try:
            player1 = int(input('Player 1 : '))  # Yellow player
            player2 = int(input('Player 2 : '))  # Red player
        except ValueError:
            pass

    # Player 1
    if player1 == 0:
        player1 = User()
    elif player1 == 1:
        player1 = RandomAI()
    elif player1 == 2:
        player1 = MinimaxAI()
    elif player1 == 3:
        player1 = Minimax
    # Player 2
    if player2 == 0:
        player2 = User()
    elif player2 == 1:
        player2 = RandomAI()
    elif player2 == 2:
        player2 = MinimaxAI()
    elif player2 == 3:
        player2 = Minimax()

    return player1, player2


def main(player1, player2, display=True):
    """
    Main function, game loop.
    Returns the winner if it's not a draw.
    """
    grid = Grid()  # Instancing the grid.
    grid.show(display)
    current = 2  # Players round
    last = None  # Last played move
    possible = [0, 1, 2, 3, 4, 5, 6]

    while grid.endgame(current, last) is not True:
        current = 3 - current
        if current == 1:
            col = int(player1.play(grid.grid, current, last, possible))
        else:
            col = int(player2.play(grid.grid, current, last, possible))
        last = grid.play_move(col, current)  # Modifies the grid
        grid.show(display)
        possible = grid.possible_moves()
    if grid.winner is None:
        return None
    else:
        return current


if __name__ == '__main__':
    P1, P2 = game_options()
    winner = main(P1, P2)
    if winner is not None:
        print(f"Player {winner} ({COLORS[winner]}) has won !")
    else:
        print(f"Draw ... No winners.")