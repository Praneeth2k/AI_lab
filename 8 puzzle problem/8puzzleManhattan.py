# 8 puzzle problem

board = [4, 1, 3, 7, 2, 6, 5 , 8, 0]
final = [1, 2, 3, 4, 5, 6, 7 , 8, 0]

row = [1, 1, 1, 2, 2, 2, 3, 3, 3]
col = [1, 2, 3, 1, 2, 3, 1, 2, 3]

prev = "N"

prev_prev = "N"

dm = "N"



def start():
    global prev
    global prev_prev
    global dm
    while final_reached() == False:
        
        if(prev_prev == "L" and prev == "R" or prev_prev == "R" and prev == "L"):
            dm = "S"
        if(prev_prev == "D" and prev == "U" or prev_prev == "U" and prev == "D"):
            dm = "V"
        
        prev_prev = prev
        prev = move()

        print(prev)
        

        dm = "N"

def final_reached():
    for i in range(9):
        if(board[i] != final[i]):
            return False
    
    return True



def move():
    a = 9999
    b = 9999
    c = 9999
    d = 9999
    dist = 9999
    move = "L"
    if(dm!="S"):
        if(move_tile("L")):
            
            a = manhattan()
            dist = a
            du = move_tile("R")
        if(move_tile("R")):
            
            b = manhattan()
            if(b < dist):
                dist = b
                move = "R"
            du = move_tile("L")
    if(dm!="V"):
        if(move_tile("U")):
            c = manhattan()
            if(c < dist): 
                dist = c
                move = "U"
            du = move_tile("D")
        if(move_tile("D")):
            d = manhattan()
            if(d < dist): 
                dist = d
                move = "D"
            du = move_tile("U")
    du = move_tile(move)
    
    
    return move

def move_tile(m):
    z = index_of(0)
    if(m == "L"):
        if(z == 0 or z == 3 or z == 6):
            return False
        swap_board(z-1, z)
    if(m == "R"):
        if(z == 2 or z == 5 or z == 8):
            return False
        swap_board(z, z+1)
    if(m == "U"):
        if(z == 0 or z == 1 or z == 2):
            return False
        swap_board(z-3, z)
    if(m == "D"):
        if(z == 6 or z == 7 or z == 8):
            return False
        swap_board(z, z+3)
    return True

def manhattan():
    sum = 0
    for i in range(9):
        p = index_of(i)
        

        q = final_index(i)
        
        sum = sum + abs(int(row[p]) - int(row[q])) + abs(int(col[p]) - int(col[q]))
    
    return sum

def index_of(n):
    for i in range(9):
        if(n == board[i]):
            return i

def final_index(n):
    for i in range(9):
        if(n == final[i]):
            return i

def swap_board(p, q):
    temp = board[p]
    board[p] = board[q]
    board[q] = temp

    
start()
    
