import pygame
import random
#Initialize the pygame
pygame.init()

#This creates the screen size
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Samantha Goes To Space")
icon= pygame.image.load('cat.png')
pygame.display.set_icon(icon)

#background
background= pygame.image.load('background.png')

#Playersu
PlayerImg= pygame.image.load('8bit.png')
playerX= 370
playerY= 480
playerX_change = 0

#Enemy
enemyImg= pygame.image.load('squirrel.png')
enemyX= random.randint(0,800)
enemyY= random.randint(50,150)
enemyX_change = 1
enemyY_change = 40


#blit function actually draws the image onto the screen- then you have to plug into the while loop after the rgb display
def player(x,y):
    screen.blit(PlayerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

running = True
#Game Infiite Loop:goes through all the events happening and if the close button has happened as an event the loop
#will change running to false- the loop closes and the program is over. 
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    
    
    #Keystroke event happens- then check what it is. 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.25
            if event.key == pygame.K_RIGHT:
                playerX_change = 2.25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

#RGB values 
    screen.fill((50, 168, 157)) #cyan
#background image
    screen.blit(background,(0,0))

#this is a boundry check 
#player
    playerX += playerX_change
    if playerX <=0:
        playerX=0
    if playerX >= 738:
        playerX=738
#enemy movement
    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 1
        enemyY += enemyY_change
    if enemyX >= 738:
        enemyX_change = -1
        enemyY += enemyY_change
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()


    #x +=right and -=left
    #y +=down and -=up d
