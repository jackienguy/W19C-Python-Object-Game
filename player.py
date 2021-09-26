class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn

    # TODO
    # def moveUp(self):
    
    # TODO
    # def moveDown(self):

    # TODO
    # def moveLeft(self):

    # TODO
    # def moveRight(self):

class Moves(Player):
    def player_move(self, w, s, a, d, position):
        self.up = w
        self.down = s
        self.left = a
        self.right = d
        
        if (input == w):
            position += 1
            print("Moved up")
        elif (input == s):
            position -= 1
            print("Moved down")
        elif(input == a):
            position -= 1
            print("Moved left")
        elif(input == d):
            print("Moved right")
        else:
            print("Invlaid key")


