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
idle = [pygame.image.load('images/character_sprites/adventurer-idle-2-00.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-01.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-02.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-03.png')]
idleLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-03.png'),True, False)]
attack =  [pygame.image.load('images/character_sprites/adventurer-attack1-00.png'), pygame.image.load('images/character_sprites/adventurer-attack1-01.png'), pygame.image.load('images/character_sprites/adventurer-attack1-02.png'), pygame.image.load('images/character_sprites/adventurer-attack1-03.png'), pygame.image.load('images/character_sprites/adventurer-attack1-04.png'), pygame.image.load('images/character_sprites/adventurer-attack2-00.png'), pygame.image.load('images/character_sprites/adventurer-attack2-01.png'), pygame.image.load('images/character_sprites/adventurer-attack2-02.png'), pygame.image.load('images/character_sprites/adventurer-attack2-03.png'),pygame.image.load('images/character_sprites/adventurer-attack2-04.png'),pygame.image.load('images/character_sprites/adventurer-attack2-05.png'),pygame.image.load('images/character_sprites/adventurer-attack3-00.png'), pygame.image.load('images/character_sprites/adventurer-attack3-01.png'), pygame.image.load('images/character_sprites/adventurer-attack3-02.png'), pygame.image.load('images/character_sprites/adventurer-attack3-03.png'),pygame.image.load('images/character_sprites/adventurer-attack3-04.png'),pygame.image.load('images/character_sprites/adventurer-attack3-05.png')]
attackLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-04.png'),True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-04.png'),True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-05.png'), True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-04.png'),True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-05.png'), True, False)]
#airAttack =
#airAttackLeft


clock = pygame.time.Clock()
class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.left = False
        self.right = False
        self.isIdle = True
        self.jpleft = False
        self.jpright = False
        self.isAttack = False
        self.isJump = False
        self.walkCount = 0
        self.idleCount = 0
        self.jumpframeCount = 0
        self.attackCount = 0
        self.jumpCount = 10
        
            
    def draw(self, win):
        if self.walkCount + 1 > 18: # 3 frames per walking frame
            self.walkCount = 0
            
        if self.idleCount +1 > 15: # 5 frames per idle frame
            self.idleCount = 0
            
        if self.jumpframeCount +1 > 9:
            self.jumpframeCount = 0
            
        if self.attackCount +1 >34:
            self.attackCount = 0
            
        if self.left and not self.isJump and not self.isIdle and not self.isAttack:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
        elif self.right and not self.isJump and not self.isIdle and not self.isAttack:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
        if self.isJump and self.right:
            win.blit(jumpRight[self.jumpframeCount//3], (self.x,self.y))
            
        elif self.isJump and self.left:
            win.blit(jumpLeft[self.jumpframeCount//3], (self.x,self.y))
            
        #elif self.isJump and not self.right and not self.left:
        #    win.blit(jumpRight[self.jumpframeCount//3], (self.x,self.y))
            
        if self.isIdle and self.right and not self.isJump:
            win.blit(idle[self.idleCount//5], (self.x,self.y)) 
            self.idleCount += 1
            
        elif self.isIdle and self.left and not self.isJump:
            win.blit(idleLeft[self.idleCount//5], (self.x,self.y)) 
            self.idleCount += 1
        
        elif self.isIdle and not self.left and not self.right and not self.isJump:
            win.blit(idle[self.idleCount//5], (self.x,self.y)) 
            self.idleCount += 1
            
        if self.isAttack and self.right:
            win.blit(attack[self.attackCount//2], (self.x,self.y))
            self.attackCount += 1
            
        if self.isAttack and self.left:
            win.blit(attackLeft[self.attackCount//2], (self.x,self.y))
            self.attackCount += 1
    def Idle(self):
        adventurer.isIdle = True
        adventurer.walkCount = 0
        adventurer.isAttack = False
        self.attackCount = 0
        
    def runLeft(self):
        if adventurer.x > adventurer.vel:
            adventurer.x -= adventurer.vel
            adventurer.left = True
            adventurer.right = False
            adventurer.isIdle = False
            adventurer.isAttack = False
            self.attackCount = 0
            
    def runRight (self):
        if adventurer.x < SCREEN_WIDTH-adventurer.width:
            adventurer.x += adventurer.vel
            adventurer.left = False
            adventurer.right = True
            adventurer.isIdle = False
            adventurer.isAttack = False
            self.attackCount = 0
            
    def Jump(self):
        adventurer.isJump=True
        adventurer.isIdle = False
        adventurer.isAttack = False
        adventurer.walkCount = 0
        self.attackCount = 0
        
    def Attack (self):
        if adventurer.isJump == False:
            adventurer.isAttack = True
            adventurer.isIdle = False

def redrawGameWindow():

    win.blit(bg, (0,0))
    adventurer.draw(win)
    pygame.display.update()     
    
#mainloop
adventurer = player (0, SCREEN_HEIGHT-100, 30, 37)
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        adventurer.runLeft()
        
    elif keys[pygame.K_d]:
        adventurer.runRight()
        
    elif keys [pygame.K_f]:
        adventurer.Attack()

    else:
        adventurer.Idle()
        
    if not(adventurer.isJump):
        if keys[pygame.K_SPACE]:
            adventurer.Jump()
    else:
        if adventurer.jumpCount>= -10:
            adventurer.y -= (adventurer.jumpCount*abs(adventurer.jumpCount))*0.35
            adventurer.jumpCount -= 1
        else:
            adventurer.isJump = False
            adventurer.isAttack = False
            adventurer.isIdle = True
            adventurer.jumpCount = 10
            
    redrawGameWindow()
    
pygame.quit()