import chess
import numpy as np


def possibleStates(fen):
    ''' This function takes a board's fen as input
        Calculates all legal moves, and calculates fen for boards of all these moves
        Returns a python list of these fens
    '''
    fenList = []
    legalMoves = chess.Board(fen).legal_moves
    tempBoard = chess.Board(fen) 

    for i in legalMoves:
        tempBoard = chess.Board(fen)
        tempBoard.push(i)
        # print (tempBoard, "\n")                     #comment to avoid printing
        fenList.append(tempBoard.fen())

    return fenList






# #driver function
# def driver(): 
#     initialBoard = chess.Board() 

#     print()
#     print(initialBoard, "\n")

#     possibleStates(initialBoard.fen())
#     print(initialBoard.push_san("e4"))
#     print(eval_centerControl(initialBoard.fen()))

# # driver()





# TEST AREA

# print(board.push_san("Nh3"))
# print(board)
# print(board.legal_moves)
# for i in board.legal_moves:
#     print (type(i))