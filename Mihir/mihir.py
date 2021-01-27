import chess

board2 = chess.Board()
fenn = 'rnb1kbnr/ppp1pp1p/6p1/3N4/8/8/PPPP1PPP/R1BQKBNR b KQkq - 0 4' 


# materialcount(fenn)


def countsqset(sqset):
    """
    
     takes input as sqset, returns number of 1s in it 
     made it to count no of pieces attacking a particular square as .attack() returns a squareset 
     
    """
    countt=0
    for sq in sqset:
        countt+=1
    return countt






    


