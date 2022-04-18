"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.9

File that permits a multiple game launch (simulation).
"""
from time import time
from main import main
from Players.random_ai import RandomAI

player1 = RandomAI()  # Set player 1 type.
player2 = RandomAI()  # Set player 2 type.
N = 10000  # Amount of simulations.
p1_wins = 0
p2_wins = 0

tI = time()  # Time at beginning of simulation.
for _ in range(N):
    winner = main(player1, player2, False)  # Launching main function of root file.
    if winner == 1:
        p1_wins += 1
    elif winner == 2:
        p2_wins += 1
tF = time()  # Time at end of simulation.

print(f"Simulation time {tF - tI} s\n"  # Calculating simulation time.
      f"{player1} (P1) : {p1_wins} wins\n"
      f"{player2} (P2) : {p2_wins} wins")
