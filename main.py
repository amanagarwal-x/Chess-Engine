from backend import miniMax, findBestMove
from utility_funcs import convert_to_standard, find_from_pgn, board_to_dict_converter, squaresdict
import random, chess
import pprint
pp=pprint.PrettyPrinter()


class Game:
    f = open("./Database/pgn_database.txt","r")
    content = f.read()
    f.close()
    cur_pgn=""
    pgn_move_no = 1

    @staticmethod
    def game(move_no, black_move, board):

        if(board.is_checkmate()):
            return 0
        if(board.is_stalemate()):
            return 0  
        
        #FIRST MOVE ----------
        if(move_no==1):
            opening_moves = ["e4","d4","b3","g3","Nf3","c4"]
            move = random.choice(opening_moves)
            board.push_san(f"{move}")
            Game.cur_pgn+= "1. " + move

        
        elif move_no%2!=0:
            next_move = find_from_pgn(Game.content,Game.cur_pgn)
            Game.pgn_move_no = Game.pgn_move_no + 1
            if(next_move!=""):
                Game.cur_pgn+=str(Game.pgn_move_no)+". "+ next_move
                board.push_san(next_move)
            
            else:
                movee = str(findBestMove(board))
                new_notation_move = convert_to_standard(board,str(movee))
                board.push_san(movee)
                Game.cur_pgn+= " " + str(Game.pgn_move_no) + ". " + new_notation_move  #Adding white move to current pgn in standard pgn notation

        else :
            if(board.is_checkmate()):
                return 0
            if(board.is_stalemate()):
                return 0

            blackMove = black_move
            Game.cur_pgn+=" " + convert_to_standard(board, blackMove) + " "
            board.push_san(blackMove)
            

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
            pass
    return leg_list



def play_move(move_no, black_move, board):
    if move_no == 1:
        Game.game(move_no, 69, board)
    else:
        if Game.game(move_no, black_move, board) == 0:
            return ("CM")
    print("PGN", Game.cur_pgn)            
    return board_to_dict_converter(board)



#For simuating GUI flow
board = chess.Board() 
def gui():
    move_no = 1
    black_move = "e7e5"
    # print(board)
    print(play_move(move_no, 69, board))
    # print(board)

    move_no = move_no+1
    print(play_move(move_no, black_move, board))
    # print(board)

    move_no = move_no+1
    print(play_move(move_no, 59 , board))

    move_no = move_no+1
    # print(play_move(move_no, "d7d5", board))
    # print(board)    
    pp.pprint(boardList)
    # board_dict = play_move(move_no, "d7d5", board)
    # for square in board_dict:
    #     boardList[filesToCols[square[0].lower()]][ranksToRows[square[1]]] = board_dict[square]
    # boardList_T =[[row[i] for row in boardList] for i in range(len(boardList[0]))]
    # pp.pprint(boardList_T)
# gui()




boardList=[
    ["bR","bN","bB","bQ","bK","bB","bN","bR"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wR","wN","wB","wQ","wK","wB","wN","wR"]
]

ranksToRows = {"1":7, "2":6, "3":5, "4":4, "5":3, "6":2, "7":1, "8":0 }
filesToCols = {"a":0 ,"b":1 , "c":2, "d":3, "e":4, "f":5, "g":6,"h":7}