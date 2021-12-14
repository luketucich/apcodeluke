import pygame
import random


#Starts Pygame
pygame.init()

#Creates the Screen + Size
screen = pygame.display.set_mode((800, 800))

#Changes Background
background = pygame.image.load('meadowthing.jpeg')

#Name of New Window + Icon
pygame.display.set_caption("Hail Hydra")
icon = pygame.image.load('001-hydra.png')
pygame.display.set_icon(icon)

#mainCharacter Location in terms of X,Y
playerImg = pygame.image.load('mainCharacter.png')
playerX = 336
playerY = 600
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('001-shredder.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 200)
enemyX_change = 0.2
enemyY_change = 20

#Fire
fireImg = pygame.image.load('001-fire.png')
fireX = 0
fireY = 600
fireX_change = 0
fireY_change = 10

#"ready"- fire can't be seen
#"shoot"- the fire is moving
fire_state = "ready"

#mainCharacter Location in term of new Window
def player(x,y):
    screen.blit(playerImg, (x, y))

#Knight_Game location in term of window
def enemy(x,y):
    screen.blit(enemyImg, (x, y))

def shoot_bullet(x, y):
    global fire_state
    fire_state = "shoot"
    screen.blit(fireImg,(x + 64, y + 20))

#Game loop to keep it Working
running = True
while running:

   #Scren Color
   screen.fill((0, 0, 0))

   #Background Image
   screen.blit(background,(0, 0))

   #Allows to close the Window
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False

       #Checks what button is pressed to move mainCharacter
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               playerX_change = -0.2
           if event.key == pygame.K_RIGHT:
               playerX_change = 0.2
           if event.key == pygame.K_SPACE:
               shoot_bullet(playerX, fireY)

       if event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0

   #Checks boundaries for mainCharacter
   playerX += playerX_change

   if playerX <= 0:
       playerX = 0
   elif playerX >= 672:
       playerX = 672

   #Enemy Movement
   enemyX += enemyX_change

   if enemyX <= 0:
       enemyX_change = 0.2
       enemyY += enemyY_change
   elif enemyX >= 736:
       enemyX_change = -0.2
       enemyY += enemyY_change

   #Fire Movement
   if fire_state == "fire":
       shoot_bullet(playerX, fireY)
       fireY += fireY_change
    

   player(playerX, playerY)
   enemy(enemyX, enemyY)

   pygame.display.update()