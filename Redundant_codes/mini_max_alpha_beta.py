import chess
import math
# from Aman.main import *
# from Mihir.mihirr import *
from evalFunctions import *
from utility_funcs import *
maximumScore = 1000^3
minimumScore = -1000^3
maxDepth = 3

alppha = -math.inf
betta = math.inf
def miniMax(board, depth,alpha,beta, isMax):
    score = evaluate(board.fen())

    if score >= maximumScore or score <= minimumScore or depth == maxDepth:
        return score

    if isMax:
        best = -1000
        SortedList = LegalSort(board)
        for i in SortedList:
            board.push_san(str(i))
            best = max( best, miniMax(board, depth+1,alpha,beta, not isMax))
            board.pop()
            alpha=max(alpha,best)

            if(beta<=alpha):
                return best
        return best

    else:
        best = 1000
        SortedList = LegalSort(board)
        for i in SortedList:
            board.push_san(str(i))
            best = min( best, miniMax(board, depth+1,alpha,beta, not isMax))
            board.pop()
            beta=min(beta,best)
            if(beta<=alpha):
                return best
        return best    

def findBestMove(board):
    bestVal = -1000
    moveVal = 0
    bestMove = ""
    SortedList = LegalSort(board)
    for i in SortedList:
        board.push_san(str(i))
        moveVal = miniMax(board, 0,alppha,betta, False)
    
        if moveVal >= bestVal:
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
        if(board.is_checkmate()):
            print('-----------------GAME OVER-----------------')
            break
        if(board.is_stalemate()):
            print('-----------------STALEMATE-----------------')
            break        
        print("Computer's Move:")
        board.push_san(str(findBestMove(board)))
        print()
        print(board, "\n")

        while(1):
            if(board.is_checkmate()):
                print('-----------------GAME OVER-----------------')
                break
            if(board.is_stalemate()):
                print('-----------------STALEMATE-----------------')
                break   
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