from copy import deepcopy as dcopy

# Constants

# Movement directions
NORTH = "NORTH"
SOUTH = "SOUTH"
WEST = "WEST"
EAST = "EAST"

NORTH_WEST = "NORTH_WEST" 
NORTH_EAST = "NORTH_EAST"
SOUTH_WEST = "SOUTH_WEST"
SOUTH_EAST = "SOUTH_EAST"

# For Knight 
UP_RIGHT = "UP_RIGHT"

UP_LEFT = "UP_LEFT"
DOWN_RIGHT = "DOWN_RIGHT"
DOWN_LEFT = "DOWN_LEFT"
RIGHT_UP = "RIGHT_UP"
RIGHT_DOWN = "RIGHT_DOWN"
LEFT_UP = "LEFT_UP"
LEFT_DOWN = "LEFT_DOWN"

COLOR = "COLOR"
NAME = "NAME"

WHITE = "WHITE"
BLACK = "BLACK"

EMPTY = None

PAWN = "PAWN"
KNIGHT = "KNIGHT"
BISHOP = "BISHOP"
ROOK = "ROOK"
QUEEN = "QUEEN"
KING = "KING"

# Piece keys 
WHITE_PAWN = "WHITE_PAWN"
WHITE_KNIGHT = "WHITE_KNIGHT"
WHITE_BISHOP = "WHITE_BISHOP"
WHITE_ROOK = "WHITE_ROOK"
WHITE_QUEEN = "WHITE_QUEEN"
WHITE_KING = "WHITE_KING"

BLACK_PAWN = "BLACK_PAWN"
BLACK_KNIGHT = "BLACK_KNIGHT"
BLACK_BISHOP = "BLACK_BISHOP"
BLACK_ROOK = "BLACK_ROOK"
BLACK_QUEEN = "BLACK_QUEEN"
BLACK_KING = "BLACK_KING"

# Might not need these
        

# Piece data


# Piece creator

class Piece():  
    """
    This class is just a namespace for methods relating to chess pieces.

    For example to get a pieces color use: Piece.color_of(piece)   
    """
    # Chess piece helper functions
    DATA = {
        WHITE_PAWN:     {COLOR: WHITE, NAME: PAWN}, 
        WHITE_ROOK:     {COLOR: WHITE, NAME: ROOK}, 
        WHITE_KNIGHT:   {COLOR: WHITE, NAME: KNIGHT}, 
        WHITE_BISHOP:   {COLOR: WHITE, NAME: BISHOP}, 
        WHITE_QUEEN:    {COLOR: WHITE, NAME: QUEEN}, 
        WHITE_KING:     {COLOR: WHITE, NAME: KING},

        BLACK_PAWN:     {COLOR: BLACK, NAME: PAWN}, 
        BLACK_ROOK:     {COLOR: BLACK, NAME: ROOK}, 
        BLACK_KNIGHT:   {COLOR: BLACK, NAME: KNIGHT}, 
        BLACK_BISHOP:   {COLOR: BLACK, NAME: BISHOP}, 
        BLACK_QUEEN:    {COLOR: BLACK, NAME: QUEEN}, 
        BLACK_KING:     {COLOR: BLACK, NAME: KING}
    }

    CREATE = {
        WHITE: {
            PAWN:   WHITE_PAWN, 
            ROOK:   WHITE_ROOK, 
            KNIGHT: WHITE_KNIGHT, 
            BISHOP: WHITE_BISHOP, 
            QUEEN:  WHITE_QUEEN, 
            KING:   WHITE_KING
        }, 

        BLACK: {
            PAWN:   BLACK_PAWN, 
            ROOK:   BLACK_ROOK, 
            KNIGHT: BLACK_KNIGHT, 
            BISHOP: BLACK_BISHOP, 
            QUEEN:  BLACK_QUEEN, 
            KING:   BLACK_KING
        }
    }

    DIRECTIONS = {
        NORTH: (-1, 0),
        SOUTH: (1, 0),
        EAST: (0, 1),
        WEST: (0, -1),
        NORTH_EAST: (-1, 1),
        NORTH_WEST: (-1, -1),
        SOUTH_EAST: (1, 1),
        SOUTH_WEST: (1, -1),
        # for knight
        UP_LEFT: (-2, -1),
        UP_RIGHT: (-2, 1),
        DOWN_LEFT: (2, -1),
        DOWN_RIGHT: (2, 1),
        LEFT_UP: (-1, -2),
        LEFT_DOWN: (1, -2),
        RIGHT_UP: (-1, 2),
        RIGHT_DOWN: (1, 2)
    }

    MOVEMENT = {
        PAWN: {WHITE: (NORTH, NORTH_EAST, NORTH_WEST), BLACK: (SOUTH, SOUTH_WEST, SOUTH_EAST)},
        KNIGHT: (UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT, LEFT_UP, LEFT_DOWN, RIGHT_UP, RIGHT_DOWN),
        BISHOP: (NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST),
        ROOK: (NORTH, SOUTH, WEST, EAST),
        QUEEN: (NORTH, SOUTH, WEST, EAST, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST),
        KING: (NORTH, SOUTH, WEST, EAST, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST)
    }

    VALUE = {PAWN: 1, BISHOP: 3, KNIGHT: 3.5, ROOK: 5, QUEEN: 10, KING: 0} # what do we do for the KINGs value? 

    COLORS = (WHITE, BLACK)
    NAMES = (PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING)
    PIECES = (
        WHITE_PAWN, WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING,
        BLACK_PAWN, BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING
    )
    WHITE_PIECES = (WHITE_PAWN, WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING)
    BLACK_PIECES = (BLACK_PAWN, BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING)


    @property
    def names():
        return Piece.NAMES


    @staticmethod
    @property
    def colors():
        return (Piece.COLORS)


    @staticmethod
    @property
    def white():
        return dcopy(Piece.WHITE_PIECES)


    @staticmethod
    @property
    def black():
        return Piece.BLACK_PIECES


    @staticmethod
    @property
    def all():
        return Piece.PIECES


    @staticmethod
    def color_of(piece):
        return Piece.DATA[piece][COLOR]


    @staticmethod
    def name_of(piece):
        return Piece.DATA[piece][NAME]


    @staticmethod
    def data_of(piece):
        return Piece.DATA[piece]


    @staticmethod
    def create(color, name):
        return Piece.CREATE[color][name]


    @staticmethod
    def value_of(piece):
        return  Piece.VALUE[Piece.name_of(piece)]


    @staticmethod
    def movement_of(piece):
        name = Piece.color_of(piece)
        if name == PAWN:
            return Piece.MOVEMENT[name][color]
        else:
            return Piece.MOVEMENT[name]


    @staticmethod
    def directions_of(direct):
        return DIRECTIONS[direct]


    @staticmethod
    def format(piece):  
        if Piece.name_of(piece) == KNIGHT:
            return Piece.color_of(piece)[0] + Piece.name_of(piece)[1] 
        else: 
            return Piece.color_of(piece)[0] + Piece.name_of(piece)[0]


class Board():
    # Called when creating class instance 
    def __init__(self):

        # Board creator, is this the correct setup? Should this even be here?
        self.__board = [
            [BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING, BLACK_BISHOP, BLACK_KNIGHT, BLACK_ROOK],
            [BLACK_PAWN for n in range(8)],
            [EMPTY for n in range(8)],
            [EMPTY for n in range(8)],
            [EMPTY for n in range(8)],
            [EMPTY for n in range(8)],
            [WHITE_PAWN for n in range(8)],
            [WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_KING, WHITE_QUEEN, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK]
        ]

        # Piece dictionaries, phase these out in favor of self.__pieces
        self.__white_pieces = {PAWN: [], KNIGHT: [], BISHOP: [], ROOK: [], QUEEN: [], KING: []} 
        self.__black_pieces = {PAWN: [], KNIGHT: [], BISHOP: [], ROOK: [], QUEEN: [], KING: []}

        self.__pieces = {
            WHITE_PAWN: [], WHITE_ROOK: [], WHITE_KNIGHT: [], WHITE_BISHOP: [], WHITE_KING: [], 
            WHITE_QUEEN: [], WHITE_BISHOP: [], WHITE_KNIGHT: [], WHITE_ROOK: [],

            BLACK_PAWN: [], BLACK_ROOK: [], BLACK_KNIGHT: [], BLACK_BISHOP: [], BLACK_KING: [], 
            BLACK_QUEEN: [], BLACK_BISHOP: [], BLACK_KNIGHT: [], BLACK_ROOK: []
        }

        # Populates the piece dictionaries using the board
        for rIdx in range(8):
            for cIdx in range(8):
                square = self.__board[rIdx][cIdx]
                if square != EMPTY:
                    self.__pieces[square] += [[rIdx, cIdx]]
                    if Piece.color_of(square) == WHITE:
                        self.__white_pieces[Piece.name_of(square)] += [[rIdx, cIdx]]
                    elif Piece.color_of(square) == BLACK:
                        self.__black_pieces[Piece.name_of(square)] += [[rIdx, cIdx]]

        # True if the color can still castle on that side
        self.__white_can_castle_left = True
        self.__white_can_castle_right = True
        self.__black_can_castle_left = True
        self.__black_can_castle_right = True

        # True of the color has castled
        self.__white_castled = False
        self.__black_castled = False

        # The next color to move
        self.__current_move = WHITE



    # Called when class instance is printed
    def __str__(self):
        print_board = "\n    0   1   2   3   4   5   6   7\n"
        print_board += "  " + "===="*8 + "==\n"
        for rIdx in range(-8, 0, 1):
            print_board += str(-rIdx) + " |"
            for cIdx in range(8):
                pos = self.square(rIdx, cIdx)
                if pos == EMPTY:
                    print_board += " -- "
                else:
                    print_board += " " + Piece.format(pos) + " "
            print_board += "| " + str(8+rIdx) + "\n"

        print_board += "  " + "===="*8 + "==\n"
        print_board += "    A   B   C   D   E   F   G   H\n"    
        return print_board

    # I've used the dcopy function to prevent the accidental modification of data thorough the getter methods
    # I'll add dedicated setter methods that do the appropriate type and error checking. 

    @property
    def board(self):
        return dcopy(self.__board)

    # Make getter and setter methods for the square
    def square(self, idx1, idx2=None):
        if idx2 == None:
            return self.__board[idx1[0]][idx1[1]]
        else:
            return self.__board[idx1][idx2]


    @property
    def white_pieces(self):
        return {Piece.name_of(piece): self.__pieces[piece] for piece in Piece.white}


    @property
    def black_pieces(self):
        return dcopy(self.__black_pieces)

    @property
    def pieces(self):
        return dcopy(self.__pieces)
    


    def find_position(self, piece):
        """
        Returns a list of positions for the pieces with COLOR: color and NAME: name
        """
        return self.__pieces[piece]


    @property
    def white_castled(self):
        return self.__white_castled


    @property
    def black_castled(self):
        return self.__black_castled


    @property
    def current_move(self):
        return self.__current_move


    @property
    def white_piece_value(self):
        """
        Returns the total value of the white pieces in the dict self.__white_pieces
        """
        return sum([Piece.value_of(piece) * len(pos) for piece, pos in self.__white_pieces.items()])


    @property
    def black_piece_value(self):
        """
        Returns the total value of the black pieces in the dict self.__black_pieces
        """
        return sum([Piece.value_of(piece) * len(pos) for piece, pos in self.__black_pieces.items()])


    # This needs to be changed to something that checks for checkmate
    @property
    def winner(self):
        """
        Returns the color of the winner is there is one, else returns False 
        """
        if not self.find_position(WHITE, KING) and not self.find_pieces(BLACK, KING):
            raise ValueError("Both kings are gone.")
        elif not self.find_position(WHITE, KING):
            return BLACK
        elif not self.find_position(BLACK, KING):
            return WHITE
        else:
            return False


    def remove_piece(self, pos):
        square = self.__board[pos[0]][pos[1]]
        color = Piece.color_of(square)
        name = Piece.name_of(square)

        if color == WHITE:
            idx = self.__white_pieces[name].index(pos)
            del self.__white_pieces[name][idx]
        elif color == BLACK:
            idx = self.__black_pieces[name].index(pos)
            del self.__black_pieces[name][idx]

        self.__board[pos[0]][pos[1]] = EMPTY


    def move(self, start_pos, end_pos, debug=False):
        
        # Extract the row and column indexes for ease of use
        start_rIdx = start_pos[0]
        start_cIdx = start_pos[1]
        end_rIdx = end_pos[0]
        end_cIdx = end_pos[1]

        start_square = self.__board[start_rIdx][start_cIdx]
        end_square = self.__board[end_rIdx][end_cIdx]

        if debug: print("\n=== ChessBoard.make_move({}, {}) ===".format(start_pos, end_pos))

        # ValueError checking
        if start_square == EMPTY:
            raise ValueError("The piece to move does not exist.")
        elif Piece.color_of(start_square) != self.__current_move:
            raise ValueError("The piece is the wrong color.")
        elif end_square != EMPTY:
            if Piece.color_of(end_square) == self.__current_move:
                raise ValueError("Can not take piece of same color.")

        piece_name = Piece.name_of(start_square)
        piece_color = Piece.color_of(start_square)

        if debug:
            print("\n=== Before move")
            print("Start square:", start_square)
            print("End square:", end_square)
            print("Board at start pos:", self.__board[start_rIdx][start_cIdx])
            print("Board at end pos:", self.__board[end_rIdx][end_cIdx])

        self.__update_board(start_pos, end_pos)

        # Logic for pawn promotion
        if start_square == WHITE_PAWN and end_rIdx == 0:
            self.__white_promote(end_pos)
        elif start_square == BLACK_PAWN and end_rIdx == 7:
            self.__black_promote(end_pos)
        
        # Logic for castling
        elif not self.__white_castled and (self.__white_can_castle_left or self.__white_can_castle_right):
            if start_square == WHITE_KING: 
                if self.__white_can_castle_left and end_pos == [7, 1]:
                    self.__white_castle([7, 0])
                elif self.__white_can_castle_right and end_pos == [7, 5]:
                    self.__white_castle([7, 7])
                else:
                    self.__white_can_castle_left = False
                    self.__white_can_castle_right = False

            elif start_square == WHITE_ROOK:
                if start_pos == [7, 0]:
                    self.__white_can_castle_left = False
                elif start_square == [7, 7]:
                    self.__white_can_castle_right = False

        elif not self.__black_castled and (self.__black_can_castle_left or self.__black_can_castle_right):            
            if start_square == BLACK_KING:
                if self.__black_can_castle_left and end_pos == [0, 2]:
                    self.__black_castle([0, 0])
                elif self._black_castle_right and end_pos == [0, 6]:
                    self.__black_castle([0, 7])
                else:
                    self.__black_can_castle_left = False
                    self.__black_can_castle_right = False

            elif start_square == BLACK_ROOK:
                if start_pos == [0, 0]:
                    self.__black_can_castle_left = False
                elif start_pos == [0, 7]:
                    self.__black_can_castle_right = False

        if debug:
            print("\n=== After move")
            print("Start square:", start_square)
            print("End square:", end_square)
            print("Board at start pos:", self.__board[start_rIdx][start_cIdx])
            print("Board at end pos:", self.__board[end_rIdx][end_cIdx])


    def __update_board(self, start_pos, end_pos):

        start_rIdx = start_pos[0]
        start_cIdx = start_pos[1]
        end_rIdx = end_pos[0]
        end_cIdx = end_pos[1]
        
        end_square = self.__board[end_rIdx][end_cIdx]
        start_square = self.__board[start_rIdx][start_cIdx]

        piece_color = Piece.color_of(start_square)
        piece_name = Piece.name_of(start_square)

        if piece_color == WHITE:
            # Update the piece dictionary
            idx = self.__white_pieces[piece_name].index(start_pos)  # Finds the index of the position
            self.__white_pieces[piece_name][idx] = end_pos  # Sets the pieces position to the end position

            # Logic for taking
            if end_square != EMPTY and Piece.color_of(end_square) != piece_color:
                if Piece.color_of(end_square) == piece_color:
                    raise ValueError("Cannot take piece of same color")
                take_name = Piece.name_of(end_square)
                idx = self.__black_pieces[take_name].index([end_rIdx, end_cIdx])  # Finds the index of the position of the taken piece
                del self.__black_pieces[take_name][idx]  # Removes the position of the taken piece
        
        elif piece_color == BLACK:
            # Update the piece dictionary
            idx = self.__black_pieces[piece_name].index(start_pos)  # Finds the index of the position
            self.__black_pieces[piece_name][idx] = end_pos  # Sets the pieces position to the end position

            # Logic for taking
            if end_square != EMPTY:
                if Piece.color_of(end_square) == piece_color:
                    raise ValueError("Cannot take piece of same color")
                take_name = Piece.name_of(end_square)
                idx = self.__white_pieces[take_name].index(end_pos)  # Finds the index of the position of the taken piece
                del self.__white_pieces[take_name][idx]  # Removes the position of the taken piece

        # Update the board
        self.__board[start_rIdx][start_cIdx] = EMPTY
        self.__board[end_rIdx][end_cIdx] = Piece.create(piece_color, piece_name)


    def __white_castle(self, rook_start):
        self.__white_can_castle_left = False
        self.__white_can_castle_right = False
        self.__white_castled = True
        
        if rook_start == [7, 0]:
            rook_end = [7, 2]
        elif rook_start == [7, 7]:
            rook_end = [7, 4]

        if self.__board[rook_end[0]][rook_end[1]] != EMPTY:
            raise ValueError("White castling error: the rooks end position is occupied.")

        self.__update_board(rook_start, rook_end)


    def __black_castle(self, rook_start):
        self.__black_can_castle_left = False
        self.__black_can_castle_right = False
        self.__black_castled = True

        if rook_start == [0, 0]:
            rook_end = [0, 3]
        elif rook_start == [0, 7]:
            rook_end = [0, 5]

        if self.__board[rook_end[0]][rook_end[1]] != EMPTY:
            raise ValueError("Black castling error: the rooks end position is occupied.")

        self.__update_board(rook_start, rook_end)


    def __white_promote(self, pawn_pos):
        idx = self.__white_pieces[PAWN].index(pawn_pos) 
        del self.__white_pieces[PAWN][idx]
        self.__white_pieces[QUEEN] += [pawn_pos]
        self.__board[pawn_pos[0]][pawn_pos[1]] = Piece.create(WHITE, QUEEN)


    def __black_promote(self, pawn_pos):
        idx = self.__black_pieces[PAWN].index(pawn_pos) 
        del self.__black_pieces[PAWN][idx]
        self.__black_pieces[QUEEN] += [pawn_pos]
        self.__board[pawn_pos[0]][pawn_pos[1]] = Piece.create(BLACK, QUEEN)



# This will not run if the file is imported.
if __name__ == "__main__":
    CB = Board()
    print(CB)
    print("White pieces:", CB.white_pieces, "\n")
    print("Black pieces:", CB.black_pieces, "\n")
    print("Pieces:", CB.pieces, "\n")
    print(CB.white_piece_value)
    print(CB.black_piece_value)
    print(CB.winner)
    CB.move([7, 1], [5, 1])
    CB.move([7, 2], [5, 2])
    print(CB)
    CB.move([7, 3], [7, 1])
    print(CB)
    CB.move([6, 0], [0, 0])
    print(CB)
