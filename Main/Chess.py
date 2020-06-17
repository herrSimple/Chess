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

# Pieces as dictionaries, might not need these 
WHITE_PAWN = {COLOR: WHITE, NAME: PAWN}
WHITE_KNIGHT = {COLOR: WHITE, NAME: KNIGHT}
WHITE_BISHOP = {COLOR: WHITE, NAME: BISHOP}
WHITE_ROOK = {COLOR: WHITE, NAME: ROOK}
WHITE_QUEEN = {COLOR: WHITE, NAME: QUEEN}
WHITE_KING = {COLOR: WHITE, NAME: KING}

BLACK_PAWN = {COLOR: BLACK, NAME: PAWN}
BLACK_KNIGHT = {COLOR: BLACK, NAME: KNIGHT}
BLACK_BISHOP = {COLOR: BLACK, NAME: BISHOP}
BLACK_ROOK = {COLOR: BLACK, NAME: ROOK}
BLACK_QUEEN = {COLOR: BLACK, NAME: QUEEN}
BLACK_KING = {COLOR: BLACK, NAME: KING}

# Might not need these
WHITE_PIECES = [WHITE_PAWN, WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING]
BLACK_PIECES = [BLACK_PAWN, BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING]

PIECES = [PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING]
PIECE_VALUE = {PAWN: 1, BISHOP: 3, KNIGHT: 3.5, ROOK: 5, QUEEN: 10, KING: 0} # what do we do for the KINGs value? 

# For converting list index and chess boards index
# Todo: is this correct?
NUMBER_TO_LETTER = {n: "hgfedcba"[n] for n in range(8)}
LETTER_TO_NUMBER = {"hgfedcba"[n]: n for n in range(8)}


# Helper function for printing  
def piece_format(piece):
    if piece[NAME] == KNIGHT:
        return piece[COLOR][0] + piece[NAME][1] 
    else: 
        return piece[COLOR][0] + piece[NAME][0] 


class ChessBoard():
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

        # Populates the piece dictionaries from the board
        for rIdx in range(8):
            for cIdx in range(8):
                pos = self.__board[rIdx][cIdx]
                if pos != EMPTY:
                    if pos[COLOR] == WHITE:
                        self.__white_pieces[pos[NAME]] += [[rIdx, cIdx]]
                    elif pos[COLOR] == BLACK:
                        self.__black_pieces[pos[NAME]] += [[rIdx, cIdx]]

        self.__white_castled = False
        self.__black_castled = False

        self.__current_move = WHITE

    # Called when class instance is printed with print()
    def __str__(self):
        print_board = "    0   1   2   3   4   5   6   7\n"
        print_board += "  " + "===="*8 + "==\n"
        for rIdx in range(-8, 0, 1):
            print_board += str(-rIdx) + " |"
            for cIdx in range(8):
                pos = self.square(rIdx, cIdx)
                if pos == EMPTY:
                    print_board += " -- "
                else:
                    print_board += " " + piece_format(pos) + " "
            print_board += "| " + str(8+rIdx) + "\n"

        print_board += "  " + "===="*8 + "==\n"
        print_board += "    A   B   C   D   E   F   G   H\n"    
        return print_board

    # I've used the dcopy function to prevent the accidental modification of data thorough the getter methods
    # I'll add dedicated setter methods that do the appropriate type and error checking. 

    @property
    def board(self):
        return dcopy(self.__board)

    def square(self, rIdx, cIdx):
        return dcopy(self.__board[rIdx][cIdx])
    
    @property
    def white_pieces(self):
        return dcopy(self.__white_pieces)

    @property
    def black_pieces(self):
        return dcopy(self.__black_pieces)

    def find_pieces(self, color, name):
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
        return sum([PIECE_VALUE[piece] * len(pos) for piece, pos in self.__white_pieces.items()])

    @property
    def black_piece_value(self):
        """
        Returns the total value of the black pieces in the dict self.__black_pieces
        """
        return sum([PIECE_VALUE[piece] * len(pos) for piece, pos in self.__black_pieces.items()])

    # This needs to be changed to something that checks for checkmate
    @property
    def winner(self):
        """
        Returns the color of the winner is there is one, else it returns False 
        """
        if not self.find_pieces(WHITE, KING) and not self.find_pieces(BLACK, KING):
            raise Error("Both kings are gone.")
        elif not self.find_pieces(WHITE, KING):
            return BLACK
        elif not self.find_pieces(BLACK, KING):
            return WHITE
        else:
            return False

    def make_move(self, start_idx, end_idx):

        print("=== ChessBoard.make_move({}, {}) === ".format(start_idx, end_idx))
        
        # Extract the row and column indexes for ease of use
        start_rIdx = start_idx[0]
        start_cIdx = start_idx[1]
        end_rIdx = end_idx[0]
        end_cIdx = end_idx[1]

        start_square = self.__board[start_rIdx][start_cIdx]
        end_square = self.__board[end_rIdx][end_cIdx]

        if start_square == EMPTY:
            raise Error("The start square is empty.")
        elif start_square[COLOR] != self.__current_move:
            raise Error("The piece is the wrong color.")

        # Extract piece data
        piece_name = start_square[NAME]
        piece_color = start_square[COLOR]
        
        if end_square != EMPTY:
            if end_square[COLOR] == self.__current_move:
                raise Error("Can not take piece of same color.")
            else:
                # Extract data for piece being taken
                take_name = end_square[NAME]
                take_color = end_square[COLOR]
        else:
            if piece_color == WHITE:
                # Update the pieces dictionary
                list_idx = self.__white_pieces[piece_name].index(start_idx)  # Finds the index of the position
                self.__white_pieces[piece_name][list_idx] = end_idx  # Sets the piece position to the new position
                # Update the board
                self.__board[start_rIdx][start_cIdx] = EMPTY
                self.__board[end_rIdx][end_cIdx] = end_square
            elif piece_color == BLACK:
                pass



if __name__ == "__main__":
    CB = ChessBoard()
    print(CB.square(0, 0))
    print(CB)
    CB.square(0, 0)[COLOR] = WHITE
    print(CB.square(0, 0))
    print(CB)
    print("White pieces:", CB.white_pieces, "\n")
    print("Black pieces:", CB.black_pieces, "\n")
    print(CB.white_piece_value)
    print(CB.black_piece_value)
    print(CB.winner)
    CB.make_move([7, 0], [2, 0])
    print(CB)