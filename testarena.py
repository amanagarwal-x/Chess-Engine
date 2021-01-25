import chess

newboard = chess.Board()

atte4 = newboard.is_attacked_by(chess.WHITE,chess.E4) # returns boolean -> if square is attacked by that piece
atte3 = newboard.is_attacked_by(chess.WHITE,chess.E3)
print(atte3)