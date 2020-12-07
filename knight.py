from time import sleep

class Knight:
    MOVES=[
        [1,2],
        [1,-2],
        [-1,2],
        [-1, -2],
        [2, 1],
        [2, -1],
        [-2, 1],
        [-2, -1]
        ]
    All_knights=[]
    Winners=[]

# -------------------------------- Create Knight ------------------------------------
    def __init__(self, place=None, ghost=False):
        print(self)
        self.board=[]
        self.moves=[]
        self.create_board()
        self.ghost = ghost
        

        if ghost:
            for move in self.moves:
                self.place(move)

        else:
            self.place(place)

        Knight.All_knights.append(self)

# -------------------------------- Place Knight ------------------------------------
    def place(self,place):
        self.moves.append(place)
        self.board.remove(place)
        print("knight to : "+str(place))


# -------------------------------- Mark used squares ------------------------------------
#     def mark(self, square):
#         self.board.remove(square)


# -------------------------------- create board ------------------------------------
    def create_board(self):
        self.board =[]
        for x in range(8):
            for y in range(8):
                self.board.append([x+1, y+1])

# -------------------------------- Return possible squares for next move ------------------------------------
    def possible_squares(self):
        squares=[]
        for i in range(8):
            x = Knight.MOVES[i][0] + self.moves[-1][0]
            y = Knight.MOVES[i][1] + self.moves[-1][1]
            new_pos = [x,y]
            if new_pos in self.board:
                squares.append(new_pos)

        return squares

# -------------------------------- Replicate ghosts knights ------------------------------------
    def fragment_knight(self):
        var = 0
        for move in self.possible_squares():
            new_knight=None
            print("\nmove: "+ str(var+1))
            print(move)
            sleep(.5)
            new_knight = Knight(ghost=True)
            
            print(new_knight.board)
            new_knight.moves = self.moves
            new_knight.place(move)
            print("\nknights: "+str(len(Knight.All_knights)))
            var += 1

        print('\nThis knight is dead: ' + str(self))
        del self
        print("\nknights: "+ str(len(Knight.All_knights)))

    def print(self):
        for move in self.moves:
            print(str(move) + '\n')
def tour():
    k = Knight(place=[1,1])
    k.place([k.possible_squares()[0]])

    for x in range(8):
        for y in range(8):
            k = Knight([x+1, y+1])
            print(k.moves[0])
            print(k.possible_squares())
