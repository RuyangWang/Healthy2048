import random
board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
number = [0,1,2,3]
board[random.choice(number)][random.choice(number)] = 2

def choice(board,playerInput):
    if playerInput == "w":
        for j in range(0,4):
            if board[0][j] != 0 or board[1][j] != 0 or board[2][j] != 0 or board[3][j] != 0:
                if board[0][j] == 0:
                    while board[0][j] == 0:
                        board[0][j] = board[1][j]
                        board[1][j] = board[2][j]
                        board[2][j] = board[3][j]
                        board[3][j] = 0
                if board[1][j] == 0 and (board[2][j] != 0 or board[3][j] != 0):
                    while board[1][j] == 0:
                        board[1][j] = board[2][j]
                        board[2][j] = board[3][j]
                        board[3][j] = 0
                if board[2][j] == 0 and (board[3][j]!=0):
                    while board[2][j] == 0:
                        board[2][j] = board[3][j]
                        board[3][j] = 0
        for j in range(0,4):
            if board[0][j] == board[1][j]:
                board[0][j] = board[0][j] + board[1][j]
                board[1][j] = board[2][j]
                board[2][j] = board[3][j]
                board[3][j] = 0
            if board[1][j] == board[2][j]:
                board[1][j] = board[1][j] + board[2][j]
                board[2][j] = board[3][j]
                board[3][j] = 0
            if board[2][j] == board[3][j]:
                board[2][j] = board[2][j] + board[3][j]
                board[3][j] = 0

    elif playerInput == "s":
        for j in range(0,4):
            if board[0][j] != 0 or board[1][j] != 0 or board[2][j] != 0 or board[3][j] != 0:
                if board[3][j] == 0:
                    while board[3][j] == 0:
                        board[3][j] = board[2][j]
                        board[2][j] = board[1][j]
                        board[1][j] = board[0][j]
                        board[0][j] = 0
                if board[2][j] == 0 and (board[1][j] != 0 or board[0][j] != 0):
                    while board[2][j] == 0:
                        board[2][j] = board[1][j]
                        board[1][j] = board[0][j]
                        board[0][j] = 0
                if board[1][j] == 0 and board[0][j] != 0:
                    while board[1][j] == 0:
                        board[1][j] = board[0][j]
                        board[0][j] = 0
        for j in range(0,4):
            if board[3][j] == board[2][j]:
                board[3][j] = board[3][j] + board[2][j]
                board[2][j] = board[1][j]
                board[1][j] = board[0][j]
                board[0][j] = 0
            if board[2][j] == board[1][j]:
                board[2][j] = board[2][j] + board[1][j]
                board[1][j] = board[0][j]
                board[0][j] = 0
            if board[1][j] == board[0][j]:
                board[1][j] = board[1][j] + board[0][j]
                board[0][j] = 0

    elif playerInput == "a":
        for i in range(0,4):
            if board[i][0] != 0 or board[i][1] != 0 or board[i][2] != 0 or board[i][3] != 0:
                if board[i][0] == 0:
                    while board[i][0] == 0:
                        board[i][0] = board[i][1]
                        board[i][1] = board[i][2]
                        board[i][2] = board[i][3]
                        board[i][3] = 0
                if board[i][1] == 0 and (board[i][2]!=0 or board[i][3] != 0):
                    while board[i][1] == 0:
                        board[i][1] = board[i][2]
                        board[i][2] = board[i][3]
                        board[i][3] = 0
                if board[i][2] == 0 and (board[i][3] != 0):
                    while board[i][2] == 0:
                        board[i][2] = board[i][3]
                        board[i][3] = 0
        for i in range(0,4):
            if board[i][0] == board[i][1]:
                board[i][0] = board[i][0] + board[i][1]
                board[i][1] = board[i][2]
                board[i][2] = board[i][3]
                board[i][3] = 0
            if board[i][1] == board[i][2]:
                board[i][1] = board[i][1] + board[i][2]
                board[i][2] = board[i][3]
                board[i][3] = 0
            if board[i][2] == board[i][3]:
                board[i][2] = board[i][2] + board[i][3]
                board[i][3] = 0

    elif playerInput == "d":
        for i in range(0,4):
            if board[i][0] != 0 or board[i][1] != 0 or board[i][2] != 0 or board[i][3] != 0:
                if board[i][3] == 0:
                    while board[i][3] == 0:
                        board[i][3] = board[i][2]
                        board[i][2] = board[i][1]
                        board[i][1] = board[i][0]
                        board[i][0] = 0
                if board[i][2] == 0 and (board[i][1] != 0 or board[i][0] != 0):
                    while board[i][2] == 0:
                        board[i][2] = board[i][1]
                        board[i][1] = board[i][0]
                        board[i][0]=0
                if board[i][1] == 0 and board[i][0] != 0:
                    while board[i][1] == 0:
                        board[i][1] = board[i][0]
                        board[i][0] = 0
        for i in range(0,4):
            if board[i][3] == board[i][2]:
                board[i][3] = board[i][3] + board[i][2]
                board[i][2] = board[i][1]
                board[i][1] = board[i][0]
                board[i][0] = 0
            if board[i][2] == board[i][1]:
                board[i][2] = board[i][2] + board[i][1]
                board[i][1] = board[i][0]
                board[i][0] = 0
            if board[i][1] == board[i][0]:
                board[i][1] = board[i][1] + board[i][0]
                board[i][0] = 0

def playAgain():
    return input(print("Play again? (y or n)")).lower()

print("")
print("Happy 2048!","\n")
print("Rule: 'w' for upwards, 's' for downwards, 'a' to the left, 'd' to the right, and 'quit' to quit :D")

while True:
    done = False
    print('')
    print(board[0][0],"\t",board[0][1],"\t",board[0][2],"\t",board[0][3],"\n")
    print(board[1][0],"\t",board[1][1],"\t",board[1][2],"\t",board[1][3],"\n")
    print(board[2][0],"\t",board[2][1],"\t",board[2][2],"\t",board[2][3],"\n")
    print(board[3][0],"\t",board[3][1],"\t",board[3][2],"\t",board[3][3],"\n")

    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == 2048:
                print("Yeah! You won!")
                done = True

    playerInput = input("")
    if playerInput == ('quit'):
        break

    choice(board,playerInput)
    listfori = []
    listforj = []
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j]==0:
                count+=1
                listfori.append(i)
                listforj.append(j)
    if count > 0:
        randomNumber = random.randint(0,len(listfori) - 1)
        board[listfori[randomNumber]][listforj[randomNumber]] = 2
    else:
        print("Oops! You lost!")
        done = True

    if done == True:
        if playAgain() == "y":
            board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
            number = [0,1,2,3]
            board[random.choice(number)][random.choice(number)] = 2
            done = False
        else:
            break
