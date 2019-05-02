"""
This module is used to hold the Player class. The Player represents the user-
controlled sprite on the screen.
"""
import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_L = []
    walking_frames_R = []
    jump_frames_L = []
    jump_frames_R = []
    idle_frames_L = []
    idle_frames_R = []
    attack_frames_L = []
    attack_frames_R = []
    shoot_bow_frames_L = []
    shoot_bow_frames_R = []
    air_attack_frames_L = []
    air_attack_frames_R = []
    crouch_frames_L = []
    crouch_frames_R = []
    arrow_frames_L = []
    arrow_frames_R = []

    # What direction is the player facing?

    # List of sprites we can bump against
    level = None

    # -- Methods
    def __init__(self):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        
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
        self.jumpCount = 0
        self.attackCount = 0
        self.airAttackCount = 0
        self.jumpCount = 10
        self.bowCount = 0
        self.ammo = 10
        
        walkRight = [pygame.image.load('images/character_sprites/adventurer-run-00.png'), 
                     pygame.image.load('images/character_sprites/adventurer-run-01.png'), 
                     pygame.image.load('images/character_sprites/adventurer-run-02.png'), 
                     pygame.image.load('images/character_sprites/adventurer-run-03.png'), 
                     pygame.image.load('images/character_sprites/adventurer-run-04.png'), 
                     pygame.image.load('images/character_sprites/adventurer-run-05.png')]
        for i in walkRight:
            self.walking_frames_R.append(i)
        
        walkLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-00.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-01.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-02.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-03.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-04.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-run-05.png'),True, False)]
        for i in walkLeft:    
            self.walking_frames_L.append(i)
            
        jumpRight = [pygame.image.load('images/character_sprites/adventurer-smrslt-00.png'), 
                     pygame.image.load('images/character_sprites/adventurer-smrslt-01.png'), 
                     pygame.image.load('images/character_sprites/adventurer-smrslt-02.png'), 
                     pygame.image.load('images/character_sprites/adventurer-smrslt-03.png')]
        for i in jumpRight:
            self.jump_frames_R.append(i)
        
        jumpLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-smrslt-00.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-smrslt-01.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-smrslt-02.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-smrslt-03.png'),True, False)]
        for i in jumpLeft:
            self.jump_frames_L.append(i)

        idle = [pygame.image.load('images/character_sprites/adventurer-idle-2-00.png'), 
                pygame.image.load('images/character_sprites/adventurer-idle-2-01.png'), 
                pygame.image.load('images/character_sprites/adventurer-idle-2-02.png'), 
                pygame.image.load('images/character_sprites/adventurer-idle-2-03.png')]
        for i in idle:
            self.idle_frames_R.append(i)
        
        idleLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-00.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-01.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-02.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-idle-2-03.png'),True, False)]
        for i in idleLeft:
            self.idle_frames_L.append(i)
        
        attack =  [pygame.image.load('images/character_sprites/adventurer-attack1-00.png'),
                   pygame.image.load('images/character_sprites/adventurer-attack1-01.png'),
                   pygame.image.load('images/character_sprites/adventurer-attack1-02.png'), 
                   pygame.image.load('images/character_sprites/adventurer-attack1-03.png'), 
                   pygame.image.load('images/character_sprites/adventurer-attack1-04.png'), 
                   pygame.image.load('images/character_sprites/adventurer-attack2-00.png'), 
                   pygame.image.load('images/character_sprites/adventurer-attack2-01.png'), 
                   pygame.image.load('images/character_sprites/adventurer-attack2-02.png'), 
                   pygame.image.load('images/character_sprites/adventurer-attack2-03.png'),
                   pygame.image.load('images/character_sprites/adventurer-attack2-04.png'),
                   pygame.image.load('images/character_sprites/adventurer-attack2-05.png'),
                   pygame.image.load('images/character_sprites/adventurer-attack3-00.png'), 
                   pygame.image.load('images/character_sprites/adventurer-attack3-01.png'),
                   pygame.image.load('images/character_sprites/adventurer-attack3-02.png'), 
                   pygame.image.load('images/character_sprites/adventurer-attack3-03.png'),
                   pygame.image.load('images/character_sprites/adventurer-attack3-04.png'),
                   pygame.image.load('images/character_sprites/adventurer-attack3-05.png')]
        for i in attack:
            self.attack_frames_R.append(i)
        
        attackLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-00.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-01.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-02.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-03.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack1-04.png'),True, False), 
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-00.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-01.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-02.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-03.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-04.png'),True, False), 
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack2-05.png'),True, False), 
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-00.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-01.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-02.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-03.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-04.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-attack3-05.png'),True, False)]
        for i in attackLeft:
            self.attack_frames_L.append(i)
        
        shootBow = [pygame.image.load('images/character_sprites/adventurer-bow-00.png'), 
                    pygame.image.load('images/character_sprites/adventurer-bow-01.png'), 
                    pygame.image.load('images/character_sprites/adventurer-bow-02.png'), 
                    pygame.image.load('images/character_sprites/adventurer-bow-03.png'), 
                    pygame.image.load('images/character_sprites/adventurer-bow-04.png'), 
                    pygame.image.load('images/character_sprites/adventurer-bow-05.png'),
                    pygame.image.load('images/character_sprites/adventurer-bow-06.png'), 
                    pygame.image.load('images/character_sprites/adventurer-bow-07.png'), 
                    pygame.image.load('images/character_sprites/adventurer-bow-08.png')]    
        for i in shootBow:
            self.shoot_bow_frames_R.append(i)
        
        shootBowLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-00.png'),True, False),
                        pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-01.png'),True, False),
                        pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-02.png'),True, False),
                        pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-03.png'),True, False),
                        pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-04.png'),True, False), 
                        pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-05.png'),True, False),
                        pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-06.png'),True, False),
                        pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-07.png'),True, False),
                        pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-bow-08.png'), True, False)]
        for i in shootBowLeft:
            self.shoot_bow_frames_L.append(i)
        
        airAttack = [pygame.image.load('images/character_sprites/adventurer-air-attack1-00.png'), 
                     pygame.image.load('images/character_sprites/adventurer-air-attack1-01.png'), 
                     pygame.image.load('images/character_sprites/adventurer-air-attack1-02.png'), 
                     pygame.image.load('images/character_sprites/adventurer-air-attack1-03.png')]
        for i in airAttack:
            self.air_attack_frames_R.append(i)
        
        airAttackLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-air-attack1-00.png'),True, False),
                         pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-air-attack1-01.png'),True, False),
                         pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-air-attack1-02.png'),True, False),
                         pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-air-attack1-03.png'),True, False)]
        for i in airAttackLeft:
            self.air_attack_frames_L.append(i)
        
        crouch = [pygame.image.load('images/character_sprites/adventurer-crouch-00.png'), 
                  pygame.image.load('images/character_sprites/adventurer-crouch-01.png'), 
                  pygame.image.load('images/character_sprites/adventurer-crouch-02.png'), 
                  pygame.image.load('images/character_sprites/adventurer-crouch-03.png')]
        for i in crouch:
            self.crouch_frames_R.append(i)
        
        crouchLeft = [pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-crouch-00.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-crouch-01.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-crouch-02.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/character_sprites/adventurer-crouch-03.png'),True, False)]
        for i in crouchLeft:
            self.crouch_frames_L.append(i)
        
        arrow = [pygame.transform.scale(pygame.transform.rotate(pygame.image.load('images/items/arrow.png'), 90), (30,5))]
        for i in arrow:
            self.arrow_frames_R.append(i)
        
        arrowLeft = [pygame.transform.scale(pygame.transform.rotate(pygame.image.load('images/items/arrow.png'), -90), (30,5))]
        for i in arrowLeft:
            self.arrow_frames_L.append(i)


        # Set the image the player starts with
        self.image = self.idle_frames_R[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()

    def update(self, screen):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        
        if self.walkCount + 1 > 18: # 3 frames per walking frame
            self.walkCount = 0
            
        if self.idleCount +1 > 15: # 5 frames per idle frame
            self.idleCount = 0
            
        if self.jumpCount +1 > 12:
            self.jumpCount = 0
            
        if self.crouchCount +1 > 15:
            self.crouchCount = 0    
            
        if self.airAttackCount +1 > 9:
            self.airAttackCount= 0
            
        if self.attackCount +1 >34:
            self.attackCount = 0
        
        if self.bowCount +1> 27:
            self.bowCount = 0
            self.ammo -= 1
        
        self.rect.x += self.change_x
        
        #Right Movements
            
        if self.isIdle and self.right and not self.isJump:
            self.image = self.idle_frames_R[self.idleCount//5]
            self.idleCount += 1
        
        elif self.right and not self.isJump and not self.isIdle and not self.isAttack and not self.isCrouch and not self.isBow:
            self.image = self.walking_frames_R[self.walkCount//3] 
            self.walkCount += 1
            
        elif self.isJump and self.right and not self.isAttack:
            self.image = self.jump_frames_R[self.jumpCount//3] 
            self.jumpCount +=1
        
        elif self.isJump and self.right and self.isAttack:
            self.image = self.air_attack_frames_R[self.airAttackCount//3] 
            self.airAttackCount +=1
            
        elif self.isAttack and self.right and not self.isJump:
            self.image = self.attack_frames_R[self.attackCount//2]
            self.attackCount += 1
            
        elif self.isCrouch and self.right and not self.isJump and not self.isIdle and not self.isAttack:
            self.image = self.crouch_frames_R[self.crouchCount//5] 
            self.crouchCount += 1
            
        elif self.isBow and self.right and not self.isAttack and not self.isJump and not self.isIdle:
            if self.ammo > 0:
                self.image = self.shoot_bow_frames_R[self.bowCount//3] 
                self.bowCount += 1
            else:
                self.image = self.idle_frames_R[self.bowCount//3] 
                
        #Left Movements            
        
        if self.isIdle and self.left and not self.isJump:
            self.image = self.idle_frames_L[self.idleCount//5] 
            self.idleCount += 1
            
        elif self.left and not self.isJump and not self.isIdle and not self.isAttack and not self.isCrouch and not self.isBow:
            self.image = self.walking_frames_L[self.walkCount//3]  
            self.walkCount += 1
        
        elif self.isJump and self.left and not self.isAttack:
            self.image = self.jump_frames_L[self.jumpCount//3] 
            self.jumpCount +=1
    
        elif self.isJump and self.left and self.isAttack:
            self.image = self.air_attack_frames_L[self.airAttackCount//3] 
            self.airAttackCount +=1
    
        elif self.isAttack and self.left and not self.isJump:
            self.image = self.attack_frames_L[self.attackCount//2] 
            self.attackCount += 1
    
        elif self.isCrouch and self.left and not self.isJump and not self.isIdle and not self.isAttack:
            self.image = self.crouch_frames_L[self.crouchCount//5] 
            self.crouchCount += 1
    
        elif self.isBow and self.left and not self.isAttack and not self.isJump and not self.isIdle:
            if self.ammo > 0:
                self.image = self.shoot_bow_frames_L[self.bowCount//3] 
                self.bowCount += 1
            else:
                self.image = self.idle_frames_L[self.bowCount//3] 
        

        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
                
# =============================================================================
#         #Check to see if enemy hits us
#         enemy_hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
#         for enemy in enemy_hit_list:
#             if 
# =============================================================================
        
    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height
            self.isJump = False
            self.isAttack = False
            self.isIdle = True

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -20
            self.isJump = False
            self.isAttack = False
            self.isIdle = True


        self.isJump=True
        self.isIdle = False
        self.isAttack = False
        self.isCrouch = False
        self.isBow = False
        self.bowCount = 0
        self.walkCount = 0
        self.attackCount = 0
        self.crouchCount = 0

    def Idle(self):
        self.change_x = 0
        self.isIdle = True
        self.walkCount = 0
        self.isAttack = False
        self.isBow = False
        self.bowCount = 0
        self.attackCount = 0
        self.airAttackCount = 0
        self.jumpCount = 0
    
    def Crouch(self):
        self.isIdle = False
        self.isCrouch = True
        self.isAttack = False
        self.isBow = False
        self.bowCount = 0
        self.walkCount = 0
        self.AttackCount = 0
        self.airAttackCount = 0
        
    def RunLeft(self):
        self.change_x = -10
        self.left = True
        self.right = False
        self.isIdle = False
        self.isAttack = False
        self.isCrouch = False
        self.isBow = False
        self.bowCount = 0
        self.attackCount = 0
        self.airAttackCount = 0
        self.crouchCount = 0
        
            
    def RunRight (self):
        self.change_x = 10
        self.left = False
        self.right = True
        self.isIdle = False
        self.isAttack = False
        self.isCrouch = False
        self.isBow = False
        self.bowCount = 0
        self.attackCount = 0
        self.airAttackCount = 0
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
        self.airAttackCount = 0
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
        self.airAttackCount = 0
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
#    def draw(self, screen):
#        if adventurer.right:
#            screen.blit(arrow, (self.x, self.y))
#            self.facing = 1
#        if adventurer.left:
#            self.facing = -1
#            screen.blit(arrowLeft, (self.x, self.y))
