import chess
from Aman.main import *
from Mihir.mihir import *
from evalFunctions import *

maximumScore = 1000^3
minimumScore = -1000^3
maxDepth = 3



def miniMax(board, depth, isMax):
    score = evaluate(board.fen())

    if score >= maximumScore or score <= minimumScore or depth == maxDepth:
        return score

    if isMax:
        best = -1000
        for i in board.legal_moves:
            board.push_san(str(i))
            best = max( best, miniMax(board, depth+1, not isMax))
            board.pop()
        return best

    else:
        best = 1000
        for i in board.legal_moves:
            board.push_san(str(i))
            best = min( best, miniMax(board, depth+1, not isMax))
            board.pop()
        return best    

def findBestMove(board):
    bestVal = -1000
    moveVal = 0
    bestMove = ""
    for i in board.legal_moves:
        board.push_san(str(i))
        moveVal = miniMax(board, 0, False)
    
        if moveVal > bestVal:
            bestVal = moveVal
            bestMove = board.peek()
            # print ("#########", board.peek())
        board.pop()            
    return bestMove



def game():
    board = chess.Board() 
    print()
    print(board, "\n")
    while(1):  
        print("Computer's Move:")
        board.push_san(str(findBestMove(board)))
        print()
        print(board, "\n")

        while(1):
            try:
                print("Possible Moves: ", board.legal_moves)
                blackMove = input("Enter your move: ")

                if blackMove == 'q':                                                    # Press q to quit game
                    return

                board.push_san(blackMove)
                print()
                print(board, "\n")
                break
            except:
                print("\n\nINVALID MOVE\n\n")

game()
















#TEST AREA

# class Node:
#     def __init__(self, board, score, left = None, right = None):
#         self.board = board
#         self.score = score
#         self.right = right
#         self.left = left


# def miniMax(board):
#     root = Node(board, finalScore(board.fen()))
#     for i in possibleStates(board.fen()):   
#         return