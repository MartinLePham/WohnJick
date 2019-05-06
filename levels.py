import pygame

import constants
import platforms
import Enemyspotted
import random

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    
    # Background image
    background = []

    # How far this world has been scrolled left/right
    world_shift = 0

    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving platforms
            collide with the player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    # Update everythign on this level
    def update(self,screen):
        """ Update everything in this level."""
        self.platform_list.update()
        
        for enemy in self.enemy_list:
            if enemy.Health() <= 0:
                self.enemy_list.remove(enemy)
        self.enemy_list.update(self.platform_list)       

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        # We don't shift the background as much as the sprites are shifted
        # to give a feeling of depth.
        screen.fill(constants.WHITE)
        screen.blit(self.background,(self.world_shift // 3,0))
        

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
    
    def __init__(self, player):
        """ Create level 1. """
        
        
        # Call the parent constructor
        Level.__init__(self, player)
        
        self.level_limit = -1*constants.SCREEN_WIDTH
        self.background = pygame.transform.scale(pygame.image.load('Background.png'), (abs(self.level_limit),constants.SCREEN_HEIGHT))

        
        self.background.set_colorkey(constants.WHITE)
        

        # Array with type of platform, and x, y location of the platform.
        level = [ #Top left Platforms
                  [platforms.STONE_CLIFF_RIGHT, 480, 280],
                  #Middle Platform
                  [platforms.GRASS_CLIFF_LEFT, 940, 500],
                  [platforms.GRASS_CLIFF_RIGHT, 1400, 500],
                  #Top Right Platform
#                  [platforms.GRASS_FLOOR_THICK, 0, 730]    
                  ]
        #Bottom
        for x in range(0, constants.SCREEN_WIDTH, 32):
            level.append([platforms.GRASS_FLOOR_GRASSY, x, 730])
        
        #Top Left Platforms
        for x in range(0, 240, 16):
            level.append([platforms.STONE_CLIFF_MIDDLE, x, 200])
        for x in range(240, 400, 16):
            level.append([platforms.STONE_CLIFF_MIDDLE, x, 240])
        for x in range(0, 480, 16):
            level.append([platforms.STONE_CLIFF_MIDDLE, x, 280])
        for x in range(0, 400, 16):
            level.append([platforms.STONE_CLIFF_FILL, x, 260])
            
        #Middle Platform
        for y in range(602, constants.SCREEN_HEIGHT, 78):
            level.append([platforms.GRASS_CLIFF_LEFT_FILL, 940, y])
        for y in range(586, constants.SCREEN_HEIGHT, 60):
            level.append([platforms.GRASS_CLIFF_RIGHT_FILL, 1400, y])
        for x in range(1028, 1400, 28):
            level.append([platforms.GRASS_FLOOR_SKINNY, x, 500])
        for x in range(940+31, 1400, 16):
            for y in range(500+102, constants.SCREEN_HEIGHT, 48):    
                level.append([platforms.STONE_CLIFF_FILL, x, y])
        for x in range(940+88, 1400, 16):
            level.append([platforms.STONE_CLIFF_FILL, x, 522])
            level.append([platforms.STONE_CLIFF_FILL, x, 560])
            
        #Top Right Platforms
        for x in range(1800, constants.SCREEN_WIDTH, 48):
            level.append([platforms.STONE_PLATFORM_LONG, x, 200])
        for x in range(1600, constants.SCREEN_WIDTH, 48):
            level.append([platforms.STONE_PLATFORM_LONG, x, 400])
        
        #Left and Right Map Boundary
        for y in range(0, constants.SCREEN_HEIGHT, 48):
            level.append([platforms.STONE_CLIFF_FILL, -16, y])
            level.append([platforms.STONE_CLIFF_FILL, constants.SCREEN_WIDTH + 16, y])

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a custom moving platform
        #Left Floating Platform
        block = platforms.MovingPlatform(platforms.FLOATING_STONE)
        block.rect.x = 550
        block.rect.y = 280
        block.boundary_top = 280
        block.boundary_bottom = constants.SCREEN_HEIGHT
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)        
        
        #Middle Left Floating Platform
        block = platforms.MovingPlatform(platforms.FLOATING_GRASS)
        block.rect.x = 860
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = constants.SCREEN_HEIGHT
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        #Middle Right Floating Platform
        block = platforms.MovingPlatform(platforms.FLOATING_GRASS)
        block.rect.x = 1460
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = constants.SCREEN_HEIGHT
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)

        #Enemies
        enemy = Enemyspotted.Enemy_Bandit(1000, 600)
        enemy.player = self.player
        enemy.level = self
        self.enemy_list.add(enemy)
        
        
# =============================================================================
#         enemy.rect.x = 1400 ####WHY DOES BLOB SPAWN
#         enemy.rect.y = 600
#         self.enemy_list.add(enemy)
# =============================================================================
        
        
        #Spawn Enemies
        Platform_Areas = []
        Bottom_Left_Area = [[0, 1028], 650, 6] #[x bounds], [y location], [number of max type of enemies]
        Platform_Areas.append(Bottom_Left_Area)
        
        number = 0
        for area in Platform_Areas:
            while number < 4:
                x = random.randint(area[0][0], area[0][1])
                y = area[1]       
                enemy = Enemyspotted.Enemy_Bandit(x, y)
                enemy.player = self.player
                enemy.level = self
                self.enemy_list.add(enemy)
                number += 1
        
# =============================================================================
#         level_enemies = []
#         max_enemies = 10
#         enemies_spawned = 0    
#         while enemies_spawned < max_enemies + 1:
#             for area in Platform_Areas: 
#                 bandit_spawned = 0
#                 blob_spawned = 0
#                 while bandit_spawned < random.randint(0, area[2] + 1):
#                     bandit.rect.x = random.randint(area[0][0], area[0][1])
#                     bandit.rect.y = area[1]
#                     level_enemies.append(bandit)
#                     bandit_spawned += 1
#                     enemies_spawned += 1
# =============================================================================
# =============================================================================
#                 enemies_left = area[2] - bandit_spawned
#                 if enemies_left < area[2]:
#                     while blob_spawned < enemies_left:
#                         blob.rect.x = random.randint(area[0][0], area[0][1])
#                         blob.rect.y = area[1]
#                         self.enemy_list.add(blob)
# =============================================================================
                        
#        for enemy in level_enemies:
            


# Create platforms for the level
# =============================================================================
# class Level_02(Level):
#     """ Definition for level 2. """
# 
#     def __init__(self, player):
#         """ Create level 1. """
# 
#         # Call the parent constructor
#         Level.__init__(self, player)
# 
#         self.background = pygame.image.load("background_02.png").convert()
#         self.background.set_colorkey(constants.WHITE)
#         self.level_limit = -1000
# 
#         # Array with type of platform, and x, y location of the platform.
#         level = [ [platforms.STONE_PLATFORM_LEFT, 500, 550],
#                   [platforms.STONE_PLATFORM_MIDDLE, 570, 550],
#                   [platforms.STONE_PLATFORM_RIGHT, 640, 550],
#                   [platforms.GRASS_LEFT, 800, 400],
#                   [platforms.GRASS_MIDDLE, 870, 400],
#                   [platforms.GRASS_RIGHT, 940, 400],
#                   [platforms.GRASS_LEFT, 1000, 500],
#                   [platforms.GRASS_MIDDLE, 1070, 500],
#                   [platforms.GRASS_RIGHT, 1140, 500],
#                   [platforms.STONE_PLATFORM_LEFT, 1120, 280],
#                   [platforms.STONE_PLATFORM_MIDDLE, 1190, 280],
#                   [platforms.STONE_PLATFORM_RIGHT, 1260, 280],
#                   ]
# 
# 
#         # Go through the array above and add platforms
#         for platform in level:
#             block = platforms.Platform(platform[0])
#             block.rect.x = platform[1]
#             block.rect.y = platform[2]
#             block.player = self.player
#             self.platform_list.add(block)
# 
#         # Add a custom moving platform
#         block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
#         block.rect.x = 1500
#         block.rect.y = 300
#         block.boundary_top = 100
#         block.boundary_bottom = 550
#         block.change_y = -1
#         block.player = self.player
#         block.level = self
#         self.platform_list.add(block)
# 
# =============================================================================
