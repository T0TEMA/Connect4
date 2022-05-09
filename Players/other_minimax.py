from random import choice


class Minimax():
    
    def __init__(self, player, board):
        self.board = board
        self.player = player

    def play(self, depth):
        move,_ = self.minimax(self.player, depth)
        return move

    def minimax(self, game, depth, maximize=True):

        endGame = self.endGame()
        if depth == 0 or endGame is not None:
            score = 10+depth if endGame == self.player else -10-depth if endGame is not None else 0
            return None, score

        best_score = float("inf") if not maximize else float("-inf") if maximize else 0
        best_actions = []

        for pos, next_pos in self.search_move(game):

            # Effectuer le coup
            case1 = self.board[pos[0]][pos[1]]
            case2 = self.board[next_pos[0]][next_pos[1]]

            self.board[pos[0]][pos[1]] = 0
            self.board[next_pos[0]][next_pos[1]] = case1

            # Lance la récursion
            _, score = self.minimax(3-game, depth-1, not maximize)

            # Annuler le coup
            self.board[pos[0]][pos[1]] = case1
            self.board[next_pos[0]][next_pos[1]] = case2

            if (not maximize and score < best_score) or (maximize and score > best_score):
                best_score = score
                best_actions = [(pos, next_pos)]
            elif score == best_score:
                best_actions.append((pos, next_pos))

        return choice(best_actions), best_score

    def endGame(self):
        """
        True si self.player gagne avec self.board
        False si perd
        None si non
        """
        pass


    def search_move(self, player):
        """
        liste des coups possible pour le player
        """
        pass
