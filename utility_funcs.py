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

def convert_to_standard(board,old_move):
    """
    takes input as old notation (e2e4) and converts to standard notation (e4)
    returns - standard notation form of given move in old notation
    """
    startt = old_move[:2].upper()
    endd = old_move[2:].upper()
    conv = chess.Move(from_square=squaresdict[startt],to_square=squaresdict[endd])
    move_new = "".join(board.san(conv))

    return move_new

def fast_legal_sort(board):
    #? need to check this in minimax
    move_set = set()
    for i in board.legal_moves:
        move_set.add(convert_to_standard(board,str(i)))
    print(move_set)

    sorted_list = []
    for move in move_set:
        if '#' in move:
            sorted_list.append(move)
    for move in move_set:
        if (('#' not in move) and ('+' in move or 'x' in move)):
            sorted_list.append(move)
        elif('#' not in move and '+' not in move and 'x' not in move):
            sorted_list.append(move)
    # print(f'\nold list {move_set}\nnew list {sorted_list}\n')
    return sorted_list


def find_from_pgn(data,current_pgn):
    """
    data - content of pgn file from file read
    current_pgn - running pgn of the game
    returns - next move according to given database in string form in standard notation (e4 and not e2e4)
    """
    index = data.find(current_pgn)
    if(index==-1):
        return ""
    else:
        move = data[index+len(current_pgn)+3:index+len(current_pgn)+10]
        if ' ' in move:
            sep = move.split(' ')
            move = sep[0]
        return move




'''
#---------------------------TESTING FOR PGN-----------------------
# f = open("Database\pgn_database.txt","r")
# content = f.read()
# f.close()
#cur_pgn1 = "1. d4 Nf6"
# cur_pgn2 = "1. a3 e5 2. e3 d6" #2 moves //ans d4
# cur_pgn3 = "1. Nf3 Nf6 2. c4 g6 3. g3 c6" #3 moves //ans - Bg2
# cur_pgn4 = "1. c4 c6 2. d4 d5 3. Nc3 Nf6 4. e3 a6" #4 moves //ans - Nf3
# cur_pgn5 = "1. d4 d5 2. c4 c6 3. Nc3 Nf6 4. Nf3 a6 5. Bg5 Ne4" #5 moves // ans - e3
# cur_pgn6 = "1. d4 c6 2. e4 d5 3. Nd2 dxe4 4. Nxe4 Nf6 5. Ng3 e5 6. dxe5 Qxd1+" #6 moves// ans- Kxd1
# cur_pgn7 = "1. e4 c6 2. d4 d5 3. Nc3 dxe4 4. Nxe4 Bf5 5. Ng3 Bg6 6. h4 h6 7. N1e2 e6" #7 moves // ans - Nf4
# cur_pgn8 = "1. e4 c5 2. Nf3 a6 3. d4 cxd4 4. Nxd4 Nf6 5. Nc3 d6 6. Bg5 e6 7. Qd2 Be7 8. f4 h6" #8 moves // ans- Bxf6
# cur_pgn9 = "1. Nf3 g6 2. e3 Bg7 3. c4 c5 4. Nc3 Nc6 5. b3 Nf6 6. Bb2 O-O 7. Be2 a6 8. O-O Rb8 9. d4 d6" #9 moves // ans - dxc5


# print(find_from_pgn(content,cur_pgn5))
# print(find_from_pgn(content,cur_pgn6))
# print(find_from_pgn(content,cur_pgn7))
# print(find_from_pgn(content,cur_pgn8)) 
# print(find_from_pgn(content,cur_pgn9)) #!does not work if no of completed moves>8
# print(find_from_pgn(content,cur_pgn2))
'''