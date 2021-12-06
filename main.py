import os

PLAYER1 = "o"
PLAYER2 = "x"

WIDTH = 6
HEIGHT = 7

dir = [(1,0), (0,1), (1,1)]

blk = [[" " for j in range(WIDTH)] for i in range(HEIGHT)]
available_inputs = range(WIDTH)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def print_board():
    clearConsole()
    global blk
    for i in range(HEIGHT):
        print("".join(blk[i]))
    print("-" * WIDTH)
    print("".join(map(str,range(WIDTH))))

def add_stone(num:int, player):
    global blk
    for i in range(HEIGHT - 1,-1,-1):
        if blk[i][num] == " ":
            blk[i][num] = player
            break
    

def check_win(player):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            for dx,dy in dir:
                y = i
                x = j
                cnt = 0
                for _ in range(4):
                    if blk[y][x] == player:
                        cnt += 1
                    y += dy
                    x += dx
                    if y == HEIGHT or x == WIDTH:
                        break
                if cnt == 4:
                    return True
    return False
                    


player = PLAYER1
print_board()
while(True):
    num = int(input())

    add_stone(num,player)
    print_board()
    if check_win(player):
        break
    player = PLAYER1 if player == PLAYER2 else PLAYER2 

print(player + "  Win!!")