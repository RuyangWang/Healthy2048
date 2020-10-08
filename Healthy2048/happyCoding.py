import pygame, sys, random

pygame.init()
display_width = 1280
display_height = 720
screen = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)
pygame.display.set_caption("happy 2048!")

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Blue = (0,0,255)
pygame.init()

board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
number = [0,1,2,3]
board[random.choice(number)][random.choice(number)] = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_UP:
                for j in range(0,4):
                    if board[0][j] != 0 or board[1][j] != 0 or board[2][j] != 0 or board[3][j] != 0:
                        if board[0][j] == 0:
                            while board[0][j] == 0:
                                board[0][j] = board[1][j]
                                board[1][j] = board[2][j]
                                board[2][j] = board[3][j]
                                board[3][j] = 0
                        elif board[1][j] == 0 and (board[2][j] != 0 or board[3][j] != 0):
                            while board[1][j] == 0:
                                board[1][j] = board[2][j]
                                board[2][j] = board[3][j]
                                board[3][j] = 0
                        elif board[2][j] == 0 and (board[3][j]!=0):
                            while board[2][j] == 0:
                                board[2][j] = board[3][j]
                                board[3][j] = 0
                for j in range(0,4):
                    if board[0][j] == board[1][j]:
                        board[0][j] = board[0][j] + board[1][j]
                        board[1][j] = board[2][j]
                        board[2][j] = board[3][j]
                        board[3][j] = 0
                    elif board[1][j] == board[2][j]:
                        board[1][j] = board[1][j] + board[2][j]
                        board[2][j] = board[3][j]
                        board[3][j] = 0
                    elif board[2][j] == board[3][j]:
                        board[2][j] = board[2][j] + board[3][j]
                        board[3][j] = 0
            elif event.key == pygame.K_DOWN:
                for j in range(0,4):
                    if board[0][j] != 0 or board[1][j] != 0 or board[2][j] != 0 or board[3][j] != 0:
                        if board[3][j] == 0:
                            while board[3][j] == 0:
                                board[3][j] = board[2][j]
                                board[2][j] = board[1][j]
                                board[1][j] = board[0][j]
                                board[0][j] = 0
                        elif board[2][j] == 0 and (board[1][j] != 0 or board[0][j] != 0):
                            while board[2][j] == 0:
                                board[2][j] = board[1][j]
                                board[1][j] = board[0][j]
                                board[0][j] = 0
                        elif board[1][j] == 0 and board[0][j] != 0:
                            while board[1][j] == 0:
                                board[1][j] = board[0][j]
                                board[0][j] = 0
                for j in range(0,4):
                    if board[3][j] == board[2][j]:
                        board[3][j] = board[3][j] + board[2][j]
                        board[2][j] = board[1][j]
                        board[1][j] = board[0][j]
                        board[0][j] = 0
                    elif board[2][j] == board[1][j]:
                        board[2][j] = board[2][j] + board[1][j]
                        board[1][j] = board[0][j]
                        board[0][j] = 0
                    elif board[1][j] == board[0][j]:
                        board[1][j] = board[1][j] + board[0][j]
                        board[0][j] = 0
            elif event.key == pygame.K_LEFT:
                for i in range(0,4):
                    if board[i][0] != 0 or board[i][1] != 0 or board[i][2] != 0 or board[i][3] != 0:
                        if board[i][0] == 0:
                            while board[i][0] == 0:
                                board[i][0] = board[i][1]
                                board[i][1] = board[i][2]
                                board[i][2] = board[i][3]
                                board[i][3] = 0
                        elif board[i][1] == 0 and (board[i][2]!=0 or board[i][3] != 0):
                            while board[i][1] == 0:
                                board[i][1] = board[i][2]
                                board[i][2] = board[i][3]
                                board[i][3] = 0
                        elif board[i][2] == 0 and (board[i][3] != 0):
                            while board[i][2] == 0:
                                board[i][2] = board[i][3]
                                board[i][3] = 0
                for i in range(0,4):
                    if board[i][0] == board[i][1]:
                        board[i][0] = board[i][0] + board[i][1]
                        board[i][1] = board[i][2]
                        board[i][2] = board[i][3]
                        board[i][3] = 0
                    elif board[i][1] == board[i][2]:
                        board[i][1] = board[i][1] + board[i][2]
                        board[i][2] = board[i][3]
                        board[i][3] = 0
                    elif board[i][2] == board[i][3]:
                        board[i][2] = board[i][2] + board[i][3]
                        board[i][3] = 0
            elif event.key == pygame.K_RIGHT:
                for i in range(0,4):
                    if board[i][0] != 0 or board[i][1] != 0 or board[i][2] != 0 or board[i][3] != 0:
                        if board[i][3] == 0:
                            while board[i][3] == 0:
                                board[i][3] = board[i][2]
                                board[i][2] = board[i][1]
                                board[i][1] = board[i][0]
                                board[i][0] = 0
                        elif board[i][2] == 0 and (board[i][1] != 0 or board[i][0] != 0):
                            while board[i][2] == 0:
                                board[i][2] = board[i][1]
                                board[i][1] = board[i][0]
                                board[i][0]=0
                        elif board[i][1] == 0 and board[i][0] != 0:
                            while board[i][1] == 0:
                                board[i][1] = board[i][0]
                                board[i][0] = 0
                for i in range(0,4):
                    if board[i][3] == board[i][2]:
                        board[i][3] = board[i][3] + board[i][2]
                        board[i][2] = board[i][1]
                        board[i][1] = board[i][0]
                        board[i][0] = 0
                    elif board[i][2] == board[i][1]:
                        board[i][2] = board[i][2] + board[i][1]
                        board[i][1] = board[i][0]
                        board[i][0] = 0
                    elif board[i][1] == board[i][0]:
                        board[i][1] = board[i][1] + board[i][0]
                        board[i][0] = 0
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

    screen.fill(White)

    for x in range (40, 560, 160):
        x += 5
        for y in range (305, 825, 160):
            y += 5
            if board[(x-45)//160][(y-310)//160] == 0:
                pygame.draw.rect(screen,(247,238,214),[y,x,155,155])
            elif board[(x-45)//160][(y-310)//160] == 2:
                img = pygame.image.load("img2.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 4:
                img = pygame.image.load("img4.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 8:
                img = pygame.image.load("img8.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 16:
                img = pygame.image.load("img16.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 32:
                img = pygame.image.load("img32.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 64:
                img = pygame.image.load("img64.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 128:
                img = pygame.image.load("img128.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 256:
                img = pygame.image.load("img256.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 512:
                img = pygame.image.load("img512.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 1024:
                img = pygame.image.load("img1024.jpg")
                screen.blit(img,(y,x))
            elif board[(x-45)//160][(y-310)//160] == 2048:
                img = pygame.image.load("img2048.jpg")
                screen.blit(img,(y,x))

    pygame.display.update()
