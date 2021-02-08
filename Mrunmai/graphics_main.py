
import pygame as p
import chess

import chessEngine

WIDTH = HEIGHT = 512
DIMENSION=8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {} #dictionary to store all the images piece wise


#this will be called once in main

def loadImages():
    pieces = ['P' , 'R' , 'N', 'B' , 'K', 'Q' , 'p' , 'r' , 'n' , 'b' ,'k' ,'q' ]
    for piece in pieces:
        if(piece.isupper()):
            IMAGES[piece] = p.transform.scale(p.image.load("white/" + piece +  ".png"),(SQ_SIZE, SQ_SIZE))
        else:
            IMAGES[piece] = p.transform.scale(p.image.load("black/" + piece + ".png"),(SQ_SIZE, SQ_SIZE))
            
            
        #we can access image of white pawn by : IMAGES['P'] since we got by =  p.image.load(images/P.png)
        
#main function this will handle user input and update the graphics:
#IMAGES['P'] = p.image.load(dvndjvd.png)


def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))  
    gs = chessEngine.GameState()
    print(gs.board)
    loadImages() #do only once, before the while loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)        
        clock.tick(MAX_FPS)
        p.display.flip()
        
def drawGameState(screen, gs):
    drawBoard(screen) #draw squares on board
    #add extra graphics
    draPieces(screen, gs.board) #draw pieces on top of those squares
    


#draw the squares on board
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("grey")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c)%2)] #if 0: white if 1 then grey
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    #p.display.flip()
    
def draPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE , SQ_SIZE))
    
main()
