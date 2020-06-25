from copy import deepcopy as dcopy
from time import time, sleep
from timeit import timeit
from random import choice

from util.Board import *
from util.Minmax import *


def play_random_game():
    PieceHandler = ChessPieceHandler()
    Board = ChessBoard(PieceHandler)
    turn_num = 1

    print("White pieces:", Board.white_pieces)
    print("Black pieces:", Board.black_pieces)
    print(Board)

    while True:
        print("\n===== TURN {} =====".format(turn_num))
        # Move white
        white_moves = Board.all_white_moves
        #print("White moves:", white_moves, "\n")

        piece = choice(list(white_moves.keys()))
        #print("Piece:", piece)

        piece_pos = piece[1]
        #print("Piece pos:", piece_pos)
        move = choice(white_moves[piece])
        #print("Move:", move)
        Board.move_piece(piece_pos, move)
        print("Board before moves:", Board)
        print("White move: {}, at {} to {}".format(piece[0], piece_pos, move))
        print("White piece value: {}, Black piece value: {}".format(Board.white_piece_value, Board.black_piece_value))
        print("Can white castle: {}".format(Board.can_white_castle))
        print("White can castle, left: {}, right: {}".format(Board.white_can_castle_left, Board.white_can_castle_right))
        
        
        print("\nBoard after white move:", Board)

        if Board.white_castled: break
        
        if Board.has_winner:
            print("===== Winner: {} =====".format(Board.has_winner))
            break

        # Move black
        black_moves = Board.all_black_moves
        #print("White moves:", black_moves, "\n")

        piece = choice(list(black_moves.keys()))
        #print("Piece:", piece)

        piece_pos = piece[1]
        #print("Piece pos:", piece_pos)
        move = choice(black_moves[piece])
        #print("Move:", move)
        Board.move_piece(piece_pos, move)
        print("Black move: {}, at {} to {}".format(piece[0], piece_pos, move))
        print("White piece value: {}, Black piece value: {}".format(Board.white_piece_value, Board.black_piece_value))
        print("Can black castle: {}".format(Board.can_black_castle))
        print("Black can castle, left: {}, right: {}".format(Board.black_can_castle_left, Board.black_can_castle_right))
        if piece == BLACK_ROOK: 
            pass
        
        print("\nBoard after black move:", Board)

        if Board.black_castled: break
        
        if Board.has_winner:
            print("===== Winner: {} =====".format(Board.has_winner))
            break
        turn_num += 1


def tests():
    PieceHandler = ChessPieceHandler()
    Board = ChessBoard(PieceHandler)
    print("Piece names:", ChessPieceHandler().names)
    print("Piece colors:", ChessPieceHandler().colors)

    print(Board)
    print("Moves of white pawn at [6, 0]:", Board.get_moves([6, 0]))
    print("Moves of black pawn at [1, 0]:", Board.get_moves([1, 0]))
    print("Moves of white knight at [7, 1]:", Board.get_moves([7, 1]))
    print("Moves of white knight at [7, 6]:", Board.get_moves([7, 6]))
    print("Moves of black knight at [0, 1]:", Board.get_moves([0, 1]))
    print("Moves of black knight at [0, 6]:", Board.get_moves([0, 6]))
    print("\nWhite pieces:", Board.white_pieces, "\n")
    print("Black pieces:", Board.black_pieces, "\n")
    print("Pieces:", Board.pieces, "\n")

    for piece, positions in Board.pieces.items():
        for pos in positions:
            print("Piece:", piece, "At:", pos, "Moves:", Board.get_moves(pos))

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

    for piece, positions in Board.pieces.items():
        for pos in positions:
            print("Piece:", piece, "At:", pos, "Moves:", Board.get_moves(pos))

    # for _ in range(10000):
    #     for piece, positions in Board.pieces.items():
    #         for pos in positions:
    #             Board.get_moves(pos)

    
# This will not run if the file is imported.
if __name__ == "__main__":
    game_num = 1
    while True:
        print("\n========== GAME {} ==========\n".format(game_num))
        play_random_game()
        game_num += 1
    
