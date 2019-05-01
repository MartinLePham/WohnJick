import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
class Enemy_Bandit(pygame.sprite.Sprite):
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
    direction = "R"

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
        
        walkRight = [pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_001.png'), 
                     pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_002.png'), 
                     pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_003.png'), 
                     pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_004.png'), 
                     pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_005.png'), 
                     pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_006.png'),
                     pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_007.png'),
                     pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_008.png')]
        for i in walkRight:
            self.walking_frames_R.append(i)
        
        walkLeft = [pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_001.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_002.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_003.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_004.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_005.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_006.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_007.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Running/Bandit_Running_008.png'),True, False)]
        for i in walkLeft:    
            self.walking_frames_L.append(i)

        idle = [pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_001.png'), 
                pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_002.png'), 
                pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_003.png'), 
                pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_004.png'),
                pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_005.png'),
                pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_006.png')]
        for i in idle:
            self.idle_frames_R.append(i)
        
        idleLeft = [pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_001.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_002.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_003.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_004.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_005.png'),True, False),
                    pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit Idle/Bandit_Idle_006.png'),True, False)]
        for i in idleLeft:
            self.idle_frames_L.append(i)
        
        attack =  [pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_001.png'),
                   pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_002.png'),
                   pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_003.png'), 
                   pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_004.png'), 
                   pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_005.png'), 
                   pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_006.png'), 
                   pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_007.png')]
        for i in attack:
            self.attack_frames_R.append(i)
        
        attackLeft = [pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_001.png'),True, False),
                      pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_002.png'),True, False),
                      pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_003.png'),True, False),
                      pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_004.png'),True, False),
                      pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_005.png'),True, False), 
                      pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_006.png'),True, False),
                      pygame.transform.flip(pygame.image.load('/Users/rachelengelbrecht/Desktop/Bandit_Attack/Bandit_Attack_007.png'),True, False)]
        for i in attackLeft:
            self.attack_frames_L.append(i)

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
                        
        if self.airAttackCount +1 > 9:
            self.airAttackCount= 0
            
        if self.attackCount +1 >34:
            self.attackCount = 0
        
        
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        
        #Right Movements
        if self.direction == "R":
            
            if self.isIdle and self.right and not self.isJump:
                self.image = self.idle_frames_R[self.idleCount//5]
                self.idleCount += 1
            
            elif self.right and not self.isJump and not self.isIdle and not self.isAttack and not self.isCrouch and not self.isBow:
                self.image = self.walking_frames_R[self.walkCount//3] 
                self.walkCount += 1
             
            elif self.isAttack and self.right and not self.isJump:
                self.image = self.attack_frames_R[self.attackCount//2]
                self.attackCount += 1
                else:
                    self.image = self.idle_frames_R[self.bowCount//3] 
                    
        #Left Movements            
        else:
            
            if self.isIdle and self.left and not self.isJump:
                self.image = self.idle_frames_L[self.idleCount//5] 
                self.idleCount += 1
                
        
            elif self.isJump and self.left and self.isAttack:
                self.image = self.air_attack_frames_L[self.airAttackCount//3] 
                self.airAttackCount +=1
        
            elif self.isAttack and self.left and not self.isJump:
                self.image = self.attack_frames_L[self.attackCount//2] 
                self.attackCount += 1
        
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

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -10
        self.direction = "L"

    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 10
        self.direction = "R"

    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
    
    def Idle(self):
        self.isIdle = True
        self.walkCount = 0
        self.isAttack = False
        self.attackCount = 0
    
    def RunLeft(self):
        self.change_x = -10
        self.left = True
        self.right = False
        self.isIdle = False
        self.isAttack = False
        self.attackCount = 0
        self.direction = "L"
        
            
    def RunRight (self):
        self.change_x = 10
        self.left = False
        self.right = True
        self.isIdle = False
        self.isAttack = False
        self.bowCount = 0
        self.attackCount = 0
        self.direction = "R"
                    
    def Attack (self):
        self.isAttack = True
        self.isIdle = False

        
