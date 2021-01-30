from Aman.main import *
from Mihir.mihirr import *

import chess

newboard = chess.Board() 
# print(newboard) 




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


# print(f'\nset of atttackers E3 : \n{newboard.attackers(color=True,square=chess.E3)}\n')
# sqatte3 = newboard.attackers(color=True,square=chess.E3)
# print(f'\ncount of attackers {countsqset(sqatte3)}\n')

# print(f'\nset of atttackers D2 : \n{newboard.attackers(color=True,square=chess.D2)}\n')
# sqattd2 = newboard.attackers(color=True,square=chess.D2)
# print(f'\ncount of attackers {countsqset(sqattd2)}\n')


# attf4 = newboard.is_attacked_by(chess.WHITE,chess.F4)
# print(attf4)

# print(possibleStates(newboard.fen()))


# atte4 = newboard.is_attacked_by(chess.WHITE,chess.E4) # returns boolean -> if square is attacked by that piece
# atte3 = newboard.is_attacked_by(chess.WHITE,chess.E3)
# print(atte3)

"""
    ek colour, pure board me, kitne squares control kar rha

    common square rehge, check no of attackers from both side

    ek funct

    sqw, sqb
    [a1-h8], 
"""


"""
trying dictionary
dict1={}
i=0
for square in upper_square:
    dict1[square]=i
    i+=1
print(dict1)
"""


def SortedList(newboard):
    '''
        Returns the legal moves after sorting them
        Sorting order : First moves with capture or check, then other moves
    '''

    # print(newboard)
    # print(newboard.legal_moves)
    squaresdict={'A1':chess.A1, 'A2':chess.A2, 'A3':chess.A3, 'A4':chess.A4,'A5':chess.A5,'A6':chess.A6,'A7':chess.A7,'A8':chess.A8,'B1':chess.B1, 'B2':chess.B2, 'B3':chess.B3, 'B4':chess.B4,'B5':chess.B5,'B6':chess.B6,'B7':chess.B7,'B8':chess.B8,'D1':chess.D1, 'D2':chess.D2, 'D3':chess.D3, 'D4':chess.D4,'D5':chess.D5,'D6':chess.D6,'D7':chess.D7,'D8':chess.D8,'F1':chess.F1, 'F2':chess.F2, 'F3':chess.F3, 'F4':chess.F4,'F5':chess.F5,'F6':chess.F6,'F7':chess.F7,'F8':chess.F8,'G1':chess.G1, 'G2':chess.G2, 'G3':chess.G3, 'G4':chess.G4,'G5':chess.G5,'G6':chess.G6,'G7':chess.G7,'G8':chess.G8,'C1':chess.C1, 'C2':chess.C2, 'C3':chess.C3, 'C4':chess.C4,'C5':chess.C5,'C6':chess.C6,'C7':chess.C7,'C8':chess.C8,'E1':chess.E1, 'E2':chess.E2, 'E3':chess.E3, 'E4':chess.E4,'E5':chess.E5,'E6':chess.E6,'E7':chess.E7,'E8':chess.E8,'H1':chess.H1, 'H2':chess.H2, 'H3':chess.H3, 'H4':chess.H4,'H5':chess.H5,'H6':chess.H6,'H7':chess.H7,'H8':chess.H8,}
    LegalMoves=[]
    for i in newboard.legal_moves: 
        start = str(i)[:2].upper()
        end = str(i)[2:].upper()
        # print(f'i is {i} and start is {start} and end is {end}')
        pieceat = newboard.piece_at(square=squaresdict[start])
        if(str(pieceat)!='P'):
            if(newboard.piece_at(square=squaresdict[end])): #if there is a piece on the new square then put 'x' in notation
                ret=str(pieceat)+'x'+str(i)[2:]
            else:
                ret = str(pieceat)+str(i)[2:]
            
        else:
            #if two piece of same type can go to square eg Nbe2, Nge2
            if(newboard.piece_at(square=squaresdict[end])): #if there is a piece on the new square then put 'x' in notation
                # Nbxe2, Ngxe2 //TODO: take care of this and other cases as well
                # else:
                ret=str(i)[0]+'x'+end.lower()
            else:
                ret=str(i)[2:]
        
        #checking if that move leads to a check
        newboard.push_san(ret)
        if(newboard.is_check()):
            ret+='+'
        newboard.pop()

        LegalMoves.append(ret)
        
    sortedList=[]
    for move in LegalMoves:
        if (('x' in move) or ('+' in move)): #moves which lead to capture or threat will be given priority
            sortedList.append(move)
            LegalMoves.remove(move)

    for move in LegalMoves:
        sortedList.append(move)
        LegalMoves.remove(move)


    return sortedList







