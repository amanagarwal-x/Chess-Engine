from Aman.main import *
from Mihir.mihirr import *
from utility_funcs import *
import chess
import pprint
from final_game import game
pp=pprint.PrettyPrinter()

newboard = chess.Board() 
# print(newboard) 




# print(newboard)
upper_square=[] # contains all square names in uppercase
for word in chess.SQUARE_NAMES:
    upper_square.append(word.upper())
# print(upper_square)   

# print(newboard.is_attacked_by(color=True, square=chess.D4))
# print(f'\n If I select square D2 \n{newboard.attacks(chess.D2)}\n') 
# print(f'\nIf I select square F1 \n{newboard.attacks(chess.F1)}\n') 

# print(f'\nno of ones for D2 : {countones(newboard.attacks(chess.D2))}\n')
# print(f'\nno of ones for F1 : {countones(newboard.attacks(chess.F1))}\n')

""" returned this-> (if only one pawn on d2 nothing else)
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . 1 . 1 . . .
. . . . . . . .
. . . . . . . .

returned this-> (if I add a knight on f1 in same position but select square D2)
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . 1 . 1 . . .
. . . . . . . .
. . . . . . . .

returned this-> if in prev position I choose square F1
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . 1 . 1 .
. . . 1 . . . 1
. . . . . . . .

so it doesnt count number of attackers, it just sees if it is being controlled by white or not
"""


# print(f'\nset of atttackers E3 : \n{newboard.attackers(color=True,square=chess.E3)}\n')
# sqatte3 = newboard.attackers(color=True,square=chess.E3)
# print(f'\ncount of attackers {countsqset(sqatte3)}\n')

# print(f'\nset of atttackers D2 : \n{newboard.attackers(color=True,square=chess.D2)}\n')
# sqattd2 = newboard.attackers(color=True,square=chess.D2)
# print(f'\ncount of attackers {countsqset(sqattd2)}\n')


# attf4 = newboard.is_attacked_by(chess.WHITE,chess.F4)
# print(attf4)

# print(possibleStates(newboard.fen()))


# atte4 = newboard.is_attacked_by(chess.WHITE,chess.E4) # returns boolean -> if square is attacked by that piece
# atte3 = newboard.is_attacked_by(chess.WHITE,chess.E3)
# print(atte3)

"""
    ek colour, pure board me, kitne squares control kar rha

    common square rehge, check no of attackers from both side

    ek funct

    sqw, sqb
    [a1-h8], 
"""


"""
# trying dictionary
dict1={}
i=0
for square in upper_square:
    dict1[square]=i
    i+=1
print(dict1)

fruits={'apple':3,'orange':4,'banana':5,'chikoo':7}
for fruit in fruits:
    # print(f'value is {fruit.value()}')
    print(f'printing iterator {fruit}')
    print(f'value is {fruits[fruit]}')
"""

# def eval_PiecePosition(fen):
#     cur_board = chess.Board(f'{fen}')
#     white_pieces,black_pieces = piece_location(cur_board)
#     print(f'white dict \n{white_pieces}\nblack dict \n{black_pieces}\n')


# eval_PiecePosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')


neww = chess.Board()
# print(str(neww.piece_at(chess.A5)))
squaresdict={'A1':chess.A1, 'A2':chess.A2, 'A3':chess.A3, 'A4':chess.A4,'A5':chess.A5,'A6':chess.A6,'A7':chess.A7,'A8':chess.A8,'B1':chess.B1, 'B2':chess.B2, 'B3':chess.B3, 'B4':chess.B4,'B5':chess.B5,'B6':chess.B6,'B7':chess.B7,'B8':chess.B8,'D1':chess.D1, 'D2':chess.D2, 'D3':chess.D3, 'D4':chess.D4,'D5':chess.D5,'D6':chess.D6,'D7':chess.D7,'D8':chess.D8,'F1':chess.F1, 'F2':chess.F2, 'F3':chess.F3, 'F4':chess.F4,'F5':chess.F5,'F6':chess.F6,'F7':chess.F7,'F8':chess.F8,'G1':chess.G1, 'G2':chess.G2, 'G3':chess.G3, 'G4':chess.G4,'G5':chess.G5,'G6':chess.G6,'G7':chess.G7,'G8':chess.G8,'C1':chess.C1, 'C2':chess.C2, 'C3':chess.C3, 'C4':chess.C4,'C5':chess.C5,'C6':chess.C6,'C7':chess.C7,'C8':chess.C8,'E1':chess.E1, 'E2':chess.E2, 'E3':chess.E3, 'E4':chess.E4,'E5':chess.E5,'E6':chess.E6,'E7':chess.E7,'E8':chess.E8,'H1':chess.H1, 'H2':chess.H2, 'H3':chess.H3, 'H4':chess.H4,'H5':chess.H5,'H6':chess.H6,'H7':chess.H7,'H8':chess.H8}

def converter(boardd):
    '''
    gives dict which shows location of all pieces, key - square ('A1'), value-piece('bR') 
    '''

    dictt ={}
    for square in squaresdict:
        # print(square)
        dictt[square] = '--' 
    mmap={'N':'wN','n':'bN','P':'wp','p':'bp','R':'wR','r':'bR','Q':'wQ','q':'bQ','K':'wK','k':'bK','B':'wB','b':'bB','None':'--'}


    for squares in dictt:
        cur_piece = str(boardd.piece_at(squaresdict[squares]))
        # print(f'square-{squares},cur_piece={cur_piece}')
        dictt[squares]=mmap[cur_piece]
    
    return dictt


# print(str(neww.find_move(from_square=chess.E2 ,to_square=chess.E3)))


def give_high(sq):
    '''
    give input square in string form (in capital eg-E4)
    returns list of legal moves from that square

    eg - give_high('E2') ==> ['E3','E4']
    '''
    leg_list=[]
    for square in squaresdict:
        try:
            cur_square=str(neww.find_move(from_square=squaresdict[sq] ,to_square=squaresdict[square]))[2:].upper()
            leg_list.append(cur_square)
        except ValueError:
            # print('wrong move')
            pass
    return leg_list


def play_move(boardd,movee):
    boardd.push_san(movee)


neww.push_san('e2e4')
# print(give_high('B1'))
# pp.pprint(converter())


