import pygame as p
import chessengine
import chess
from playsound import playsound
from main import Game, play_move
import pprint
pp=pprint.PrettyPrinter()

WIDTH=HEIGHT=512
DIMENSION=8
SQ_SIZE= HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES={}

def loadImages():
        pieces=['wp','wR','wN','wB','wQ','wK','bp','bR','bN','bB','bQ','bK']
        for piece in pieces:
            IMAGES[piece]=p.transform.scale(p.image.load("Mrunmai/Images/" + piece + ".png"),(SQ_SIZE, SQ_SIZE))
       
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs =chessengine.GameState()
    loadImages()
    running =True
    sqSelected = ()
    playerClicks = []
    move_no = 1
    board = chess.Board() 
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running=False
            elif e.type ==p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                col = location[0]//SQ_SIZE 
                row = location[1]//SQ_SIZE
                if sqSelected == (row,col):
                    sqSelected = ()
                    playerClicks=[]
                else:
                    sqSelected = (row,col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2 and move_no%2 == 0:
                    move =chessengine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    try:
                        board_dict = play_move(move_no, move.getChessNotation(), board)
                        #For CheckMate condition, board_dict == "CM"
                        boardList = gs.board
                        for square in board_dict:
                            boardList[chessengine.Move.filesToCols[square[0].lower()]][chessengine.Move.ranksToRows[square[1]]] = board_dict[square]
                        gs.board =[[row[i] for row in boardList] for i in range(len(boardList[0]))]
                        pp.pprint(gs.board)
                        playsound("./sounds/attack.wav")
                        move_no = move_no + 1
                    except ValueError:
                        print("Illegal Move")

                    sqSelected = ()
                    playerClicks=[]
                     
            elif move_no%2 != 0:
                board_dict = play_move(move_no, "454", board)
                boardList = gs.board
                for square in board_dict:
                    boardList[chessengine.Move.filesToCols[square[0].lower()]][chessengine.Move.ranksToRows[square[1]]] = board_dict[square]
                gs.board =[[row[i] for row in boardList] for i in range(len(boardList[0]))]
                pp.pprint(gs.board)
                playsound("./sounds/attack.wav")
                move_no = move_no + 1

        drawGameState(screen,gs)
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, gs):
        drawBoard(screen) 
        drawPieces(screen, gs.board) 

def drawBoard(screen):
    colors =[p.Color("white") , p.Color("darkgreen")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
           color = colors[((r+c)%2)]
           p.draw.rect(screen , color , p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))   


if __name__== "__main__":
    main()

    
