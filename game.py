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
bg = pygame.transform.scale(pygame.image.load('images/background/Background.png'), (SCREEN_WIDTH,SCREEN_HEIGHT))

#Sprites needed for animation
walkRight = [pygame.image.load('images/character_sprites/adventurer-run-00.png'), pygame.image.load('images/character_sprites/adventurer-run-01.png'), pygame.image.load('images/character_sprites/adventurer-run-02.png'), pygame.image.load('images/character_sprites/adventurer-run-03.png'), pygame.image.load('images/character_sprites/adventurer-run-04.png'), pygame.image.load('images/character_sprites/adventurer-run-05.png')]
walkLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-04.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-05.png'),True, False)]
jumpRight = [pygame.image.load('images/character_sprites/adventurer-smrslt-00.png'), pygame.image.load('images/character_sprites/adventurer-smrslt-01.png'), pygame.image.load('images/character_sprites/adventurer-smrslt-02.png'), pygame.image.load('images/character_sprites/adventurer-smrslt-03.png')]
jumpLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-smrslt-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-smrslt-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-smrslt-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-smrslt-03.png'),True, False)]
idle = [pygame.image.load('images/character_sprites/adventurer-idle-2-00.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-01.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-02.png'), pygame.image.load('images/character_sprites/adventurer-idle-2-03.png')]
idleLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-03.png'),True, False)]
attack =  [pygame.image.load('images/character_sprites/adventurer-attack1-00.png'), pygame.image.load('images/character_sprites/adventurer-attack1-01.png'), pygame.image.load('images/character_sprites/adventurer-attack1-02.png'), pygame.image.load('images/character_sprites/adventurer-attack1-03.png'), pygame.image.load('images/character_sprites/adventurer-attack1-04.png'), pygame.image.load('images/character_sprites/adventurer-attack2-00.png'), pygame.image.load('images/character_sprites/adventurer-attack2-01.png'), pygame.image.load('images/character_sprites/adventurer-attack2-02.png'), pygame.image.load('images/character_sprites/adventurer-attack2-03.png'),pygame.image.load('images/character_sprites/adventurer-attack2-04.png'),pygame.image.load('images/character_sprites/adventurer-attack2-05.png'),pygame.image.load('images/character_sprites/adventurer-attack3-00.png'), pygame.image.load('images/character_sprites/adventurer-attack3-01.png'), pygame.image.load('images/character_sprites/adventurer-attack3-02.png'), pygame.image.load('images/character_sprites/adventurer-attack3-03.png'),pygame.image.load('images/character_sprites/adventurer-attack3-04.png'),pygame.image.load('images/character_sprites/adventurer-attack3-05.png')]
attackLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-04.png'),True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-04.png'),True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-05.png'), True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-04.png'),True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-05.png'), True, False)]
shootBow = [pygame.image.load('images/character_sprites/adventurer-bow-00.png'), pygame.image.load('images/character_sprites/adventurer-bow-01.png'), pygame.image.load('images/character_sprites/adventurer-bow-02.png'), pygame.image.load('images/character_sprites/adventurer-bow-03.png'), pygame.image.load('images/character_sprites/adventurer-bow-04.png'), pygame.image.load('images/character_sprites/adventurer-bow-05.png'), pygame.image.load('images/character_sprites/adventurer-bow-06.png'), pygame.image.load('images/character_sprites/adventurer-bow-07.png'), pygame.image.load('images/character_sprites/adventurer-bow-08.png')]    
shootBowLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-03.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-04.png'),True, False), pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-05.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-06.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-07.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-08.png'), True, False)]
airAttack = [pygame.image.load('images/character_sprites/adventurer-air-attack1-00.png'), pygame.image.load('images/character_sprites/adventurer-air-attack1-01.png'), pygame.image.load('images/character_sprites/adventurer-air-attack1-02.png'), pygame.image.load('images/character_sprites/adventurer-air-attack1-03.png')]
airAttackLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-air-attack1-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-air-attack1-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-air-attack1-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-air-attack1-03.png'),True, False)]
crouch = [pygame.image.load('images/character_sprites/adventurer-crouch-00.png'), pygame.image.load('images/character_sprites/adventurer-crouch-01.png'), pygame.image.load('images/character_sprites/adventurer-crouch-02.png'), pygame.image.load('images/character_sprites/adventurer-crouch-03.png')]
crouchLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-crouch-00.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-crouch-01.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-crouch-02.png'),True, False),pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-crouch-03.png'),True, False)]
arrow = [pygame.transform.scale(pygame.transform.rotate(pygame.image.load('images/items/arrow.png'), 90), (30,5))]
arrowLeft = [pygame.transform.scale(pygame.transform.rotate(pygame.image.load('images/items/arrow.png'), -90), (30,5))]

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
        self.right = True
        self.isIdle = True
        self.jpleft = False
        self.jpright = False
        self.isAttack = False
        self.isJump = False
        self.isCrouch = False
        self.isBow= False
        self.crouchCount = 0
        self.walkCount = 0
        self.idleCount = 0
        self.jumpframeCount = 0
        self.attackCount = 0
        self.jpAttackCount = 0
        self.jumpCount = 10
        self.bowCount = 0
        self.ammo = 10
            
    def draw(self, win):
        if self.walkCount + 1 > 18: # 3 frames per walking frame
            self.walkCount = 0
            
        if self.idleCount +1 > 15: # 5 frames per idle frame
            self.idleCount = 0
            
        if self.jumpframeCount +1 > 12:
            self.jumpframeCount = 0
            
        if self.crouchCount +1 > 15:
            self.crouchCount = 0    
            
        if self.jpAttackCount +1 > 9:
            self.jpAttackCount= 0
            
        if self.attackCount +1 >34:
            self.attackCount = 0
        
        if self.bowCount +1> 27:
            self.bowCount = 0
            self.ammo -= 1
        
        if self.left and not self.isJump and not self.isIdle and not self.isAttack and not self.isCrouch and not self.isBow:
            win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
        elif self.right and not self.isJump and not self.isIdle and not self.isAttack and not self.isCrouch and not self.isBow:
            win.blit(walkRight[self.walkCount//3], (self.x,self.y))
            self.walkCount += 1
            
        if self.isJump and self.right and not self.isAttack:
            win.blit(jumpRight[self.jumpframeCount//3], (self.x,self.y))
            self.jumpframeCount +=1
            
        elif self.isJump and self.left and not self.isAttack:
            win.blit(jumpLeft[self.jumpframeCount//3], (self.x,self.y))
            self.jumpframeCount +=1
            
        elif self.isJump and self.right and self.isAttack:
            win.blit(airAttack[self.jpAttackCount//3], (self.x,self.y))
            self.jpAttackCount +=1
            
        elif self.isJump and self.left and self.isAttack:
            win.blit(airAttackLeft[self.jpAttackCount//3], (self.x,self.y))
            self.jpAttackCount +=1
            
        if self.isIdle and self.right and not self.isJump:
            win.blit(idle[self.idleCount//5], (self.x,self.y)) 
            self.idleCount += 1
            
        elif self.isIdle and self.left and not self.isJump:
            win.blit(idleLeft[self.idleCount//5], (self.x,self.y)) 
            self.idleCount += 1
        
        elif self.isIdle and not self.left and not self.right and not self.isJump:
            win.blit(idle[self.idleCount//5], (self.x,self.y)) 
            self.idleCount += 1
            
        if self.isAttack and self.right and not self.isJump:
            win.blit(attack[self.attackCount//2], (self.x,self.y))
            self.attackCount += 1
            
        elif self.isAttack and self.left and not self.isJump:
            win.blit(attackLeft[self.attackCount//2], (self.x,self.y))
            self.attackCount += 1
        
        if self.isCrouch and self.left and not self.isJump and not self.isIdle and not self.isAttack:
            win.blit(crouchLeft[self.crouchCount//5], (self.x,self.y))
            self.crouchCount += 1
            
        elif self.isCrouch and self.right and not self.isJump and not self.isIdle and not self.isAttack:
            win.blit(crouch[self.crouchCount//5], (self.x,self.y))
            self.crouchCount += 1
            
        if self.isBow and self.right and not self.isAttack and not self.isJump and not self.isIdle:
            if self.ammo > 0:
                win.blit(shootBow[self.bowCount//3], (self.x,self.y))
                self.bowCount += 1
            else:
                win.blit(shootBow[self.bowCount//3], (self.x,self.y))
                
        if self.isBow and self.left and not self.isAttack and not self.isJump and not self.isIdle:
            if self.ammo > 0:
                win.blit(shootBowLeft[self.bowCount//3], (self.x,self.y))
                self.bowCount += 1
            else:
                win.blit(shootBow[self.bowCount//3], (self.x,self.y))
                
    def Idle(self):
        self.isIdle = True
        self.walkCount = 0
        self.isAttack = False
        self.isBow = False
        self.bowCount = 0
        self.attackCount = 0
        self.jpAttackCount = 0
        self.jumpframeCount = 0
    
    def Crouch(self):
        self.isIdle = False
        self.isCrouch = True
        self.isAttack = False
        self.isBow = False
        self.bowCount = 0
        self.walkCount = 0
        self.AttackCount = 0
        self.jpAttackCount = 0
        
    def runLeft(self):
        if self.x > self.vel:
            self.x -= self.vel
            self.left = True
            self.right = False
            self.isIdle = False
            self.isAttack = False
            self.isCrouch = False
            self.isBow = False
            self.bowCount = 0
            self.attackCount = 0
            self.jpAttackCount = 0
            self.crouchCount = 0
            
    def runRight (self):
        if self.x < SCREEN_WIDTH-self.width:
            self.x += self.vel
            self.left = False
            self.right = True
            self.isIdle = False
            self.isAttack = False
            self.isCrouch = False
            self.isBow = False
            self.bowCount = 0
            self.attackCount = 0
            self.jpAttackCount = 0
            self.crouchCount = 0
            
    def Jump(self):
        self.isJump=True
        self.isIdle = False
        self.isAttack = False
        self.isCrouch = False
        self.isBow = False
        self.bowCount = 0
        self.walkCount = 0
        self.attackCount = 0
        self.jpAttackCount = 0
        self.crouchCount = 0
        
    def Attack (self):
        self.isAttack = True
        self.isIdle = False
        self.isCrouch = False
        self.isBow = False
        self.bowCount = 0        
        self.crouchCount = 0
        
    def Shoot(self):
        self.isBow = True
        self.isIdle = False
        self.isAttack = False
        self.isCrouch = False
        self.walkCount = 0
        self.attackCount = 0
        self.jpAttackCount = 0
        self.crouchCount = 0
        
#class Projectile (object):
#    def __init__(self,x,y,radius,width,height,facing):
#        self.x = x
#        self.y = y
#        self.radius = radius
#        self.width = width
#        self.height = height
#        self.vel = 15*facing
#    
#    def draw(self, win):
#        if adventurer.right:
#            win.blit(arrow, (self.x, self.y))
#            self.facing = 1
#        if adventurer.left:
#            self.facing = -1
#            win.blit(arrowLeft, (self.x, self.y))


def redrawGameWindow():

    win.blit(bg, (0,0))
    adventurer.draw(win)
    pygame.display.update()     
    #for bullet in bullets:
    #    bullet.draw(win)
#mainloop
adventurer = player (0, SCREEN_HEIGHT-100, 30, 37)
bullets = []
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
#    for bullet in bullets:
#        if bullet.x < SCREEN_WIDTH and bullet.x > 0:
#            bullet.x += bullet.vel
#        else:
#            bullets.pop(bullets.index(bullet))
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        adventurer.runLeft()
        
    elif keys[pygame.K_d]:
        adventurer.runRight()
        
    elif keys [pygame.K_f]:
        adventurer.Attack()

    elif keys [pygame.K_s]:
        adventurer.Crouch()
        
    elif keys [pygame.K_r]:
        adventurer.Shoot()
        
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