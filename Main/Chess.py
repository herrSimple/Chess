from copy import deepcopy as dcopy

# Constants 
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
PIECE_NAMES = [PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING]
WHITE_PIECES = [WHITE_PAWN, WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING]
BLACK_PIECES = [BLACK_PAWN, BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING]

# Piece data
PIECE_DATA = {
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

# Piece creator
CREATE_PIECE = {
    WHITE: {
        PAWN: WHITE_PAWN, 
        ROOK: WHITE_ROOK, 
        KNIGHT: WHITE_KNIGHT, 
        BISHOP: WHITE_BISHOP, 
        QUEEN: WHITE_QUEEN, 
        KING: WHITE_KING
    }, 

    BLACK: {
        PAWN: BLACK_PAWN, 
        ROOK: BLACK_ROOK, 
        KNIGHT: BLACK_KNIGHT, 
        BISHOP: BLACK_BISHOP, 
        QUEEN: BLACK_QUEEN, 
        KING: BLACK_KING
    }
}

PIECE_VALUE = {PAWN: 1, BISHOP: 3, KNIGHT: 3.5, ROOK: 5, QUEEN: 10, KING: 0} # what do we do for the KINGs value? 

# For converting list index and chess boards index
# Todo: is this correct?
NUMBER_TO_LETTER = {n: "hgfedcba"[n] for n in range(8)}
LETTER_TO_NUMBER = {"hgfedcba"[n]: n for n in range(8)}


class Piece():
    """
    This class is just a namespace for methods relating to chess pieces.

    For example to get a pieces color use: Piece.color(piece)   
    """
    # Chess piece helper functions
    @staticmethod
    def color(piece):
        return PIECE_DATA[piece][COLOR]


    @staticmethod
    def name(piece):
        return PIECE_DATA[piece][NAME]


    @staticmethod
    def data(piece):
        return 


    @staticmethod
    def create(color, name):
        return CREATE_PIECE[color][name]


    @staticmethod
    def value(piece):
        return PIECE_VALUE[piece]


    @staticmethod
    def piece_format(piece):  
        if Piece.name(piece) == KNIGHT:
            return Piece.color(piece)[0] + Piece.name(piece)[1] 
        else: 
            return Piece.color(piece)[0] + Piece.name(piece)[0]


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

        # Piece dictionaries
        self.__white_pieces = {PAWN: [], KNIGHT: [], BISHOP: [], ROOK: [], QUEEN: [], KING: []} 
        self.__black_pieces = {PAWN: [], KNIGHT: [], BISHOP: [], ROOK: [], QUEEN: [], KING: []}

        # Populates the piece dictionaries using the board
        for rIdx in range(8):
            for cIdx in range(8):
                pos = self.__board[rIdx][cIdx]
                if pos != EMPTY:
                    if Piece.color(pos) == WHITE:
                        self.__white_pieces[Piece.name(pos)] += [[rIdx, cIdx]]
                    elif Piece.color(pos) == BLACK:
                        self.__black_pieces[Piece.name(pos)] += [[rIdx, cIdx]]

        # True if the color can still castle on that side
        self.__white_castle_left = True
        self.__white_castle_right = True
        self.__black_castle_left = True
        self.__black_castle_right = True

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
                    print_board += " " + Piece.piece_format(pos) + " "
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
        return dcopy(self.__white_pieces)


    @property
    def black_pieces(self):
        return dcopy(self.__black_pieces)


    def find_position(self, color, name):
        """
        Returns a list of positions for the pieces with COLOR: color and NAME: name
        """
        if color == WHITE:
            return dcopy(self.__white_pieces[name])
        elif color == BLACK:
            return dcopy(self.__black_pieces[name])


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
        return sum([Piece.value(piece) * len(pos) for piece, pos in self.__white_pieces.items()])


    @property
    def black_piece_value(self):
        """
        Returns the total value of the black pieces in the dict self.__black_pieces
        """
        return sum([Piece.value(piece) * len(pos) for piece, pos in self.__black_pieces.items()])


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


    def make_move(self, start_pos, end_pos, debug=False):
        
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
        elif Piece.color(start_square) != self.__current_move:
            raise ValueError("The piece is the wrong color.")
        elif end_square != EMPTY:
            if Piece.color(end_square) == self.__current_move:
                raise ValueError("Can not take piece of same color.")

        piece_name = Piece.name(start_square)
        piece_color = Piece.color(start_square)

        if debug:
            print("\n=== Before move")
            print("Start square:", start_square)
            print("End square:", end_square)
            print("Board at start pos:", self.__board[start_rIdx][start_cIdx])
            print("Board at end pos:", self.__board[end_rIdx][end_cIdx])

        self.__update_board(piece_color, piece_name, start_rIdx, start_cIdx, end_rIdx, end_cIdx)

        # Logic for pawn promotion
        if start_square == WHITE_PAWN and end_rIdx == 0:
            self.__white_promote(end_pos)
        elif start_square == BLACK_PAWN and end_rIdx == 7:
            self.__black_promote(end_pos)
        
        # Logic for castling
        elif not self.__white_castled and (self.__white_castle_left or self.__white_castle_right):
            if start_square == WHITE_KING: 
                if self.__white_castle_left and end_pos == [7, 1]:
                    self.__white_castle([7, 0])
                elif self.__white_castle_right and end_pos == [7, 5]:
                    self.__white_castle([7, 7])
                else:
                    self.__white_castle_left = False
                    self.__white_castle_right = False

            elif start_square == WHITE_ROOK:
                if start_pos == [7, 0]:
                    self.__white_castle_left = False
                elif start_square == [7, 7]:
                    self.__white_castle_right = False

        elif not self.__black_castled and (self.__black_castle_left or self.__black_castle_right):            
            if start_square == BLACK_KING:
                if self.__black_castle_left and end_pos == [0, 2]:
                    self.__black_castle([0, 0])
                elif self._black_castle_right and end_pos == [0, 6]:
                    self.__black_castle([0, 7])
                else:
                    self.__black_castle_left = False
                    self.__black_castle_right = False

            elif start_square == BLACK_ROOK:
                if start_pos == [0, 0]:
                    self.__black_castle_left = False
                elif start_pos == [0, 7]:
                    self.__black_castle_right = False

        if debug:
            print("\n=== After move")
            print("Start square:", start_square)
            print("End square:", end_square)
            print("Board at start pos:", self.__board[start_rIdx][start_cIdx])
            print("Board at end pos:", self.__board[end_rIdx][end_cIdx])


    def __update_board(self, piece_color, piece_name, start_rIdx, start_cIdx, end_rIdx, end_cIdx):
        
        end_square = self.__board[end_rIdx][end_cIdx]

        if piece_color == WHITE:
            # Update the piece dictionary
            idx = self.__white_pieces[piece_name].index([start_rIdx, start_cIdx])  # Finds the index of the position
            self.__white_pieces[piece_name][idx] = [end_rIdx, end_cIdx]  # Sets the pieces position to the end position

            # Logic for taking
            if end_square != EMPTY:
                take_name = Piece.name(end_square)
                idx = self.__black_pieces[take_name].index([end_rIdx, end_cIdx])  # Finds the index of the position of the taken piece
                del self.__black_pieces[take_name][idx]  # Removes the position of the taken piece
        
        elif piece_color == BLACK:
            # Update the piece dictionary
            idx = self.__black_pieces[piece_name].index([start_rIdx, start_cIdx])  # Finds the index of the position
            self.__black_pieces[piece_name][idx] = [end_rIdx, end_cIdx]  # Sets the pieces position to the end position

            # Logic for taking
            if end_square != EMPTY:
                take_name = Piece.name(end_square)
                idx = self.__white_pieces[take_name].index([end_rIdx, end_cIdx])  # Finds the index of the position of the taken piece
                del self.__white_pieces[take_name][idx]  # Removes the position of the taken piece

        # Update the board
        self.__board[start_rIdx][start_cIdx] = EMPTY
        self.__board[end_rIdx][end_cIdx] = Piece.create(piece_color, piece_name)


    def __white_castle(self, rook_start):
        self.__white_castle_left = False
        self.__white_castle_right = False
        self.__white_castled = True
        
        if rook_start == [7, 0]:
            rook_end = [7, 2]
        elif rook_start == [7, 7]:
            rook_end = [7, 4]

        if self.__board[rook_end[0]][rook_end[1]] != EMPTY:
            raise ValueError("White castling error: the rooks end position is occupied.")

        self.__update_board(WHITE, ROOK, rook_start[0], rook_start[1], rook_end[0], rook_end[1])


    def __black_castle(self, rook_start):
        self.__black_castle_left = False
        self.__black_castle_right = False
        self.__black_castled = True

        if rook_start == [0, 0]:
            rook_end = [0, 3]
        elif rook_start == [0, 7]:
            rook_end = [0, 5]

        if self.__board[rook_end[0]][rook_end[1]] != EMPTY:
            raise ValueError("Black castling error: the rooks end position is occupied.")

        self.__update_board(BLACK, ROOK, rook_start[0], rook_start[1], rook_end[0], rook_end[1])


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
    print(CB.white_piece_value)
    print(CB.black_piece_value)
    print(CB.winner)
    CB.make_move([7, 1], [5, 1])
    CB.make_move([7, 2], [5, 2])
    print(CB)
    CB.make_move([7, 3], [7, 1])
    print(CB)
