"""
Author : Totema (T0TEMA on GitHub)
Version : Python 3.10

File that permits a multiple game launch (simulation).
"""
from time import time
from main import main
from Players.random_ai import RandomAI
from Players.minimax_ai import MinimaxAI

player1 = MinimaxAI()  # Set player 1 type.
player2 = RandomAI()  # Set player 2 type.
N = int(input("Amount of games simulated.")) # Amount of simulations.

p1_wins = 0
p2_wins = 0
draw = 0

tI = time()  # Time at beginning of simulation.
for _ in range(N):
    winner = main(player1, player2, False)  # Launching main function of root file.
    if winner == 1:
        p1_wins += 1
    elif winner == 2:
        p2_wins += 1
    else:
        draw += 1
tF = time()  # Time at end of simulation.

print(f"Simulation time : {tF - tI} s\n"  # Calculating simulation time.
      f"{player1} (P1) : {p1_wins} ({p1_wins/(N/100)} %) wins \n"
      f"{player2} (P2) : {p2_wins} ({p2_wins/(N/100)} %) wins \n"
      f"Draws          : {draw}  ({draw/(N/100)} %) draws")

input("\nClose program")
