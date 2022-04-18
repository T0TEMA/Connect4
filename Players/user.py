class User:
    @staticmethod
    def play(grid, player):
        move = -1
        while move > 7 or move < 1:
            try:
                move = int(input("In which row do you want to play ?"))
                break
            except ValueError:
                pass
        return move

