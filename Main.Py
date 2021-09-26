import pygame

#Initialize the pygame
pygame.init()

#This creates the screen size
screen = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("Space Fucking Invaders")
icon= pygame.image.load('cat.png')
pygame.display.set_icon(icon)


running = True
#Game Infiite Loop:goes through all the events happening and if the close button has happened as an event the loop
#will change running to false- the loop closes and the program is over. 
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

    #RGB values        
    screen.fill((50, 168, 157)) #cyan
    pygame.display.update()