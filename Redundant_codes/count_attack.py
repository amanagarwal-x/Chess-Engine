import chess

from utility_funcs import *

upper_square = [chess.A1, chess.B1, chess.C1, chess.D1, chess.E1,
                chess.F1, chess.G1, chess.H1, chess.A2, chess.B2, chess.C2, chess.D2, chess.E2,
                chess.F2, chess.G2, chess.H2,chess.A3, chess.B3, chess.C3, chess.D3, chess.E3,
                chess.F3, chess.G3, chess.H3,chess.A4, chess.B4, chess.C4, chess.D4, chess.E4,
                chess.F4, chess.G4, chess.H4,chess.A5, chess.B5, chess.C5, chess.D5, chess.E5,
                chess.F5, chess.G5, chess.H5,chess.A6, chess.B6, chess.C6, chess.D6, chess.E6,
                chess.F6, chess.G6, chess.H6,chess.A7, chess.B7, chess.C7, chess.D7, chess.E7,
                chess.F7, chess.G7, chess.H7,chess.A8, chess.B8, chess.C8, chess.D8, chess.E8,
                chess.F8, chess.G8, chess.H8,]  # contains all square names in uppercase


# print(upper_square_string)


def count_attack(fen):
    # print(board(f''))
    cur_pos = chess.Board(f'{fen}')
    print(cur_pos)
    i = 0
    white_control = {}
    black_control = {}
    # for sq in upper_square:
    #     # first initializing control of that square to 0 times
        # white_control[sq] = 0
        # black_control[sq] = 0
    for sq in upper_square:
        white_control[upper_square_string[i]] = countsqset(
            cur_pos.attackers(color=True, square=sq))
        black_control[upper_square_string[i]] = countsqset(
            cur_pos.attackers(color=False, square=sq))

        i += 1

    print(f'\nList of control of squares for white : \n{white_control}')
    print(f'\nList of control of squares for black : \n{black_control}')

    cntwhite=0
    cntblack=0
    for num in white_control.values():
        cntwhite+=num
    for num in black_control.values():
        cntblack+=num
    cnt_outofone = (cntwhite - 1)/26

    print(f'white controls {cntwhite} squares and black controls {cntblack} squares')
    diff = cntwhite - cntblack
    if(diff==0):
        return diff

    '''
    max value of difference = 63, min value -63 
    ''' 
    if(diff!=0):
        scaled_diff = (diff +63)/(126)
        return scaled_diff*(abs(diff)/diff)


# print(count_attack('3k3r/8/8/8/8/8/8/R2K4 w - - 0 1'))
# print(count_attack('8/8/8/3q4/8/8/7P/8 w - - 0 1'))

