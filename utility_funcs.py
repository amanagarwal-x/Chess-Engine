import chess

SQUARE_FROM_INT = {
    1:'A1', 2:'B1', 3:'C1', 4:'D1', 5:'E1', 6:'F1', 7:'G1', 8:'H1',
    9:'A2', 10:'B2', 11:'C2', 12:'D2', 13:'E2', 14:'F2', 15:'G2', 16:'H2',
    17:'A3', 18:'B3', 19:'C3', 20:'D3', 21:'E3', 22:'F3', 23:'G3', 24:'H3',
    25:'A4', 26:'B4', 27:'C4', 28:'D4', 29:'E4', 30:'F4', 31:'G4', 32:'H4',
    33:'A5', 34:'B5', 35:'C5', 36:'D5', 37:'E5', 38:'F5', 39:'G5', 40:'H5',
    41:'A6', 42:'B6', 43:'C6', 44:'D6', 45:'E6', 46:'F6', 47:'G6', 48:'H6',
    49:'A7', 50:'B7', 51:'C7', 52:'D7', 53:'E7', 54:'F7', 55:'G7', 56:'H7',
    57:'A8', 58:'B8', 59:'C8', 60:'D8', 61:'E8', 62:'F8', 63:'G8', 64:'H8',
}

squaresdict={'A1':chess.A1, 'A2':chess.A2, 'A3':chess.A3, 'A4':chess.A4,'A5':chess.A5,'A6':chess.A6,'A7':chess.A7,'A8':chess.A8,'B1':chess.B1, 'B2':chess.B2, 'B3':chess.B3, 'B4':chess.B4,'B5':chess.B5,'B6':chess.B6,'B7':chess.B7,'B8':chess.B8,'D1':chess.D1, 'D2':chess.D2, 'D3':chess.D3, 'D4':chess.D4,'D5':chess.D5,'D6':chess.D6,'D7':chess.D7,'D8':chess.D8,'F1':chess.F1, 'F2':chess.F2, 'F3':chess.F3, 'F4':chess.F4,'F5':chess.F5,'F6':chess.F6,'F7':chess.F7,'F8':chess.F8,'G1':chess.G1, 'G2':chess.G2, 'G3':chess.G3, 'G4':chess.G4,'G5':chess.G5,'G6':chess.G6,'G7':chess.G7,'G8':chess.G8,'C1':chess.C1, 'C2':chess.C2, 'C3':chess.C3, 'C4':chess.C4,'C5':chess.C5,'C6':chess.C6,'C7':chess.C7,'C8':chess.C8,'E1':chess.E1, 'E2':chess.E2, 'E3':chess.E3, 'E4':chess.E4,'E5':chess.E5,'E6':chess.E6,'E7':chess.E7,'E8':chess.E8,'H1':chess.H1, 'H2':chess.H2, 'H3':chess.H3, 'H4':chess.H4,'H5':chess.H5,'H6':chess.H6,'H7':chess.H7,'H8':chess.H8,}

def LegalSort(board):
    '''
    Returns the legal moves after sorting them
    Sorting order : First moves with capture or check, then other moves
    '''
    SortedLegalMoves=[]
    for i in board.legal_moves:
        # start=str(i)[:2].upper()
        end = str(i)[2:].upper()
        # print(board.gives_check(move=i))
        # print(f'start is {start} and end is {end}')
        if(board.piece_at(square=squaresdict[end])):
            # SortedLegalMoves.append(str(i))
            SortedLegalMoves.insert(0,str(i))
        elif(board.gives_check(move=i)):
            SortedLegalMoves.insert(0,str(i))
        else:
            SortedLegalMoves.append(str(i))

    return SortedLegalMoves


def fast_legal_sort(board):
    move_set = set()
    sannns="initial"
    for move in board.legal_moves:
        sannns = " ".join(board.san(move) for move in board.legal_moves)
        move_set.add(str(sannns))
    move_list = sannns.split(" ")
    sorted_list=[]
    # print(f'move set is {move_list} and len is {len(move_list)}')
    for move in move_list:
        if (('x' in str(move)) or ('+' in str(move)) or ('#' in str(move))):
            sorted_list.insert(0,str(move))
        else:
            sorted_list.insert(len(sorted_list),str(move))
    
    return sorted_list

def piece_location(board):
    """
    Returns two dictionary white piece, black_piece of format --> {'Piece_type':Square}
    for example 
    white dictionary
    {'P': 'A2', 'R': 'A1', 'N': 'B1', 'B': 'C1', 'K': 'E1', 'Q': 'D1'}
    black dictionary
    {'r': 'A8', 'n': 'B8', 'b': 'C8', 'k': 'E8', 'q': 'D8', 'p': 'A7'}
    """

    piecemap = board.piece_map()
    white_pieces={}
    black_pieces={}
    for pair in piecemap:
        key = pair
        val = piecemap[key]
        # print(f'key : {key} val : {val}')
        if(str(val.symbol()).isupper()): #WHITE
            white_pieces[val.symbol()] = SQUARE_FROM_INT[key+1]
        else:
            black_pieces[val.symbol()] = SQUARE_FROM_INT[key+1]
    # print(f'white dictionary \n{white_pieces}\nblack dictionary \n{black_pieces}\n')
    return white_pieces,black_pieces



print('--------------------------------------------------------')
# newboard = chess.Board('r1b1k2r/ppp1pppp/5n2/2bp4/2B1Pnq1/1R3N1P/PPPP1PP1/RNBQ2K1 w Qkq - 0 1')
newboard = chess.Board('3rk3/5p2/8/8/8/1B6/5Q2/K7 w - - 0 1')
print(fast_legal_sort(newboard))
print(LegalSort(newboard))

