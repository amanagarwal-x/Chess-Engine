import chess

newboard = chess.Board()

atte4 = newboard.is_attacked_by(chess.WHITE,chess.E4)
atte3 = newboard.is_attacked_by(chess.WHITE,chess.E3)
print(atte3)