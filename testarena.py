from Aman.main import *

import chess

newboard = chess.Board() #starting position


upper_square=[] # contains all square names in uppercase
for word in chess.SQUARE_NAMES:
    upper_square.append(word.upper())
print(upper_square)    


# attf4 = newboard.is_attacked_by(chess.WHITE,chess.F4)
# print(attf4)

# print(possibleStates(newboard.fen()))


# atte4 = newboard.is_attacked_by(chess.WHITE,chess.E4) # returns boolean -> if square is attacked by that piece
# atte3 = newboard.is_attacked_by(chess.WHITE,chess.E3)
# print(atte3)