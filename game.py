# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:27:38 2019

@author: Álvaro
"""
import pygame


pygame.init()
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750
win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Wohn Jick')

#Sprites needed for animation
walkRight = [pygame.image.load('images/character_sprites/adventurer-run-00.png'), pygame.image.load('images/character_sprites/adventurer-run-01.png'), pygame.image.load('images/character_sprites/adventurer-run-02.png'), pygame.image.load('images/character_sprites/adventurer-run-03.png'), pygame.image.load('images/character_sprites/adventurer-run-04.png'), pygame.image.load('images/character_sprites/adventurer-run-05.png')]
walkLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-04.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-05.png'),True, False)]
jumpRight = [pygame.image.load('images/character_sprites/adventurer-jump-00.png'), pygame.image.load('images/character_sprites/adventurer-jump-01.png'), pygame.image.load('images/character_sprites/adventurer-jump-02.png'), pygame.image.load('images/character_sprites/adventurer-jump-03.png')]
jumpLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-jump-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-jump-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-jump-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-jump-03.png'),True, False)]
bg = pygame.transform.scale(pygame.image.load('images/background/Background.png'), (SCREEN_WIDTH,SCREEN_HEIGHT))
char = [pygame.image.load('images/character_sprites/adventurer-idle-2-00.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-01.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-02.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-03.png')]

clock = pygame.time.Clock()
class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.jpleft = False
        self.jpright = False
        self.walkCount = 0
        self.idleCount = 0
        self.jumpframeCount = 0
        self.isJump = False
        self.jumpCount = 10
        
            
    def draw(self, win):
        if self.walkCount + 1 > 18: # 3 frames per walking frame
            self.walkCount = 0
            
        if self.idleCount +1 > 15: # 5 frames per idle frame
            self.idleCount = 0
            
        if self.jumpframeCount +1 > 9:
            self.jumpframeCount = 0
            
        if self.left and not self.isJump:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
        elif self.right and not self.isJump:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
        if self.isJump and self.right:
            win.blit(jumpRight[self.jumpframeCount//3], (self.x,self.y))
            
        elif self.isJump and self.left:
            win.blit(jumpLeft[self.jumpframeCount//3], (self.x,self.y))
            
        elif self.isJump and not self.right and not self.left:
            win.blit(jumpRight[self.jumpframeCount//3], (self.x,self.y))
            
        if not self.left and not self.right and not self.isJump:
            win.blit(char[self.idleCount//5], (self.x,self.y)) 
            self.idleCount += 1        
        
#char_width = 30
#char_height = 37
#x = 0
#y = SCREEN_HEIGHT-char_height-60
#char_vel = 10

#left = False
#right = False
#jpleft = False
#jpright = False
#walkCount = 0
#idleCount = 0
#jumpframeCount = 0



def redrawGameWindow():
    '''
    global walkCount
    global idleCount
    global jumpframeCount
    global isJump
    win.blit(bg, (0,0))
    
    if walkCount + 1 > 18: # 3 frames per walking frame
        walkCount = 0
    if idleCount +1 > 15: # 5 frames per idle frame
        idleCount = 0
    if jumpframeCount +1 > 9:
        jumpframeCount = 0
    if left and not isJump:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right and not isJump:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    if isJump and right:
        win.blit(jumpRight[jumpframeCount//3], (x,y))
    elif isJump and left:
        win.blit(jumpLeft[jumpframeCount//3], (x,y))
    elif isJump and not right and not left:
        win.blit(jumpRight[jumpframeCount//3], (x,y))
    if not left and not right and not isJump:
        win.blit(char[idleCount//5], (x,y)) 
        idleCount += 1
    '''
    win.blit(bg, (0,0))
    adventurer.draw(win)
    pygame.display.update()     
    
#mainloop
adventurer = player (0, SCREEN_HEIGHT-100, 30, 37)
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and adventurer.x > adventurer.vel:
        adventurer.x -= adventurer.vel
        adventurer.left = True
        adventurer.right = False
    elif keys[pygame.K_d] and adventurer.x < SCREEN_WIDTH-adventurer.width:
        adventurer.x += adventurer.vel
        adventurer.left = False
        adventurer.right = True
    else:
        adventurer.right = False
        adventurer.left = False
        adventurer.walkCount = 0
        
    if not(adventurer.isJump):
        if keys[pygame.K_SPACE]:
            adventurer.isJump=True
            adventurer.right = False
            adventurer.left = False
            adventurer.walkCount = 0
    else:
        if adventurer.jumpCount>= -10:
            adventurer.y -= (adventurer.jumpCount*abs(adventurer.jumpCount))*0.25
            adventurer.jumpCount -= 1
        else:
            adventurer.isJump = False
            adventurer.jumpCount = 10
            
    redrawGameWindow()
    
pygame.quit()