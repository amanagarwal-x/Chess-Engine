import chess

# from main import *
from Aman.main import *

initialBoard = chess.Board() 
print()
print(initialBoard, "\n")


while(1):
    print("Computer's Move:")
    initialBoard = chess.Board(possibleStates(initialBoard.fen())[0])
    print()
    print(initialBoard, "\n")

    print("Possible Moves: ", initialBoard.legal_moves)
    blackMove = input("Enter your move: ")
    initialBoard.push_san(blackMove)
    print()
    print(initialBoard, "\n")

