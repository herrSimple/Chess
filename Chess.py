from copy import deepcopy as dcopy

# Constants

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
NORTH_EAST = (-1, 1)
NORTH_WEST = (-1, -1)
SOUTH_EAST = (1, 1)
SOUTH_WEST = (1, -1)

# For knight
UP_LEFT = (-2, -1)
UP_RIGHT = (-2, 1)
DOWN_LEFT = (2, -1)
DOWN_RIGHT = (2, 1)
LEFT_UP = (-1, -2)
LEFT_DOWN = (1, -2)
RIGHT_UP = (-1, 2)
RIGHT_DOWN = (1, 2)

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
WHITE_PAWN = "WP"
WHITE_KNIGHT = "WN"
WHITE_BISHOP = "WB"
WHITE_ROOK = "WR"
WHITE_QUEEN = "WQ"
WHITE_KING = "WK"

BLACK_PAWN = "BP"
BLACK_KNIGHT = "BN"
BLACK_BISHOP = "BB"
BLACK_ROOK = "BR"
BLACK_QUEEN = "BQ"
BLACK_KING = "BK"

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

PIECE_CREATE = {
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

PIECE_DIRECTIONS = {
    PAWN: {
        WHITE: (NORTH, NORTH_EAST, NORTH_WEST), 
        BLACK: (SOUTH, SOUTH_WEST, SOUTH_EAST)
    },
    KNIGHT: (UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT, LEFT_UP, LEFT_DOWN, RIGHT_UP, RIGHT_DOWN),
    BISHOP: (NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST),
    ROOK:   (NORTH, SOUTH, WEST, EAST),
    QUEEN:  (NORTH, SOUTH, WEST, EAST, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST),
    KING:   (NORTH, SOUTH, WEST, EAST, NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST)
}

PIECE_VALUES = {PAWN: 1, BISHOP: 3, KNIGHT: 3.5, ROOK: 5, QUEEN: 10, KING: 0} # what do we do for the KINGs value? 

PIECE_COLORS = (WHITE, BLACK)
PIECE_NAMES = (PAWN, ROOK, KNIGHT, BISHOP, QUEEN, KING)
PIECE_ALL = (
    WHITE_PAWN, WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING,
    BLACK_PAWN, BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING
)
PIECE_WHITE = (WHITE_PAWN, WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING)
PIECE_BLACK = (BLACK_PAWN, BLACK_ROOK, BLACK_KNIGHT, BLACK_BISHOP, BLACK_QUEEN, BLACK_KING)

RF_TO_IDX = {"abcdefgh"[y] + "87654321"[x]: (x, y) for y in range(8) for x in range(8)}
IDX_TO_RF = {value: key for key, value in RF_TO_IDX.items()}

def convert_move_format(move):
    if isinstance(move, str):
        return (RF_TO_IDX[move[:2]], RF_TO_IDX[move[2:]])
    else:
        return IDX_TO_RF[move[0]] + IDX_TO_RF[move[1]]   


def color_of(piece):
    """
    Returns the color of the piece.
    """
    return PIECE_DATA[piece][COLOR]


def name_of(piece):
    """
    Returns the name of the piece.
    """
    return PIECE_DATA[piece][NAME]


def data_of(piece):
    """
    Returns a dictionary containing the color and name of the piece.
    """
    return PIECE_DATA[piece]


def create(color, name):
    """
    Returns a piece.   
    """
    return PIECE_CREATE[color][name]


def value_of(piece):
    """
    Returns the value of the piece.
    """
    return  PIECE_VALUES[name_of(piece)]


def directions_of(piece):
    """
    Returns the movement directions of piece.
    """
    color = color_of(piece)
    name = name_of(piece)
    if name == PAWN:
        return PIECE_DIRECTIONS[name][color]
    else:
        return PIECE_DIRECTIONS[name]


def are_same_color(piece1, piece2):
    """
    Returns True is piece1 and piece2 are the sale color, otherwise False.
    """
    return color_of(piece1) == color_of(piece2)


def format(piece):
    return piece   


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
            [WHITE_ROOK, WHITE_KNIGHT, WHITE_BISHOP, WHITE_QUEEN, WHITE_KING, WHITE_BISHOP, WHITE_KNIGHT, WHITE_ROOK]
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
                    self.__positions[square] += [(rIdx, cIdx)]

        # True if the color can still castle on that side
        self.__can_white_castle_left = True
        self.__can_white_castle_right = True

        self.__can_black_castle_left = True
        self.__can_black_castle_right = True

        # True of the color has castled
        self.__has_white_castled = False
        self.__has_black_castled = False

        # The next color to move
        self.__color_to_move = WHITE

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
                    print_board += " " + format(pos) + " "
            print_board += "| " + str(8+rIdx) + "\n"

        print_board += "  " + "===="*8 + "==\n"
        print_board += "    A   B   C   D   E   F   G   H\n"    
        return print_board

    # I've used the dcopy function to prevent the accidental modification of data thorough the getter methods
    # I'll add dedicated setter methods that do the appropriate type and error checking.

    def clone(self, move=None):
        board = dcopy(self)
        if move is not None:
            board.make_move(move)
        return board

    @property
    def board(self):
        return self.__board

    @property
    def pieces(self):
        return self.__positions

    @property
    def color_to_move(self):
        return self.__color_to_move

    @property
    def can_white_castle_left(self):
        return self.__can_white_castle_left

    @property
    def can_white_castle_right(self):
        return self.__can_white_castle_right

    @property
    def can_black_castle_left(self):
        return self.__can_black_castle_left

    @property
    def can_white_castle_right(self):
        return self.__can_white_castle_right
    
    # Make getter and setter methods for the square
    def get_square(self, *args):
        if len(args) == 1:
            return self.__board[args[0][0]][args[0][1]]
        elif len(args) == 2:
            return self.__board[args[0]][args[1]]

    @property
    def white_pieces(self):
        # Works on self.__positions
        return {piece: self.__positions[piece] for piece in PIECE_WHITE}

    @property
    def black_pieces(self):
        return {piece: self.__positions[piece] for piece in PIECE_BLACK}

    @property
    def can_white_castle(self):
        return (not self.__has_white_castled) and (self.__can_white_castle_left or self.__can_white_castle_right)
    
    @property
    def white_castled(self):
        return self.__has_white_castled

    @property
    def white_can_castle_left(self):
        return self.__can_white_castle_left

    @property
    def white_can_castle_right(self):
        return self.__can_white_castle_right
    
    @property
    def can_black_castle(self):
        return (not self.__has_black_castled) and (self.__can_black_castle_left or self.__can_black_castle_right)
    
    @property
    def black_castled(self):
        return self.__has_black_castled

    @property
    def black_can_castle_left(self):
        return self.__can_black_castle_left

    @property
    def black_can_castle_right(self):
        return self.__can_black_castle_right

    @property
    def white_piece_value(self):
        """
        Returns the total value of the white pieces in the dict self.__white_pieces
        """
        return sum([value_of(piece) * len(self.__positions[piece]) for piece in PIECE_WHITE])

    @property
    def black_piece_value(self):
        """
        Returns the total value of the black pieces in the dict self.__black_pieces
        """
        return sum([value_of(piece) * len(self.__positions[piece]) for piece in PIECE_BLACK])

    @property
    def board_value(self):
        value = 0
        winner = self.has_winner

        if winner == WHITE:
            value += float("inf")
        elif winner == BLACK:
            value -= float("inf")

        if self.black_castled:
            value -= 5
        if self.white_castled:
            value += 5

        value += self.white_piece_value
        value -= self.black_piece_value 
        
        return value 

    @property
    def has_winner(self):
        """
        Returns the color of the winner is there is one, otherwise False.
        """
        if not self.pieces[WHITE_KING] and not self.pieces[BLACK_KING]:
            return False  #
        elif not self.pieces[WHITE_KING]:
            return BLACK
        elif not self.pieces[BLACK_KING]:
            return WHITE
        else:
            return False

    def find_position(self, piece):
        """
        Returns the list of positions that the piece occupies.
        """
        return self.__positions[piece]

    def get_piece(self, pos):  # Use self.get_square instead
        """
        Returns a tuple (piece, name, color) for the square at pos. Use get_square unless you are sure that a piece at pos.
        """
        piece = self.__board[pos[0]][pos[1]]

        if piece == EMPTY:
            raise ValueError("The square is empty")

        return piece  

    def is_on_board(self, pos):
        # print("In is on board\n", "Pos:", pos, "On board:", (7 >= pos[0] >= 0 and 7 >= pos[1] >= 0))
        return 7 >= pos[0] >= 0 and 7 >= pos[1] >= 0

    def is_empty(self, *positions):
        for pos in positions:
            if self.get_square(pos) != EMPTY:
                return False
        return True

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
            if are_same_color(piece, end_square):
                raise ValueError("Cannot take piece of same color!")

            self.__remove_piece(end_pos)
        self.__add_piece(piece, end_pos)

    def __white_castle(self, rook_start):
        self.__can_white_castle_left = False
        self.__can_white_castle_right = False
        self.__has_white_castled = True
        
        if rook_start == (7, 0):
            rook_end = (7, 3)
        elif rook_start == (7, 7):
            rook_end = (7, 5)

        if not self.is_empty((rook_end[0], rook_end[1])):
            raise ValueError("White cannot castle the rooks end position is occupied.")

        self.__move_updater(rook_start, rook_end)

    def __black_castle(self, rook_start):
        self.__can_black_castle_left = False
        self.__can_black_castle_right = False
        self.__has_black_castled = True

        if rook_start == (0, 0):
            rook_end = (0, 3)
        elif rook_start == (0, 7):
            rook_end = (0, 5)

        if not self.is_empty((rook_end[0], rook_end[1])):
            raise ValueError("Black cannot castle the rooks end position is occupied.")

        self.__move_updater(rook_start, rook_end)

    def __white_promote(self, pawn_pos):
        self.__remove_piece(pawn_pos)
        self.__add_piece(WHITE_QUEEN, pawn_pos)

    def __black_promote(self, pawn_pos):
        self.__remove_piece(pawn_pos)
        self.__add_piece(BLACK_QUEEN, pawn_pos)

    def __get_pawn_moves(self, pos):
        """
        Looks like it is working
        """
        piece = self.get_piece(pos)
        color = color_of(piece)
        moves = []
        directions = directions_of(piece)

        # Logic for pawns first move
        # Is the white pawn on its starting row
        if color == WHITE and pos[0] == 6:  
            if self.is_empty((pos[0] - 1, pos[1]), (pos[0] - 2, pos[1])):
                moves.append((pos, (pos[0] - 2, pos[1])))
        # Is the black pawn on its starting row
        elif color == BLACK and pos[0] == 1:  
            if self.is_empty((pos[0] + 1, pos[1]), (pos[0] + 2, pos[1])):
                moves.append((pos, (pos[0] + 2, pos[1])))

        # Iterate of the pieces movement directions 
        for direct in directions:
            rDir, cDir = direct  # Unpack the row and col directions
            move_pos = (pos[0] + rDir, pos[1] + cDir)
            # Is move_pos a valid pos on the board
            if self.is_on_board(move_pos):
                move_square = self.get_square(move_pos)

                # If the pawn is moving forward it can't take
                if direct == NORTH or direct == SOUTH:
                    if move_square == EMPTY:
                        moves.append((pos, move_pos))

                # Pawn can take to left or right
                else:
                    if move_square != EMPTY:
                        if not are_same_color(piece, move_square):
                            moves.append((pos, move_pos))
        return moves

    def __get_knight_moves(self, pos):
        """
        Seems to be working
        """
        piece = self.get_piece(pos)
        color = color_of(piece)
        moves = []
        directions = directions_of(piece)

        for offset in directions:
            rOffset, cOffset = offset
            move_pos = (pos[0] + rOffset, pos[1] + cOffset)

            if self.is_on_board(move_pos):
                move_square = self.get_square(move_pos)
                if move_square == EMPTY:
                    moves.append((pos, move_pos))
                else:
                    if not are_same_color(piece, move_square):
                        moves.append((pos, move_pos))

        return moves

    def __get_king_moves(self, pos):
        piece = self.get_piece(pos)
        color = color_of(piece)
        moves = []
        directions = directions_of(piece)
        # Logic for castling, check position, maybe use propertys for the if-checking
        if color == WHITE and pos == (7, 4):
            if self.__can_white_castle_left:
                if self.is_empty((7, 1), (7, 2), (7, 3)):
                    moves.append((pos, (7, 2)))

            if self.__can_white_castle_right:
                if self.is_empty((7, 5), (7, 6)):
                    moves.append((pos, (7, 6)))

        elif color == BLACK and pos == (0, 4):
            if self.__can_black_castle_left:
                if self.is_empty((0, 1), (0, 2), (0, 4)):
                    moves.append((pos, (0, 2)))

            if self.__can_black_castle_right:
                if self.is_empty((0, 5), (0, 6)):
                    moves.append((pos, (0, 6)))

        for direct in directions:
            rDir, cDir = direct
            move_pos = (pos[0] + rDir, pos[1] + cDir)

            if self.is_on_board(move_pos):
                move_square = self.get_square(move_pos)
                if move_square == EMPTY:
                    moves.append((pos, move_pos))
                else:
                    if not are_same_color(piece, move_square):
                        moves.append((pos, move_pos))

        return moves

    def __get_normal_moves(self, pos):
        piece = self.get_piece(pos)
        color = color_of(piece)
        moves = []
        directions = directions_of(piece)

        for direct in directions:
            rDir, cDir = direct
            move_pos = (pos[0] + rDir, pos[1] + cDir)
            while True:
                if self.is_on_board(move_pos):
                    move_square = self.get_square(move_pos)
                    if move_square == EMPTY:
                        moves.append((pos, move_pos))
                    else:
                        if not are_same_color(piece, move_square):
                            moves.append((pos, move_pos))
                            break
                        else:
                            break
                else:
                    break

                move_pos = (move_pos[0] + rDir, move_pos[1] + cDir)

        return moves
        
    def get_piece_moves(self, pos):
        name = name_of(self.get_piece(pos))

        if name == PAWN:
            return self.__get_pawn_moves(pos)
        elif name == KNIGHT:
            return self.__get_knight_moves(pos)
        elif name == KING:
            return self.__get_king_moves(pos)
        else:
            return self.__get_normal_moves(pos)

    @property
    def white_moves(self):
        moves = []
        for piece in self.white_pieces:
            for pos in self.white_pieces[piece]:
                if piece_moves := self.get_piece_moves(pos):
                    moves.extend(piece_moves)
        return moves

    @property
    def black_moves(self):
        moves = []
        for piece in self.black_pieces:
            for pos in self.black_pieces[piece]:
                if piece_moves := self.get_piece_moves(pos):
                    moves.extend(piece_moves)
        return moves

    @property
    def moves(self):
        if self.color_to_move == WHITE:
            return self.white_moves
        else:
            return self.black_moves
    
    def next_color(self):
        if self.__color_to_move == WHITE:
            self.__color_to_move = BLACK
        elif self.__color_to_move == BLACK:
            self.__color_to_move = WHITE

    def make_move(self, move, debug=False):
        # Extract the row and column indexes for ease of use
        start_pos, end_pos = move
        start_rIdx = start_pos[0] 
        start_cIdx = start_pos[1]
        end_rIdx = end_pos[0]
        end_cIdx = end_pos[1]

        start_square = self.get_square(start_pos)
        end_square = self.get_square(end_pos)

        if debug: print("\n=== ChessBoard.make_move({}, {}) ===".format(start_pos, end_pos))

        # ValueError checking, this should be moved to the move finder function for pieces
        if start_square == EMPTY:
            raise ValueError("The piece to move does not exist.")
        elif color_of(start_square) != self.__color_to_move:
            raise ValueError("The piece is the wrong color.")
        elif end_square != EMPTY:
            if color_of(end_square) == self.__color_to_move:
                raise ValueError("Can not take piece of same color.")

        piece_name = name_of(start_square)
        piece_color = color_of(start_square)

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
        elif start_square == WHITE_KING:
            if self.__can_white_castle_left and end_pos == (7, 2):
                self.__white_castle((7, 0))
            elif self.__can_white_castle_right and end_pos == (7, 6):
                self.__white_castle((7, 7))
            else:
                self.__can_white_castle_left = False
                self.__can_white_castle_right = False

        # If one of the white rooks move, white cant castle with that rook 
        elif start_square == WHITE_ROOK:
            if self.__can_white_castle_left and start_pos == (7, 0):
                self.__can_white_castle_left = False
            elif self.__can_white_castle_right and start_square == (7, 7):
                self.__can_white_castle_right = False

        # Logic for black castling
        elif start_square == BLACK_KING:        
            if self.__can_black_castle_left and end_pos == (0, 2):
                self.__black_castle((0, 0))
            elif self.__can_black_castle_right and end_pos == (0, 6):
                self.__black_castle((0, 7))
            else:
                self.__can_black_castle_left = False
                self.__can_black_castle_right = False

        # If one of the black rooks move, black cant castle with that rook  
        elif start_square == BLACK_ROOK:
            if self.__can_black_castle_left and start_pos == (0, 0):
                self.__can_black_castle_left = False
            elif self.__can_black_castle_right and start_pos == (0, 7):
                self.__can_black_castle_right = False

        # This must be called after the move is made
        self.next_color()

        if debug:
            print("\n=== After move")
            print("Start square:", start_square)
            print("End square:", end_square)
            print("Board at start pos:", self.__board[start_rIdx][start_cIdx])
            print("Board at end pos:", self.__board[end_rIdx][end_cIdx])


class BoardNode():
    def __init__(self, board, key=None):
        self.__payload = board
        self.__parent = None
        self.__key = key
        self.__children = []

    @property
    def payload(self):
        return self.__payload

    @property
    def key(self):
        return self.__key
    
    @property
    def children(self):
        return self.__children

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, node):
        self.__parent = node

    def add_child(self, node):
        self.__children.append(node)


class MinmaxSearchAi():
    def __init__(self, root_board):
        self.__root = BoardNode(root_board)
        self.__last_move = None

    @property
    def root(self):
        return self.__root

    @property
    def last_move(self):
        return self.__last_move
    
    def move(self, level):
        move = self.search(level)
        self.__last_move = move
        self.root.payload.make_move(move)

    def search(self, level):
        moves = self.get_current_moves(self.root)
        best_move_val = None
        # minmax_values = []

        for move in moves: 
            child = BoardNode(self.root.payload.clone(move))
            # self.root.add_child(child)
            
            minmax_move_val = self.get_minmax_value(child, level-1)

            if best_move_val is None:
                best_move_val = minmax_move_val

            if self.root.payload.color_to_move == WHITE:
                if minmax_move_val >= best_move_val:
                    best_move = move
                    best_move_val = minmax_move_val
            else:
                if minmax_move_val <= best_move_val:
                    best_move = move
                    best_move_val = minmax_move_val

            # minmax_values.append((move, minmax_move_val))
        # return minmax_values
        return best_move

    def get_minmax_value(self, node, level):
        # print(f"{'    '*(3-level)}--- get_minmax_value({node}, {level}) -----------------------")
        if node.payload.has_winner or level == 0:
            # print("In get_minmax_value: board value =", node.payload.board_value)
            minmax_val = node.payload.board_value
        else:
            # print()
            moves = self.get_current_moves(node)
            minmax_list = []

            for move in moves:
                # print(f"{'    '*(3-level)}Move: {move}")
                # print("Move:", move)
                child = BoardNode(node.payload.clone(move))
                # node.add_child(child)
                value = self.get_minmax_value(child, level-1)
                minmax_list.append(value)
            # print(f"{'    '*(3-level)}--- color_to_move = {node.payload.color_to_move}")
            if node.payload.color_to_move == WHITE:
                minmax_val = max(minmax_list)
            else:
                minmax_val = min(minmax_list)
        # print(f"{'    '*(3-level)}--- minmax_val = {minmax_val}\n")
        return minmax_val
        
    def get_current_moves(self, board_node):
        return board_node.payload.moves

    def color_to_move(self, board_node):
        return board_node.payload.color_to_move


class HumanPlayer():
    def __init__(self, board):
        self.__board = board
        self.__last_move = None

    @property
    def board(self):
        return self.__board

    @property
    def last_move(self):
        return self.__last_move
    
    def move(self):
        move = self.get_move()
        self.__last_move = move
        self.board.make_move(move)

    def get_move(self):
        possible_moves = self.board.moves
        while True:
            try:
                move_str = str(input("Enter your move, 'all' to see all possible moves or 'board' to see the board: ")).strip()
                if move_str == "all":
                    formatted_moves = [convert_move_format(move) for move in possible_moves]
                    print(f"All available moves: {formatted_moves}")
                elif move_str == "board":
                    print(self.board)
                else:
                    move = convert_move_format(move_str)
                    if move in possible_moves:
                        break
                    else:
                        print(f"The move {move_str} is invalid, please try again!")
            except:
                print("Unknown input, please try again!")

        return move


def tests():
    board = ChessBoard()

    print(f"is empty: {board.is_empty((3, 0), (3, 1), (3, 2), (0, 3))}\n")

    print("Piece names:", PIECE_NAMES)
    print("Piece colors:", PIECE_COLORS)

    print(board)

    print(f"can white castle: {board.can_white_castle}")
    print(f"can white castle left: {board.can_white_castle_left}")
    print(f"can white castle right: {board.can_white_castle_right}")

    board.make_move(convert_move_format('e2e4'))
    board.make_move(convert_move_format('e7e5'))

    board.make_move(convert_move_format('f1d3'))
    board.make_move(convert_move_format('f8d6'))

    board.make_move(convert_move_format('g1f3'))
    board.make_move(convert_move_format('g8f6'))
    print(board)
    print(f"is empty: {board.is_empty((7, 6), (7, 5))}")

    print(f"can white castle: {board.can_white_castle}")
    print(f"can white castle left: {board.can_white_castle_left}")
    print(f"can white castle right: {board.can_white_castle_right}")
    print(f"white king moves: {board.get_piece_moves((7, 4))}")

    moves = [convert_move_format(move) for move in board.moves]
    print(f"White moves: {moves}")
    board.make_move(convert_move_format('e1g1'))
    print(board)
    moves = [convert_move_format(move) for move in board.moves]
    print(f"Black moves: {moves}")
    board.make_move(convert_move_format('e8g8'))
    print(board)
    # print("Moves of white pawn at [6, 0]:", board.get_piece_moves([6, 0]))
    # print("Moves of black pawn at [1, 0]:", board.get_piece_moves([1, 0]))
    # print("Moves of white knight at [7, 1]:", board.get_piece_moves([7, 1]))
    # print("Moves of white knight at [7, 6]:", board.get_piece_moves([7, 6]))
    # print("Moves of black knight at [0, 1]:", board.get_piece_moves([0, 1]))
    # print("Moves of black knight at [0, 6]:", board.get_piece_moves([0, 6]))
    # print("\nWhite pieces:", board.white_pieces, "\n")
    # print("Black pieces:", board.black_pieces, "\n")
    # print("Pieces:", board.pieces, "\n")

    # for piece, positions in board.pieces.items():
    #     for pos in positions:
    #         print("Piece:", piece, "At:", pos, "Moves:", board.get_piece_moves(pos))



    # print(board.white_piece_value)
    # print(board.black_piece_value)
    # print(board.has_winner)
    # # board.make_move(((7, 1), (5, 1)))
    # #board.make_move((7, 2), (5, 2))
    # print(board)
    # #board.make_move((7, 3), (7, 1))
    # print(board)
    # #board.make_move((6, 0), (0, 0))
    # print(board)

    # for piece, positions in board.pieces.items():
    #     for pos in positions:
    #         print("Piece:", piece, "At:", pos, "Moves:", board.get_piece_moves(pos))

    # board1 = board.clone( ((0, 1), (2, 2)) )
    # print("board1:", board1, board1.pieces)
    # print("board:", board, board.pieces)

    # for _ in range(10000):
    #     for piece, positions in board.pieces.items():
    #         for pos in positions:
    #             board.get_piece_moves(pos)

    # print("RF_TO_IDX:", RF_TO_IDX)
    # print("IDX_TORF:", IDX_TO_RF)

def minmax_tests():
    board = ChessBoard()
    board.make_move((6, 3), (4, 3))
    board.make_move((1, 3), (3, 3))

    board.make_move((7, 6), (5, 5))
    board.make_move((0, 2), (2, 4))

    board.make_move((6, 4), (4, 4))
    board.make_move((2, 4), (4, 6))
    #White to move
    print(board)
    minmax = MinmaxSearchAi(board)
    print("best white moves:", minmax.search(3)) 

    # print("Number of boards:", num)

def human_tests():
    board = ChessBoard()
    player = HumanPlayer(board)
    player.move()

def play_game():
    board = ChessBoard()
    white = HumanPlayer(board)
    black = MinmaxSearchAi(board)

    while True:
        print(board)
        print(f"\n--- WHITE to move ------------------------------------------------------------")
        white.move()
        print(f"\nWhites move: {convert_move_format(white.last_move)}")
        if winner := board.has_winner:
            print(f"=== {winner} has won! ============================================================")
            break
        print(f"\n--- BLACK is playing ------------------------------------------------------------")
        black.move(level=3)
        print(f"\nBlacks move: {convert_move_format(black.last_move)}")
        if winner := board.has_winner:
            print(f"--- {winner} has won! ============================================================")
            break


if __name__ == "__main__":
    # tests()
    # minmax_tests()
    play_game()

