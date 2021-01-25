import chess

# from main import *
from Aman.main import *
from Mihir.mihir import *

initialBoard = chess.Board() 
print()
print(initialBoard, "\n")


while(1):
    print("Computer's Move:")

    maxScore = float('-inf')
    nextFen = ""
    for i in possibleStates(initialBoard.fen()): 
        # print(eval_centerControl(i), materialcount(i))
        # eval_centerControl(i)
        score = eval_centerControl(i) + materialcount(i)
        
        if score >= maxScore:
            nextFen = i

   
    initialBoard = chess.Board(nextFen)
    # print()
    # print(initialBoard, "\n")

    # print("Possible Moves: ", initialBoard.legal_moves)
    blackMove = input("Enter your move: ")
    # initialBoard.push_san(blackMove)
    # print()
    # print(initialBoard, "\n")

    

