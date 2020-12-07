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
    Highest=0

# -------------------------------- Create Knight ------------------------------------
    def __init__(self, place, ghost=None):
#        print(self)
        self.board=[]
        self.moves=[]
        self.create_board()
        self.ghost = ghost
        
        if ghost:
            for move in ghost:
                self.place(move)
        
        self.place(place)

        Knight.All_knights.append(self)

# -------------------------------- Place Knight ------------------------------------
    def place(self,place):
        self.moves.append(place)
        self.board.remove(place)
#        print("knight to : "+str(place))


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
            new_knight = Knight(move, ghost=self.moves)
            var += 1
#        sleep(1)
#            print("\nmove: "+ str(var+1))
#            print(move)
#            print(new_knight.board)
#            print("\nknights: "+str(len(Knight.All_knights)))
#       print('\nThis knight is dead: ' + str(self))
        Knight.All_knights.remove(self)
        if len(self.moves) > Knight.Highest:
            Knight.Highest = len(self.moves)
            print(f"\n{self} is the best yet with {len(self.moves)}\n\n{self.moves}")
        if var % 100000000 == 0:
            pass
            #print(f"\nvar = {var}\nknights:  {str(len(Knight.All_knights))}")

