import chess
from utility_funcs import *

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
def eval_materialCount(fen):

    '''
    takes fen as input, and returns(integer) material imbalance present in the game
    positive means in favour of white
    negative means in favour of black

    PIECE VALUES USED TO EVALUATE MATERIAL COUNT - 
    Pawns - 1 point
    Bishops and Knights - 3 points
    Rooks - 5 points
    Queen - 9 points

    variables used and their meaning - 
    white_mat, black_mat - A list which stores how many pieces of each type(pawns, knights, bishops etc) are present on the board for each colour
    format in which they are stored - white_mat = [8,2,2,2,1,1] (pawn, knight, bishop, rook, queen, king)
    
    '''

    board = chess.Board(f'{fen}')
    white_mat = []
    black_mat = []

    for i in range(1,7):
        sqset = board.pieces(piece_type = i, color = True) #color = True (white) piece_type =(1,7) [pawn, knight, bishop, rook, queen, king]
        cnt = 0
        for square in sqset:
            cnt+=1
        white_mat.append(cnt)
    for i in range(1,7):
        sqset = board.pieces(piece_type = i, color = False) #color = False (black) piece_type =(1,7) [pawn, knight, bishop, rook, queen, king]
        cnt = 0
        for square in sqset:
            cnt+=1
        black_mat.append(cnt)
    white_score = white_mat[0]*1 + white_mat[1]*3.2 + white_mat[2]*3.3 + white_mat[3]*5 + white_mat[4]*9
    black_score = black_mat[0]*1 + black_mat[1]*3.2 + black_mat[2]*3.3 + black_mat[3]*5 + black_mat[4]*9
    total_score = white_score - black_score

    return total_score

#
def eval_countAttack(fen):
    '''
    counts no of attackers of white - cntwhite
    counts no of attackers of black - cntblack

    returns the difference scaled down out of 1,  positive means good for ai, negative means bad for ai

    '''

    cur_pos = chess.Board(f'{fen}')
    # print(cur_pos)
    white_control = {}
    black_control = {}
    i=0
    for sq in squaresdict.values():
        white_control[upper_square_string[i]] = countsqset(
            cur_pos.attackers(color=True, square=sq))
        black_control[upper_square_string[i]] = countsqset(
            cur_pos.attackers(color=False, square=sq))
        i+=1

    # print(f'\nList of control of squares for white : \n{white_control}')
    # print(f'\nList of control of squares for black : \n{black_control}')

    cntwhite=0
    cntblack=0
    for num in white_control.values():
        cntwhite+=num
    for num in black_control.values():
        cntblack+=num
    # cnt_outofone = (cntwhite - 1)/26 #scaled out value for sole control of white over the board

    # print(f'white controls {cntwhite} squares and black controls {cntblack} squares')
    diff = cntwhite - cntblack
    if(diff==0):
        return diff

    #max value of difference = 63, min value -63 

    scaled_diff = (diff + 63)/126

    return scaled_diff*(abs(diff)/diff)

#
def eval_PiecePosition(fen):
    cur_board = chess.Board(f'{fen}')
    white_pieces,black_pieces = piece_location(cur_board)
    print(f'white dict \n{white_pieces}\nblack dict \n{black_pieces}\n')
    #TODO : Positions of all pawns,rooks,bishops,knights is not added in map

#
def eval_isCheckMate(fen):
    board = chess.Board(fen)
    if(board.is_checkmate() or board.is_stalemate()):
        return 10^8
    return 0    

#
def evaluate(fen):
    # return (eval_centerControl(fen) + eval_materialCount(fen) + eval_kingCheck(fen) + eval_countAttack(fen))
    return (eval_materialCount(fen) + eval_kingCheck(fen) + eval_countAttack(fen) + eval_isCheckMate(fen))

#
def debugscores(fen):
    print(f'score of materialcount : {eval_materialCount(fen)}')
    print(f'score of centercount : {eval_centerControl(fen)}')
    print(f'score of kingcheck : {eval_kingCheck(fen)}')
    print(f'score of squareControl : {eval_countAttack(fen)}')

    print(f'----------------------------------------\n total score : {evaluate(fen)}')

# debugscores('rnbqk2r/pppp1ppp/5n2/4p3/1bB1P3/2N5/PPPP1PPP/R1BQK1NR w KQkq - 4 4')

