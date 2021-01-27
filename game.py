import chess

# from main import *
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
            score = eval_centerControl(i) + materialcount(i) + eval_kingCheck(i)
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
                if blackMove == 'q':                                                    # Press X to quit game
                    return
                # elif (blackMove in initialBoard.legal_moves):
                initialBoard.push_san(blackMove)
                print()
                print(initialBoard, "\n")
                break
            except:
                print("\n\nINVALID MOVE\n\n")

        # initialBoard.push_san(blackMove)
        # print()
        # print(initialBoard, "\n")
   
game()