import chess

#
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

    return score

#
def eval_kingCheck(fen): 
    ''' 
    Function to evaluate if king is under check
    Takes fen as input, and returns 0 or 1 as output.
    (Remember to give this higher weight in the driver function)
    '''
    return chess.Board(fen).is_check()

#    