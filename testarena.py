from Aman.main import *
from Mihir.mihir import *

import chess

newboard = chess.Board("8/8/8/8/8/8/3P4/5N2 w - - 0 1") 
print(newboard) 




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


print(f'\nset of atttackers E3 : \n{newboard.attackers(color=True,square=chess.E3)}\n')


sqatte3 = newboard.attackers(color=True,square=chess.E3)


print(f'count of attackers {countsqset(sqatte3)}')


# attf4 = newboard.is_attacked_by(chess.WHITE,chess.F4)
# print(attf4)

# print(possibleStates(newboard.fen()))


# atte4 = newboard.is_attacked_by(chess.WHITE,chess.E4) # returns boolean -> if square is attacked by that piece
# atte3 = newboard.is_attacked_by(chess.WHITE,chess.E3)
# print(atte3)