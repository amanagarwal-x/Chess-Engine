import chess
import chess.pgn

# f = open("Database\master_games.pgn")
f = open("Database/pgn_database.txt", "r")
g = open("Database/sorted_pgn_database.txt","w")
# f = open("Database/dem1.txt", "r")
# content = f.read()

dict1={}
sorteddict1={}

while(True):
    cur_line=f.readline()
    dict1[cur_line]=len(cur_line)
    if(f.readline()==""):
        break
f.close()

#Sorting dicitonary on values - no of moves(len of line read)

sorteddict1=sorted(dict1.items(), key = lambda kv:(kv[0], kv[1]))
sorteddict2 = {k: v for k, v in sorted(dict1.items(), key=lambda item: item[1])}
for pg in reversed(sorteddict2):
    print(sorteddict2[pg])
    # print(pg)
    g.write(pg)

# print(sorteddict2.values())
# for tup in sorteddict1:
#     print(tup[1])


# print(type(sorteddict1))