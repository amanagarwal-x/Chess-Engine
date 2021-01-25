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

def eval_centerControl(fen):
        
    ''' Evaluation function to return score for centre square control
        Return 1 if one out of four centre squares are controlled/attacked
        Return 2 if two out of four centre squares are controlled/attacked
        ...
    '''
    centerSquares = [chess.E4, chess.E5, chess.D4, chess.D5]
    score = 0

    for i in centerSquares:
        score = score + chess.Board(fen).is_attacked_by(chess.WHITE, i)
     
    # if score > 1:
    #     print(chess.Board(fen), '\n')
    return score


#driver function
def driver(): 
    initialBoard = chess.Board() 

    print()
    print(initialBoard, "\n")

    possibleStates(initialBoard.fen())
    print(initialBoard.push_san("e4"))
    print(eval_centerControl(initialBoard.fen()))

# driver()





# TEST AREA

# print(board.push_san("Nh3"))
# print(board)
# print(board.legal_moves)
# for i in board.legal_moves:
#     print (type(i))