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

# -------------------------------- Create Knight ------------------------------------
    def __init__(self, place):
        self.board=[]
        self.moves=[]
        self.place(place)
        self.create_board()

# -------------------------------- Place Knight ------------------------------------
    def place(self,place):
        self.moves.append(place)

# -------------------------------- Move Knight ------------------------------------
    def move(self, move_pair):
        self.moves.append(move_pair)
        last_move = self.moves[-1]
        self.mark(last_move)

# -------------------------------- Mark used squares ------------------------------------
    def mark(self, square):
        self.board.remove(square)


    def check_move(self):
        self.

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

# -------------------------------- Replicate ghosts knights ------------------------------------
    def fragment_knight(self,knight):

        new_knight = Knight(knight.moves[-1])
        new_knight.moves = knight.moves
