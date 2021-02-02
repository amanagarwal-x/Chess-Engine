import chess.pgn
pgn = open("Database/master_games.pgn")

first_game = chess.pgn.read_game(pgn)

fen_movedict = {}
i=0
board = first_game.board()
for move in first_game.mainline_moves():
    # i+=1
    # print(i)
    board.push(move)
    print(f'\nmove played {move}\n')
    print(board,'\n')
