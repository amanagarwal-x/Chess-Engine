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
<<<<<<< HEAD
        # print (score)
=======
>>>>>>> 19ae2bb8da368df552aa9a87b7a4a8643005b255
        
        if score >= maxScore:
            maxScore = score
            nextFen = i
            # print(chess.Board(nextFen))
            # print(f'maxscore :{maxScore} score :{score}')

    
    initialBoard = chess.Board(nextFen)
    # print()
    # print(initialBoard, "\n")

    # print("Possible Moves: ", initialBoard.legal_moves)
    blackMove = input("Enter your move: ")
    # initialBoard.push_san(blackMove)
    # print()
    # print(initialBoard, "\n")

    

