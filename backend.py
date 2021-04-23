import chess
import math
import random
from evalFunctions import evaluate
from utility_funcs import *

maximumScore = 1000^3
minimumScore = -1000^3
maxDepth = 2

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
        board.pop()            
    return bestMove
