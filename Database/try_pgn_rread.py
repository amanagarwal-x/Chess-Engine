import chess
import chess.pgn

f = open("Database\lichess_elite_dec2019.pgn")
# f = open("Database\master_games.pgn")
g = open("demo1.txt", "a")


i=0
while(True):
    i+=1
    game = chess.pgn.read_game(f)
    if game is None:
        break
    headers=dict(game.headers)
    print(game.board().variation_san(game.mainline_moves()))
    g.write(str(game.board().variation_san(game.mainline_moves())))
    g.write("\n")

f.close()
g.close()
# print(result)
