from utility_funcs import *
import chess
import pprint
from main import Game
pp=pprint.PrettyPrinter()

# newboard = chess.Board() 
# print(newboard) 




# # print(newboard)
# upper_square=[] # contains all square names in uppercase
# for word in chess.SQUARE_NAMES:
#     upper_square.append(word.upper())
# # print(upper_square)   

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


# neww = chess.Board()
# print(str(neww.piece_at(chess.A5)))



from count_attack import upper_square
a=squaresdict.values()




