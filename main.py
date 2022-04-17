"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

"""
from objects import Grid
from Players.user import User
from Players.random_ai import RandomAI


def main():
    """
    Main function, loop
    """
    # Instancing the grid.
    grid = Grid()
    grid.show()
    # Choosing the players.
    print(f"\n0 : user\n1 : ai random \n2 : ai minimax ")
    player1 = input('Player 1 : ')  # Yellow player
    player2 = input('Player 2 : ')  # Red player

    player1 = User()

    current = 2  # Players round
    last = None

    while grid.endgame(current, last) is not True:
        current = 3 - current
        print(f"\nRound player {current}")
        grid.show()
        col = int(player1.play())
        grid.play_move(col, current)
    if grid.winner is None:
        print(f"Draw ... No winners.")
    else:
        print(f"Player {current} has won !")


if __name__ == '__main__':
    main()
