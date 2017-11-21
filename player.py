class Player:
    def __init__(self,iden):
        if iden > 1:
            print("invalid")
            del self


class Human(Player):
    def get_input(self):
        return int(input('Which column:'))


class Robot(Player):
    def get_input(self):
        return 3
