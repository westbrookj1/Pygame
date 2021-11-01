import pygame
import random
import math

from pygame import mixer

#Initialize the pygame
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.
#This creates the screen size
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Samantha Goes To Space")
icon= pygame.image.load('cat.png')
pygame.display.set_icon(icon)

#background
background= pygame.image.load('landscape.jpg')

#background sound
#mixer.music.load('')
#mixer.music.play(-1)

#Playersu
PlayerImg= pygame.image.load('8bit.png')
playerX= 370
playerY= 480
playerX_change = 0

#Enemy
enemyImg= []
enemyX= []
enemyY =[]
enemyX_change= []
enemyY_change= []
numOfEnemies=6

for i in range(numOfEnemies):
    enemyImg.append(pygame.image.load('squirrel.png'))
    enemyX.append(random.randint(0,737))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(.75)
    enemyY_change.append(40)

#Basic Bullet
basicbulletImg= pygame.image.load('bullet.png')
basicbulletX= 0
basicbulletY= 480 #has to match the y value of the spaceship because that is where it launches from 
basicbulletX_change =  .75
basicbulletY_change = .75
basicbullet_state = "ready" #ready is at rest, fire means its moving

#score
scoreValue=0
font = pygame.font.Font('freesansbold.ttf',16)

textX =10
textY =10

#gameOver
over_font =pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render("Score:"+ str(scoreValue),True, (255,255,255))
    screen.blit(score,(x,y))
def gameOverText():
    over_text=over_font.render("GAME OVER",True, (255,255,255))
    screen.blit(over_text,(200,250))

#blit function actually draws the image onto the screen- then you have to plug into the while loop after the rgb display
def player(x,y):
    screen.blit(PlayerImg,(x,y))

def enemy(x,y, i):
    screen.blit(enemyImg[i],(x,y))

def fire_basicbullet(x,y):
    global basicbullet_state
    basicbullet_state = "fire"
    screen.blit(basicbulletImg,(x+16,y+10)) #adding the values to x and y to smidge the appearence of the bullet

def isCollision(enemyX,enemyY,basicbulletX,basicBulletY):
    distance= math.sqrt(((math.pow(enemyX-basicbulletX,2)))+(math.pow(enemyY-basicBulletY,2)))
    if distance <27:
        return True
    else:    
        return False

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
                playerX_change = -1.00
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.00
            if event.key == pygame.K_SPACE:
                if basicbullet_state is "ready":
                    bullet_Sound= mixer.Sound("bullet.wav")
                    bullet_Sound.play()
                    basicbulletX=playerX
                    fire_basicbullet(basicbulletX,basicbulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
#RGB values 
    screen.fill((50, 168, 157)) #cyan

#background image
    screen.blit(background,(0,0))

#bullet movement
    if basicbulletY <=0:
        basicbulletY =480
        basicbullet_state ="ready"
    if basicbullet_state is "fire":
        fire_basicbullet(basicbulletX,basicbulletY)
        basicbulletY -= basicbulletY_change

#this is a boundry check 

#player
    playerX += playerX_change
    if playerX <=0:
        playerX=0
    if playerX >= 738:
        playerX=738
#enemy movement
    for i in range(numOfEnemies):
        #Game over
        if enemyY[i] >440:
            for j in range(numOfEnemies):
                enemyY[j]=2000
            gameOverText()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = .25
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 738:
            enemyX_change[i] = -.25
            enemyY[i] += enemyY_change[i]
#collision
        collision=isCollision(enemyX[i],enemyY[i],basicbulletX,basicbulletY)
        if collision:
            explosion_Sound= mixer.Sound("EnemyDestroyed.wav")
            explosion_Sound.play()
            basicbulletY= 480
            basicbullet_state ="ready"
            scoreValue+=100
            enemyX[i]= random.randint(0,737)
            enemyY[i]= random.randint(50,150)
        enemy(enemyX[i],enemyY[i], i)
    show_score(textX,textY)       
    
    player(playerX,playerY)
    
    pygame.display.update()
    
    


    #x +=right and -=left
    #y +=down and -=up dd
