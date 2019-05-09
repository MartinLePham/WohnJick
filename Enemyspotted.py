import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet
import random
import numpy

class Enemy_Bandit(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of enemy
    change_x = 0
    change_y = 0


    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_L = []
    walking_frames_R = []
    idle_frames_L = []
    idle_frames_R = []
    attack_frames_L = []
    attack_frames_R = []


    # List of sprites we can bump against
    level = None
    player = None
    

    # -- Methods
    def __init__(self, x, y, left_bound, right_bound):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
       
        self.left = False
        self.right = True
        self.isIdle = True
        self.isAttack = False
        self.walkCount = 0
        self.idleCount = 0
        self.attackCount = 0
        
        self.left_bound = left_bound
        self.right_bound = right_bound
        
        self.health = 40
        
        
        walkRight = [pygame.image.load('images/enemy_sprites/Bandit_Running_001.png'), 
                     pygame.image.load('images/enemy_sprites/Bandit_Running_002.png'), 
                     pygame.image.load('images/enemy_sprites/Bandit_Running_003.png'), 
                     pygame.image.load('images/enemy_sprites/Bandit_Running_004.png'), 
                     pygame.image.load('images/enemy_sprites/Bandit_Running_005.png'), 
                     pygame.image.load('images/enemy_sprites/Bandit_Running_006.png'),
                     pygame.image.load('images/enemy_sprites/Bandit_Running_007.png'),
                     pygame.image.load('images/enemy_sprites/Bandit_Running_008.png')]
        for i in walkRight:
            self.walking_frames_R.append(i)
        
        walkLeft = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Running_001.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Running_002.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Running_003.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Running_004.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Running_005.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Running_006.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Running_007.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Running_008.png'),True, False)]
        for i in walkLeft:    
            self.walking_frames_L.append(i)

        idle = [pygame.image.load('images/enemy_sprites/Bandit_Idle_001.png'), 
                pygame.image.load('images/enemy_sprites/Bandit_Idle_002.png'), 
                pygame.image.load('images/enemy_sprites/Bandit_Idle_003.png'), 
                pygame.image.load('images/enemy_sprites/Bandit_Idle_004.png'),
                pygame.image.load('images/enemy_sprites/Bandit_Idle_005.png'),
                pygame.image.load('images/enemy_sprites/Bandit_Idle_006.png')]
        for i in idle:
            self.idle_frames_R.append(i)
        
        idleLeft = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Idle_001.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Idle_002.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Idle_003.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Idle_004.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Idle_005.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Idle_006.png'),True, False)]
        for i in idleLeft:
            self.idle_frames_L.append(i)
        
        attack =  [pygame.image.load('images/enemy_sprites/Bandit_Attack_001.png'),
                   pygame.image.load('images/enemy_sprites/Bandit_Attack_002.png'),
                   pygame.image.load('images/enemy_sprites/Bandit_Attack_003.png'), 
                   pygame.image.load('images/enemy_sprites/Bandit_Attack_004.png'), 
                   pygame.image.load('images/enemy_sprites/Bandit_Attack_005.png'), 
                   pygame.image.load('images/enemy_sprites/Bandit_Attack_006.png'), 
                   pygame.image.load('images/enemy_sprites/Bandit_Attack_007.png')]
        for i in attack:
            self.attack_frames_R.append(i)
        
        attackLeft = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Attack_001.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Attack_002.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Attack_003.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Attack_004.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Attack_005.png'),True, False), 
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Attack_006.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Bandit_Attack_007.png'),True, False)]
        for i in attackLeft:
            self.attack_frames_L.append(i)

        # Set the image the player starts with
        self.image = self.idle_frames_R[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, screen):
        """ Move the player. """
        self.calc_grav()
        self.wander()   
#        self.boundaries()
            
        if self.walkCount + 1 > 24: # 3 frames per walking frame
            self.walkCount = 0
            
        if self.idleCount +1 > 30: # 5 frames per idle frame
            self.idleCount = 0
                                  
        if self.attackCount +1 > 14:
            self.attackCount = 0
                        
        #Right Movements      
        if self.isIdle and self.right:
            self.image = self.idle_frames_R[self.idleCount//5]
            self.idleCount += 1
        
        elif self.right and not self.isIdle and not self.isAttack:
            self.image = self.walking_frames_R[self.walkCount//3] 
            self.walkCount += 1
         
        elif self.isAttack and self.right:
            self.image = self.attack_frames_R[self.attackCount//2]
            if self.image == self.attack_frames_R[2] or self.attack_frames_R[5]:
                if pygame.sprite.collide_rect(self, self.player):
                    self.player.subtractHealth()
#                    print('HP Lost')
                    #Possible Knockback Mechanic
            self.attackCount += 1
                    
        #Left Movements                       
        if self.isIdle and self.left:
            self.image = self.idle_frames_L[self.idleCount//5] 
            self.idleCount += 1
            
        elif self.left and not self.isIdle and not self.isAttack:
            self.image = self.walking_frames_L[self.walkCount//3] 
            self.walkCount += 1
            
        elif self.isAttack and self.left:
            self.image = self.attack_frames_L[self.attackCount//2]
            if self.image == self.attack_frames_L[2] or self.attack_frames_L[5]:
                if pygame.sprite.collide_rect(self.player, self):
                    self.player.subtractHealth()  
#                    print('HP Lost')
            self.attackCount += 1

        self.rect.x += self.change_x
        
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

        bound_hit_list = pygame.sprite.spritecollide(self, self.level.bound_list, False)
        for bound in bound_hit_list:
            if self.change_x > 0:
                self.rect.right = bound.rect.left
            elif self.change_x < 0:
                self.rect.left = bound.rect.right            

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
        
            
    def wander(self):
        """Wandering Movement"""
        movement = ['Move', 'Stop']
        move_chances = [0.25, 0.75]
        random_movement = numpy.random.choice(movement, p=move_chances)
        
        directions = ['Left', 'Right']
        chances = [0.5, 0.5]
        random_direction = numpy.random.choice(directions, p=chances)
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.player.rect.x > self.rect.x:
                self.left == False
                self.right == True
                self.Attack()
            elif self.player.rect.x < self.rect.x:
                self.right == False
                self.left == True
                self.Attack()
        else:
            if random_movement == 'Stop':
                self.Idle()
            elif random_movement == 'Move':
                if random_direction == 'Left':
                    self.RunLeft()
                elif random_direction == 'Right':
                    self.RunRight()
                    
# =============================================================================
#     def boundaries(self):
#         if self.rect.right >= self.right_bound:
#             self.change_x = 0
#             self.rect.right = self.right_bound
#         if self.rect.left <= self.left_bound:
#             self.change_x = 0
#             self.rect.left = self.left_bound
# # =============================================================================
# #         if self.change_x > 0:
# #             if self.rect.x + self.change_x >= self.right_bound - self.rect.width:
# #                 self.change_x = 0
# #                 self.rect.x = self.right_bound - self.rect.width
# #         elif self.change_x < 0:
# #             if self.rect.left <= self.left_bound:
# #                 self.change_x = 0
# #                 
# # =============================================================================
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

    def Idle(self):
        self.change_x = 0
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
            
    def RunRight (self):
        self.change_x = 10
        self.left = False
        self.right = True
        self.isIdle = False
        self.isAttack = False
        self.attackCount = 0
                    
    def Attack (self):
        self.isAttack = True
        self.isIdle = False
        self.change_x = 0

    def Health(self):
        return self.health
        
    def subtractHealth(self):
        self.health = max(self.health - 1, 0)
        if self.health <= 0:
            self.change_x = 0
            self.change_y = 0
            #-------INSERT DEATH ANIMATION-------------
                   

class Enemy_Blob(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of enemy
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_L = []
    walking_frames_R = []
    idle_frames_L = []
    idle_frames_R = []
    attack_frames_L = []
    attack_frames_R = []


    # List of sprites we can bump against
    level = None
    player = None
    

    # -- Methods
    def __init__(self, x, y, left_bound, right_bound):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
       
        self.left = False
        self.right = True
        self.isIdle = True
        self.isAttack = False
        self.walkCount = 0
        self.idleCount = 0
        self.attackCount = 0
        
        self.health = 100
        
        self.left_bound = left_bound
        self.right_bound = right_bound
        
        walkLeft = [pygame.image.load('images/enemy_sprites/Blob_Running_001.png'), 
                     pygame.image.load('images/enemy_sprites/Blob_Running_002.png'), 
                     pygame.image.load('images/enemy_sprites/Blob_Running_003.png'), 
                     pygame.image.load('images/enemy_sprites/Blob_Running_004.png'), 
                     pygame.image.load('images/enemy_sprites/Blob_Running_005.png'), 
                     pygame.image.load('images/enemy_sprites/Blob_Running_006.png'),
                     pygame.image.load('images/enemy_sprites/Blob_Running_007.png'),
                     pygame.image.load('images/enemy_sprites/Blob_Running_008.png')]
        for i in walkLeft:
            self.walking_frames_L.append(i)
        
        walkRight = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Running_001.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Running_002.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Running_003.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Running_004.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Running_005.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Running_006.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Running_007.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Running_008.png'),True, False)]
        for i in walkRight:    
            self.walking_frames_R.append(i)

        idleLeft = [pygame.image.load('images/enemy_sprites/Blob_Idle_001.png'), 
                pygame.image.load('images/enemy_sprites/Blob_Idle_002.png'), 
                pygame.image.load('images/enemy_sprites/Blob_Idle_003.png'), 
                pygame.image.load('images/enemy_sprites/Blob_Idle_004.png'),
                pygame.image.load('images/enemy_sprites/Blob_Idle_005.png'),
                pygame.image.load('images/enemy_sprites/Blob_Idle_006.png')]
        for i in idleLeft:
            self.idle_frames_L.append(i)
        
        idle = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Idle_001.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Idle_002.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Idle_003.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Idle_004.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Idle_005.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Idle_006.png'),True, False)]
        for i in idle:
            self.idle_frames_R.append(i)
        
        attackLeft =  [pygame.image.load('images/enemy_sprites/Blob_Attack_001.png'),
                   pygame.image.load('images/enemy_sprites/Blob_Attack_002.png'),
                   pygame.image.load('images/enemy_sprites/Blob_Attack_003.png'), 
                   pygame.image.load('images/enemy_sprites/Blob_Attack_004.png'), 
                   pygame.image.load('images/enemy_sprites/Blob_Attack_005.png'), 
                   pygame.image.load('images/enemy_sprites/Blob_Attack_006.png'), 
                   pygame.image.load('images/enemy_sprites/Blob_Attack_007.png'),
                   pygame.image.load('images/enemy_sprites/Blob_Attack_008.png')]
        for i in attackLeft:
            self.attack_frames_L.append(i)
        
        attack = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Attack_001.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Attack_002.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Attack_003.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Attack_004.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Attack_005.png'),True, False), 
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Attack_006.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Attack_007.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/Blob_Attack_008.png'),True, False)]
        for i in attack:
            self.attack_frames_R.append(i)

        # Set the image the player starts with
        self.image = self.idle_frames_R[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, screen):
        """ Move the player. """
        self.calc_grav()
        self.wander()   
#        self.boundaries()
            
        
        if self.walkCount + 1 > 24: # 3 frames per walking frame
            self.walkCount = 0
            
        if self.idleCount +1 > 30: # 5 frames per idle frame
            self.idleCount = 0
                                  
        if self.attackCount +1 > 16:
            self.attackCount = 0
                        
        #Right Movements      
        if self.isIdle and self.right:
            self.image = self.idle_frames_R[self.idleCount//5]
            self.idleCount += 1
        
        elif self.right and not self.isIdle and not self.isAttack:
            self.image = self.walking_frames_R[self.walkCount//3] 
            self.walkCount += 1
         
        elif self.isAttack and self.right:
            self.image = self.attack_frames_R[self.attackCount//2]
            if self.image == self.attack_frames_R[2]:
                if pygame.sprite.collide_rect(self, self.player):
                    self.player.subtractHealth()
#                    print('HP Lost')
                    #Possible Knockback Mechanic
            self.attackCount += 1
                    
        #Left Movements                       
        if self.isIdle and self.left:
            self.image = self.idle_frames_L[self.idleCount//5] 
            self.idleCount += 1
            
        elif self.left and not self.isIdle and not self.isAttack:
            self.image = self.walking_frames_L[self.walkCount//3] 
            self.walkCount += 1
            
        elif self.isAttack and self.left:
            self.image = self.attack_frames_L[self.attackCount//2]
            if self.image == self.attack_frames_L[2]:
                if pygame.sprite.collide_rect(self.player, self):
                    self.player.subtractHealth()  
#                    print('HP Lost')
            self.attackCount += 1

        self.rect.x += self.change_x
        
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
                
        bound_hit_list = pygame.sprite.spritecollide(self, self.level.bound_list, False)
        for bound in bound_hit_list:
            if self.change_x > 0:
                self.rect.right = bound.rect.left
            elif self.change_x < 0:
                self.rect.left = bound.rect.right  
                
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
                
            
    def wander(self):
        """Wandering Movement"""
        movement = ['Move', 'Stop']
        move_chances = [0.25, 0.75]
        random_movement = numpy.random.choice(movement, p=move_chances)
        
        directions = ['Left', 'Right']
        chances = [0.5, 0.5]
        random_direction = numpy.random.choice(directions, p=chances)
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.Attack()
        else:
            if random_movement == 'Stop':
                self.Idle()
            elif random_movement == 'Move':
                if random_direction == 'Left':
                    self.RunLeft()
                elif random_direction == 'Right':
                    self.RunRight()
                    
# =============================================================================
#     def boundaries(self):
#         if self.rect.right + self.change_x == self.right_bound:
#             self.change_x = 0
#             self.rect.right = self.right_bound
#         if self.rect.left == self.left_bound:
#             self.change_x = 0
#             self.rect.left = self.left_bound
# # =============================================================================
# #         if self.change_x > 0:
# #             if self.rect.x + self.change_x >= self.right_bound - self.rect.width:
# #                 self.change_x = 0
# #                 self.rect.x = self.right_bound - self.rect.width
# #         elif self.change_x < 0:
# #             if self.rect.left <= self.left_bound:
# #                 self.change_x = 0
# # =============================================================================
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

    def Idle(self):
        self.change_x = 0
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
            
    def RunRight (self):
        self.change_x = 10
        self.left = False
        self.right = True
        self.isIdle = False
        self.isAttack = False
        self.attackCount = 0
                    
    def Attack (self):
        self.isAttack = True
        self.isIdle = False
        self.change_x = 0

    def Health(self):
        return self.health
        
    def subtractHealth(self):
        self.health = max(self.health - 1, 0)
        if self.health <= 0:
            self.change_x = 0
            self.change_y = 0
            #-------INSERT DEATH ANIMATION-------------
                   
class Enemy_Midget(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """

    # -- Attributes
    # Set speed vector of enemy
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_L = []
    walking_frames_R = []
    idle_frames_L = []
    idle_frames_R = []
    attack_frames_L = []
    attack_frames_R = []


    # List of sprites we can bump against
    level = None
    player = None
    

    # -- Methods
    def __init__(self, x, y, left_bound, right_bound):
        """ Constructor function """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
       
        self.left = False
        self.right = True
        self.isIdle = True
        self.isAttack = False
        self.walkCount = 0
        self.idleCount = 0
        self.attackCount = 0
        
        self.health = 20
        
        self.left_bound = left_bound
        self.right_bound = right_bound
        
        
        walkRight = [pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_0.png'), 
                     pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_1.png'), 
                     pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_2.png'), 
                     pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_3.png'), 
                     pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_4.png'), 
                     pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_5.png')]
        for i in walkRight:
            self.walking_frames_R.append(i)
        
        walkLeft = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_0.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_1.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_2.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_3.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_4.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like run_Animation 1_5.png'),True, False)]
        for i in walkLeft:    
            self.walking_frames_L.append(i)

        idle = [pygame.image.load('images/enemy_sprites/rogue like idle_Animation 1_0.png'), 
                pygame.image.load('images/enemy_sprites/rogue like idle_Animation 1_1.png'), 
                pygame.image.load('images/enemy_sprites/rogue like idle_Animation 1_2.png')]
        for i in idle:
            self.idle_frames_R.append(i)
        
        idleLeft = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like idle_Animation 1_0.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like idle_Animation 1_1.png'),True, False),
                    pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like idle_Animation 1_2.png'),True, False)]
        for i in idleLeft:
            self.idle_frames_L.append(i)
        
        attack =  [pygame.image.load('images/enemy_sprites/rogue like attack animations_attack right_0.png'),
                   pygame.image.load('images/enemy_sprites/rogue like attack animations_attack right_1.png'),
                   pygame.image.load('images/enemy_sprites/rogue like attack animations_attack right_2.png'), 
                   pygame.image.load('images/enemy_sprites/rogue like attack animations_attack right_3.png')]
        for i in attack:
            self.attack_frames_R.append(i)
        
        attackLeft = [pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like attack animations_attack right_0.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like attack animations_attack right_1.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like attack animations_attack right_2.png'),True, False),
                      pygame.transform.flip(pygame.image.load('images/enemy_sprites/rogue like attack animations_attack right_3.png'),True, False)]
        for i in attackLeft:
            self.attack_frames_L.append(i)

        # Set the image the player starts with
        self.image = self.idle_frames_R[0]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, screen):
        """ Move the player. """
        self.calc_grav()
        self.wander() 
#        self.boundaries()
            
        
        if self.walkCount + 1 > 15: # 3 frames per walking frame
            self.walkCount = 0
            
        if self.idleCount +1 > 15: # 5 frames per idle frame
            self.idleCount = 0
                                  
        if self.attackCount +1 > 8:
            self.attackCount = 0
                        
        #Right Movements      
        if self.isIdle and self.right:
            self.image = self.idle_frames_R[self.idleCount//5]
            self.idleCount += 1
        
        elif self.right and not self.isIdle and not self.isAttack:
            self.image = self.walking_frames_R[self.walkCount//3] 
            self.walkCount += 1
         
        elif self.isAttack and self.right:
            self.image = self.attack_frames_R[self.attackCount//2]
            if self.image == self.attack_frames_R[2]:
                if pygame.sprite.collide_rect(self, self.player):
                    self.player.subtractHealth()
#                    print('HP Lost')
                    #Possible Knockback Mechanic
            self.attackCount += 1
                    
        #Left Movements                       
        if self.isIdle and self.left:
            self.image = self.idle_frames_L[self.idleCount//5] 
            self.idleCount += 1
            
        elif self.left and not self.isIdle and not self.isAttack:
            self.image = self.walking_frames_L[self.walkCount//3] 
            self.walkCount += 1
            
        elif self.isAttack and self.left:
            self.image = self.attack_frames_L[self.attackCount//2]
            if self.image == self.attack_frames_L[2]:
                if pygame.sprite.collide_rect(self.player, self):
                    self.player.subtractHealth()  
#                    print('HP Lost')
            self.attackCount += 1

        self.rect.x += self.change_x
        
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

        bound_hit_list = pygame.sprite.spritecollide(self, self.level.bound_list, False)
        for bound in bound_hit_list:
            if self.change_x > 0:
                self.rect.right = bound.rect.left
            elif self.change_x < 0:
                self.rect.left = bound.rect.right  
                
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
                
#        self.boundaries()
                
            
    def wander(self):
        """Wandering Movement"""
        movement = ['Move', 'Stop']
        move_chances = [0.25, 0.75]
        random_movement = numpy.random.choice(movement, p=move_chances)
        
        directions = ['Left', 'Right']
        chances = [0.5, 0.5]
        random_direction = numpy.random.choice(directions, p=chances)
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.Attack()
        else:
            if random_movement == 'Stop':
                self.Idle()
            elif random_movement == 'Move':
                if random_direction == 'Left':
                    self.RunLeft()
                elif random_direction == 'Right':
                    self.RunRight()

# =============================================================================
#     def boundaries(self):
#         if self.rect.x > self.right_bound:
#             self.change_x = 0
#             self.rect.x = 0
#         elif self.rect.left < self.left_bound:
#             self.change_x = -self.change_x
#             self.rect.left = self.left_bound
# # =============================================================================
# #         if self.change_x > 0:
# #             if self.rect.x + self.change_x >= self.right_bound - self.image.get_width():
# #                 self.change_x = 0
# #                 self.rect.x = self.right_bound - self.image.get_width()
# # =============================================================================
# # =============================================================================
# #         if self.change_x < 0:
# #             if self.rect.x < self.left_bound:
# #                 self.change_x = 0
# # =============================================================================
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

    def Idle(self):
        self.change_x = 0
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
            
    def RunRight (self):
        self.change_x = 10
        self.left = False
        self.right = True
        self.isIdle = False
        self.isAttack = False
        self.attackCount = 0
                    
    def Attack (self):
        self.isAttack = True
        self.isIdle = False
        self.change_x = 0

    def Health(self):
        return self.health
        
    def subtractHealth(self):
        self.health = max(self.health - 1, 0)
        if self.health <= 0:
            self.change_x = 0
            self.change_y = 0
            #-------INSERT DEATH ANIMATION-------------
                   