import pygame
import numpy as np
import sys
import random
from copy import deepcopy

pygame.init()
size = 100
screen = pygame.display.set_mode((size*3, size*3 + 50))
pygame.display.set_caption("Tic-Tac-Toe")

board = np.zeros((3,3), dtype=int)
winningCoordinates = np.zeros((2,2), dtype=int)

def SMPlayer():
    pygame.draw.rect(screen, (192,192,192), (0,0, size*3, size*3+50))
    pygame.draw.rect(screen, (0,0,0), (25,25,250,100), 5)
    pygame.draw.rect(screen, (0,0,0), (25,150,250,100) , 5)
    fonta = pygame.font.SysFont("arial", 50)
    single = fonta.render("Vs Comp.", 1 , (0,0,0))
    multi = fonta.render("Vs Player", 1, (0,0,0))
    screen.blit(single, (40,30))
    screen.blit(multi, (40, 160))
    pygame.display.update()
    
    

def drawBorder():
    pygame.draw.line(screen, (0, 0, 0), (0, 100), (300, 100))
    pygame.draw.line(screen, (0, 0, 0), (0, 200), (300, 200))
    pygame.draw.line(screen, (0, 0, 0), (100, 0), (100, 300))
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 300))



def isValidLocation(board, col, row):
    if board[row][col] != 0:
        return False
    return True


def fill(board, col, row, piece):
    board[row][col] = piece


def compMove():
    global board
    possibleMoves = [[i,j] for i in range (3) for j in range (3) if board[i][j] == 0]
    print("Possiblr moves : ", possibleMoves)
    move = False
    
    for let in [2, 1]:              # First checking for winning move of player and computer if possible
        for pos in possibleMoves:
            boardCopy = deepcopy(board)        # Copying the board and not just giving another name ref
        
            boardCopy[pos[0]][pos[1]] = let

            for r in range(3):
                if (boardCopy[r][0] == let and boardCopy[r][1] == let and boardCopy[r][2] == let) or (boardCopy[0][r] == let and boardCopy[1][r] == let and boardCopy[2][r] == let):
                    move = pos
                    return move
            if (boardCopy[0][0] == let and boardCopy[1][1]==let and boardCopy[2][2] == let) or (boardCopy[2][0] == let and boardCopy[1][1] == let and boardCopy[0][2] == let):
                move = pos
                return move


    corners = []        # Second filling corners
    for pos in possibleMoves:
        if pos in [[0,0], [0,2], [2,0], [2,2]]:
            corners.append(pos)
    if len(corners) > 0:
        move = random.choice(corners)
        return move


    if [1,1] in possibleMoves:          # Third for center
        move = [1,1]
        return move
    

    edges = []              # Fourth for the edges
    for pos in possibleMoves:
        if pos in [[0,1], [1,0], [1,2], [2,1]]:
            edges.append(pos)
    if len(edges) > 0:
        move = random.choice(edges)
        return move

    return move


def winningMove(board, piece):
    global winningCoordinates
    for r in range(3):
        if board[r][0] == piece and board[r][1] == piece and board[r][2] == piece:
            winningCoordinates[0][0] = r*size + 60
            winningCoordinates[0][1] = 0*size + 25
            winningCoordinates[1][0] = r*size + 60
            winningCoordinates[1][1] = 2*size + 75
            return True

        if board[0][r] == piece and board[1][r] == piece and board[2][r] == piece:
            winningCoordinates[0][0] = 0*size + 25
            winningCoordinates[0][1] = r*size + 52
            winningCoordinates[1][0] = 2*size + 75
            winningCoordinates[1][1] = r*size + 52
            return True
    
    if board[0][0] == piece and board[1][1]==piece and board[2][2] == piece:
        winningCoordinates[0][0] = 0*size + 25
        winningCoordinates[0][1] = 0*size + 25
        winningCoordinates[1][0] = 2*size + 85
        winningCoordinates[1][1] = 2*size + 75
        return True

    if board[2][0] == piece and board[1][1] == piece and board[0][2] == piece:
        winningCoordinates[0][0] = 2*size + 80
        winningCoordinates[0][1] = 0*size + 25
        winningCoordinates[1][0] = 0*size + 25
        winningCoordinates[1][1] = 2*size + 80
        return True

    if 0 not in board:          # The DRAW condition
        drawBoard(board)
        drawBorder()
        pygame.display.update()
        turn = 1
        pygame.time.wait(1000)
        restart()

    return False


def winningAction(board):
    drawBoard(board)
    drawBorder()
    pygame.draw.line(screen, (255,0,0), (winningCoordinates[0][1],winningCoordinates[0][0]), (winningCoordinates[1][1],winningCoordinates[1][0]), 7)
    pygame.display.update()
    pygame.time.wait(2000)

    restart()
    #pygame.draw.rect(screen, (192, 192, 192), (0,0, 300, 300))
    #label = font.render("X wins !!!", 1, (255,0,0))
    #screen.blit(label, (10,40))


def drawBoard(board):
    for c in range(3):
        for r in range(3):
            if board[r][c] == 1:
                text = font.render("X", 1, (0,0,0))
                screen.blit(text, (int(c*size+25), int(r*size+25)))
            elif board[r][c] == 2 :
                pygame.draw.circle(screen, (0,0,0), (int(c*size+50), int(r*size+50)), radius, 5)
    
    score = scoreFont.render(" X : {}    O : {}".format(SCOREX, SCOREO), 1 , (0,0,0))
    screen.blit(score, (2, 300))


def restart():
    global board, turn, winningCoordinates
    board = np.zeros((3,3), dtype=int)
    
    #turn = 0                       # Always X starts the new game
    turn += 1                       # Last time's winner starts the next game
    turn = turn % 2

    winningCoordinates = np.zeros((2,2), dtype=int)

    pygame.draw.rect(screen, (192, 192, 192), (0,0, 300, 300))
    drawBorder()
    pygame.display.update()


font = pygame.font.SysFont("monosspace", 120)
scoreFont = pygame.font.SysFont("arial", 40)
turn = 0
radius = 30
SCOREX = 0
SCOREO = 0

computerPlay = None
print(computerPlay)

while True:
    
    if computerPlay == None:
        SMPlayer()

    screen.fill((192, 192, 192))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
           
            if computerPlay == None:
                pos = pygame.mouse.get_pos()
                if pos[0] > 25 and pos[0]<250 and pos[1]>25 and pos[1]<100:
                    computerPlay =  True
                elif pos[0] > 25 and pos[0]<250 and pos[1]>150 and pos[1]<200:
                    computerPlay = False
                continue


            # PLAYER 1 TURN
            if turn == 0:
                pos = pygame.mouse.get_pos()
                
                posx = pos[0]
                posy = pos[1]
                print("Player : ",pos, posx, posy)
                if isValidLocation(board, posx//size, posy//size):
                    fill(board, posx//size, posy//size, 1)
                    turn += 1
                    turn = turn % 2
                    
                    if winningMove(board, 1) :
                        winningAction(board)
                        SCOREX += 1
                        
                print(board)

            # PLAYER 2 TURN
            elif turn == 1 and computerPlay == False:
               
                posx = event.pos[0]
                posy = event.pos[1]

                if isValidLocation(board, posx//size, posy//size):
                    fill(board, posx//size, posy//size, 2)
                    turn += 1
                    turn = turn % 2
                    
                    if winningMove(board, 2) :
                        winningAction(board)
                        SCOREO += 1
                print(board)

        # Automated Play
        if computerPlay == True and turn == 1:
            position = compMove()
            print("Computer move: ",position)
            
            fill(board, position[1], position[0], 2)
            turn += 1
            turn = turn % 2
                    
            if winningMove(board, 2) :
                winningAction(board)
                SCOREO += 1
            print(board)

    if computerPlay != None:
        drawBorder()
        drawBoard(board)
    pygame.display.update()




