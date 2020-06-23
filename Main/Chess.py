from copy import deepcopy as dcopy

from time import time

from timeit import timeit

# Constants

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
NORTH_EAST = (-1, 1)
NORTH_WEST = (-1, -1)
SOUTH_EAST = (1, 1)
SOUTH_WEST = (1, -1)
# for knight
UP_LEFT = (-2, -1)
UP_RIGHT = (-2, 1)
DOWN_LEFT = (2, -1)
DOWN_RIGHT = (2, 1)
LEFT_UP = (-1, -2)
LEFT_DOWN = (1, -2)
RIGHT_UP = (-1, 2)
RIGHT_DOWN = (1, 2)

# # Movement directions
# NORTH = "NORTH"
# SOUTH = "SOUTH"
# WEST = "WEST"
# EAST = "EAST"

# NORTH_WEST = "NORTH_WEST" 
# NORTH_EAST = "NORTH_EAST"
# SOUTH_WEST = "SOUTH_WEST"
# SOUTH_EAST = "SOUTH_EAST"

# # For Knight 
# UP_RIGHT = "UP_RIGHT"

# UP_LEFT = "UP_LEFT"
# DOWN_RIGHT = "DOWN_RIGHT"
# DOWN_LEFT = "DOWN_LEFT"
# RIGHT_UP = "RIGHT_UP"
# RIGHT_DOWN = "RIGHT_DOWN"
# LEFT_UP = "LEFT_UP"
# LEFT_DOWN = "LEFT_DOWN"

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

class ChessPieceHandler():  
    """
    This class is just a namespace for methods relating to chess pieces.

    An instance of this class must be created for the property methods to work. 
    """
    # Class attributes 
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

    # DIRECTIONS = {
    #     NORTH: (-1, 0),
    #     SOUTH: (1, 0),
    #     EAST: (0, 1),
    #     WEST: (0, -1),
    #     NORTH_EAST: (-1, 1),
    #     NORTH_WEST: (-1, -1),
    #     SOUTH_EAST: (1, 1),
    #     SOUTH_WEST: (1, -1),
    #     # for knight
    #     UP_LEFT: (-2, -1),
    #     UP_RIGHT: (-2, 1),
    #     DOWN_LEFT: (2, -1),
    #     DOWN_RIGHT: (2, 1),
    #     LEFT_UP: (-1, -2),
    #     LEFT_DOWN: (1, -2),
    #     RIGHT_UP: (-1, 2),
    #     RIGHT_DOWN: (1, 2)
    # }

    DIRECTIONS = {
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
    def names(self):
        """
        Returns a tuple containing all chess piece names. 
        """
        return self.NAMES


    @property
    def colors(self):
        """
        Returns a tuple containing the chess colors.
        """
        return self.COLORS


    @property
    def white(self):
        """
        Returns a tuple containing all the white pieces.
        """
        return self.WHITE_PIECES


    @property
    def black(self):
        """
        Returns a tuple containing all the black pieces.
        """
        return self.BLACK_PIECES


    @property
    def all(self):
        """
        Returns a tuple containing all the chess pieces
        """
        return self.PIECES


    def color_of(self, piece):
        """
        Returns the color of the piece.
        """
        return self.DATA[piece][COLOR]


    def name_of(self, piece):
        """
        Returns the name of the piece.
        """
        return self.DATA[piece][NAME]


    def data_of(self, piece):
        """
        Returns a dictionary containing the color and name of the piece.
        """
        return self.DATA[piece]


    def create(self, color, name):
        """
        Returns a piece.   
        """
        return self.CREATE[color][name]


    def value_of(self, piece):
        """
        Returns the value of the piece.
        """
        return  self.VALUE[self.name_of(piece)]


    def directions_of(piece):
        """
        Returns the movement directions of piece.
        """
        name = self.color_of(piece)
        if name == PAWN:
            return self.DIRECTIONS[name][color]
        else:
            return self.DIRECTIONS[name]


    # def direction(self, direct):
    #     """
    #     Returns the direction tuple.
    #     """
    #     return self.DIRECTIONS[direct]


    def are_same_color(self, piece1, piece2):
        """
        Returns True is piece1 and piece2 are the sale color, otherwise False.
        """
        return self.color_of(piece1) == self.color_of(piece2)


    def format(self, piece):  
        if self.name_of(piece) == KNIGHT:
            return self.color_of(piece)[0] + self.name_of(piece)[1] 
        else: 
            return self.color_of(piece)[0] + self.name_of(piece)[0]


class ChessBoard():
    # Called when creating class instance 
    def __init__(self):

        self.__PiecesCls = ChessPieceHandler()

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

        self.__positions = {
            WHITE_PAWN: [], WHITE_ROOK: [], WHITE_KNIGHT: [], WHITE_BISHOP: [], WHITE_KING: [], 
            WHITE_QUEEN: [], WHITE_BISHOP: [], WHITE_KNIGHT: [], WHITE_ROOK: [],

            BLACK_PAWN: [], BLACK_ROOK: [], BLACK_KNIGHT: [], BLACK_BISHOP: [], BLACK_KING: [], 
            BLACK_QUEEN: [], BLACK_BISHOP: [], BLACK_KNIGHT: [], BLACK_ROOK: []
        }

        # Populates the piece position dictionary using the board
        for rIdx in range(8):
            for cIdx in range(8):
                square = self.__board[rIdx][cIdx]
                if square != EMPTY:
                    self.__positions[square] += [[rIdx, cIdx]]

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
                pos = self.get_square(rIdx, cIdx)
                if pos == EMPTY:
                    print_board += " -- "
                else:
                    print_board += " " + self.__PiecesCls.format(pos) + " "
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
    def get_square(self, *args):
        if len(args) == 1:
            return self.__board[args[0][0]][args[0][1]]
        elif len(args) == 2:
            return self.__board[args[0]][args[1]]


    @property
    def white_pieces(self):
        # Works on self.__positions
        return {piece: self.__positions[piece] for piece in self.__PiecesCls.white}


    @property
    def black_pieces(self):
        return {piece: self.__positions[piece] for piece in self.__PiecesCls.black}


    @property
    def pieces(self):
        return dcopy(self.__positions)
    

    def find_position(self, piece):
        """
        Returns a list of positions for the pieces with COLOR: color and NAME: name
        """
        return self.__positions[piece]


    @property
    def can_white_castle(self):
        return not self.__white_castled and (self.__white_can_castle_left or self.__white_can_castle_right)
    

    @property
    def white_castled(self):
        return self.__white_castled


    @property
    def can_black_castle(self):
        return not self.__black_castled and (self.__black_can_castle_left or self.__black_can_castle_right)
    

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
        return sum([self.__PiecesCls.value_of(piece) * len(self.__positions[piece]) for piece in self.__PiecesCls.white])


    @property
    def black_piece_value(self):
        """
        Returns the total value of the black pieces in the dict self.__black_pieces
        """
        return sum([self.__PiecesCls.value_of(piece) * len(self.__positions[piece]) for piece in self.__PiecesCls.black])


    @property
    def winner(self):
        """
        Returns the color of the winner is there is one, otherwise False.
        """
        pass


    def get_piece(self, pos):
        """
        Returns a tuple (piece, name, color) for the square at pos.
        """
        piece = self.__board[pos[0]][pos[1]]

        if piece == EMPTY:
            raise ValueError("The square is empty")

        return piece


    def is_on_board(self, pos):
        return 7 >= pos[0] > 0 and 7 >= pos[1] > 0


    def __add_piece(self, piece, pos):
        """
        Adds piece to the self.__board and self.__positions, overwriting the existing pos.
        """
        self.__board[pos[0]][pos[1]] = piece
        self.__positions[piece].append(pos)


    def __remove_piece(self, pos):
        """
        Removes the piece at pos from the self.__board and self.__positions.
        """
        piece = self.__board[pos[0]][pos[1]]

        idx = self.__positions[piece].index(pos)
        del self.__positions[piece][idx]

        self.__board[pos[0]][pos[1]] = EMPTY


    def __move_updater(self, start_pos, end_pos):
        """
        Moves the piece at start_pos to end_pos, and updates self.__board and self.__positions.
        """
        piece = self.__board[start_pos[0]][start_pos[1]]
        end_square = self.__board[end_pos[0]][end_pos[1]]

        self.__remove_piece(start_pos)
        if end_square != EMPTY: # For taking
            if self.__PiecesCls.are_same_color(piece, end_square):
                raise ValueError("Cannot take piece of same color!")

            self.__remove_piece(end_pos)
        self.__add_piece(piece, end_pos)


    def __white_castle(self, rook_start):
        self.__white_can_castle_left = False
        self.__white_can_castle_right = False
        self.__white_castled = True
        
        if rook_start == [7, 0]:
            rook_end = [7, 2]
        elif rook_start == [7, 7]:
            rook_end = [7, 4]

        if self.__board[rook_end[0]][rook_end[1]] != EMPTY:
            raise ValueError("White cannot castle the rooks end position is occupied.")

        self.__move_updater(rook_start, rook_end)


    def __black_castle(self, rook_start):
        self.__black_can_castle_left = False
        self.__black_can_castle_right = False
        self.__black_castled = True

        if rook_start == [0, 0]:
            rook_end = [0, 3]
        elif rook_start == [0, 7]:
            rook_end = [0, 5]

        if self.__board[rook_end[0]][rook_end[1]] != EMPTY:
            raise ValueError("Black cannot castle the rooks end position is occupied.")

        self.__move_updater(rook_start, rook_end)


    def __white_promote(self, pawn_pos):
        self.__remove_piece(pawn_pos)
        self.__add_piece(WHITE_QUEEN, pawn_pos)


    def __black_promote(self, pawn_pos):
        self.__remove_piece(pawn_pos)
        self.__add_piece(BLACK_QUEEN, pawn_pos)


    def __get_pawn_moves(self, pos):
        piece = self.get_piece(pos)
        color = self.__PiecesCls.color_of(piece)

        directions = self.__PiecesCls.directions_of(piece)

        for rDir, cDir in directions:
            move_pos = [pos[0] + rDir, pos[1] + cDir]
            if self.is_on_board(move_pos):
                move_square = self.get_square(move_pos)
                if move_square != EMPTY:
                    if not self.__PiecesCls.are_same_color(piece, move_square):
                        pass





    def __get_knight_moves(self, pos):
        pass


    def __get_king_moves(self, pos):
        pass


    def __get_normal_moves(self, pos):
        pass


    def get_moves(self, pos):
        piece = self.get_piece(pos)
        name = self.__PiecesCls.name_of(piece)

        if name == PAWN:
            return self.__get_pawn_moves(pos)
        elif name == KNIGHT:
            return self.__get_knight_moves(pos)
        elif name == KING:
            return __get_king_moves(pos)
        else:
            return self.__get_normal_moves(pos)


    def move_piece(self, start_pos, end_pos, debug=False):
        
        # Extract the row and column indexes for ease of use
        start_rIdx, start_cIdx = start_pos[0], start_pos[1]
        end_rIdx, end_cIdx = end_pos[0], end_pos[1]

        start_square = self.__board[start_rIdx][start_cIdx]
        end_square = self.__board[end_rIdx][end_cIdx]

        if debug: print("\n=== ChessBoard.make_move({}, {}) ===".format(start_pos, end_pos))

        # ValueError checking, this should be moved to the move finder function for pieces
        if start_square == EMPTY:
            raise ValueError("The piece to move does not exist.")
        elif self.__PiecesCls.color_of(start_square) != self.__current_move:
            raise ValueError("The piece is the wrong color.")
        elif end_square != EMPTY:
            if self.__PiecesCls.color_of(end_square) == self.__current_move:
                raise ValueError("Can not take piece of same color.")

        piece_name = self.__PiecesCls.name_of(start_square)
        piece_color = self.__PiecesCls.color_of(start_square)

        if debug:
            print("\n=== Before move")
            print("Start square:", start_square)
            print("End square:", end_square)
            print("Board at start pos:", self.__board[start_rIdx][start_cIdx])
            print("Board at end pos:", self.__board[end_rIdx][end_cIdx])

        self.__move_updater(start_pos, end_pos)

        # A maximum of one of these logic blocks will run
        # Logic for pawn promotion
        if start_square == WHITE_PAWN and end_rIdx == 0:
            self.__white_promote(end_pos)
        elif start_square == BLACK_PAWN and end_rIdx == 7:
            self.__black_promote(end_pos)
        
        # Logic for white castling
        elif self.can_white_castle:
            if start_square == WHITE_KING: 
                if self.__white_can_castle_left and end_pos == [7, 1]:
                    self.__white_castle([7, 0])
                elif self.__white_can_castle_right and end_pos == [7, 5]:
                    self.__white_castle([7, 7])
                else:
                    self.__white_can_castle_left = False
                    self.__white_can_castle_right = False

            # If one of the white rooks move, black cant castle with that rook 
            elif start_square == WHITE_ROOK:
                if start_pos == [7, 0]:
                    self.__white_can_castle_left = False
                elif start_square == [7, 7]:
                    self.__white_can_castle_right = False

        # Logic for black castling
        elif self.can_black_castle:            
            if start_square == BLACK_KING:
                if self.__black_can_castle_left and end_pos == [0, 2]:
                    self.__black_castle([0, 0])
                elif self._black_castle_right and end_pos == [0, 6]:
                    self.__black_castle([0, 7])
                else:
                    self.__black_can_castle_left = False
                    self.__black_can_castle_right = False

            # If one of the black rooks move, black cant castle with that rook  
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


# This will not run if the file is imported.
if __name__ == "__main__":
    Board = ChessBoard()
    print("Piece names:", ChessPieceHandler().names)
    print("Piece colors:", ChessPieceHandler().colors)

    print(Board)
    print("White pieces:", Board.white_pieces, "\n")
    print("Black pieces:", Board.black_pieces, "\n")
    print("Pieces:", Board.pieces, "\n")

    print(Board.white_piece_value)
    print(Board.black_piece_value)
    print(Board.winner)
    Board.move_piece([7, 1], [5, 1])
    Board.move_piece([7, 2], [5, 2])
    print(Board)
    Board.move_piece([7, 3], [7, 1])
    print(Board)
    Board.move_piece([6, 0], [0, 0])
    print(Board)
