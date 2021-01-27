import chess

from Aman.main import *
from Mihir.mihir import *
from evalFunctions import *



def game():
    initialBoard = chess.Board() 
    print()
    print(initialBoard, "\n")
    while(1):        
        print("Computer's Move:")

        maxScore = float('-inf')
        nextFen = ""
        for i in possibleStates(initialBoard.fen()): 
            score = eval_centerControl(i) + eval_materialCount(i) + eval_kingCheck(i)
            if score >= maxScore:
                maxScore = score
                nextFen = i


        initialBoard = chess.Board(nextFen)
        print()
        print(initialBoard, "\n")
        
        while(1):
            try:
                print("Possible Moves: ", initialBoard.legal_moves)
                blackMove = input("Enter your move: ")

                if blackMove == 'q':                                                    # Press q to quit game
                    return

                initialBoard.push_san(blackMove)
                print()
                print(initialBoard, "\n")
                break
            except:
                print("\n\nINVALID MOVE\n\n")

   
game()




#TEST AREA

# def test():
#     initialBoard = chess.Board() 
#     print()
#     print(initialBoard, "\n")
#     print("Computer's Move:")

#     initialBoard.push_san("e4")
#     print()
#     print(initialBoard, "\n")
#     initialBoard.pop()
#     print()
#     print(initialBoard, "\n")

# test()    