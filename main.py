import chess
import numpy as np

def possibleStates(fen):
    fenList = []
    legalMoves = chess.Board(fen).legal_moves
    tempBoard = chess.Board(fen) 

    for i in legalMoves:
        tempBoard = chess.Board(fen)
        tempBoard.push(i)
        print (tempBoard, "\n")                     #comment to avoid printing
        fenList.append(tempBoard.fen())

    return fenList

def main(): 
    initialBoard = chess.Board() 

    print()
    print(initialBoard, "\n")

    possibleStates(initialBoard.fen())

main()





# TEST AREA

# print(board.push_san("Nh3"))
# print(board)
# print(board.legal_moves)
# for i in board.legal_moves:
#     print (type(i))