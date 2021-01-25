import chess
board = chess.Board()


def materialcount(fen):

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
        sqset = board.pieces(piece_type = i, color = True)
        cnt = 0
        for square in sqset:
            cnt+=1
        white_mat.append(cnt)
    for i in range(1,7):
        sqset = board.pieces(piece_type = i, color = False)
        cnt = 0
        for square in sqset:
            cnt+=1
        black_mat.append(cnt)
    white_score = white_mat[0]*1 + white_mat[1]*3 + white_mat[2]*3 + white_mat[3]*5 + white_mat[4]*9
    black_score = black_mat[0]*1 + black_mat[1]*3 + black_mat[2]*3 + black_mat[3]*5 + black_mat[4]*9
    total_score = white_score - black_score

    print(f'Material imbalance = {total_score}')

    return total_score
    



