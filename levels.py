import pygame

import constants
import platforms
import Enemyspotted
import random

class Level():

    # Lists of sprites used in levels
    platform_list = None
    rope_list = None
    bound_list = None
    enemy_list = None
    
    # Background image
    background = []

    # How far this world has been scrolled left/right
    world_shift = 0

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.rope_list = pygame.sprite.Group()
        self.bound_list = pygame.sprite.Group()
        self.player = player

    def update(self,screen):
        """ Update everything in this level."""
        self.platform_list.update()
        self.rope_list.update()
        self.bound_list.update()
        
        for enemy in self.enemy_list:
            if enemy.Health() <= 0:
                self.enemy_list.remove(enemy)
        self.enemy_list.update(self.platform_list)       

    def draw(self, screen):
        """ Draw everything on this level. """

        # Draw the background
        screen.fill(constants.WHITE)
        screen.blit(self.background,(self.world_shift // 3,0))
        

        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
        self.rope_list.draw(screen)
        self.bound_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):
        """ When player moves left/right, we need to scroll everything: """

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        for platform in self.platform_list:
            platform.rect.x += shift_x
            
        for rope in self.rope_list:
            rope.rect.x += shift_x
            
        for bound in self.bound_list:
            bound.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            
            

# Create platforms for the level
class Level_01(Level):
    
    def __init__(self, player):
        
        Level.__init__(self, player)
        
        self.level_limit = -1*constants.SCREEN_WIDTH
        self.background = pygame.transform.scale(pygame.image.load('images/background/Background.png'), (abs(self.level_limit),constants.SCREEN_HEIGHT))

        
        self.background.set_colorkey(constants.WHITE)
        

        # Array with type of platform, and x, y location of the platform.
        level = [ #Top left Platforms
                  [platforms.STONE_CLIFF_RIGHT, 480, 280],
                  #Middle Platform
                  [platforms.GRASS_CLIFF_LEFT, 940, 500],
                  [platforms.GRASS_CLIFF_RIGHT, 1400, 500],
                  #Solo Platform
                  [platforms.FLOATING_STONE, 700, 450]
                  #Top Right Platform
#                  [platforms.GRASS_FLOOR_THICK, 0, 730]
                  
#                  [platforms.ROPE, x, y]
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
        for x in range(2000, 2480, 48):
            level.append([platforms.STONE_PLATFORM_LONG, x, 230])
        for x in range(1800, constants.SCREEN_WIDTH, 48):
            level.append([platforms.STONE_PLATFORM_LONG, x, 400])
        
        #Left and Right Map Boundary
        for y in range(0, constants.SCREEN_HEIGHT, 48):
            level.append([platforms.STONE_CLIFF_FILL, -16, y])
            level.append([platforms.STONE_CLIFF_FILL, constants.SCREEN_WIDTH + 16, y])
        

        # Go through the array and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

 
        
        #Ropes
# =============================================================================
#         level_rope = []
#         for y in range (280, 700, 23):
#             level_rope.append([platforms.ROPE, 550, y])
#             
#         for string in level_rope:
#             rope = platforms.Rope(string[0])
#             rope.rect.x = string[1]
#             rope.rect.y = string[2]
#             rope.player = self.player
#             self.rope_list.add(rope)
# =============================================================================
        level_bound = []
        
        level_bound.append([platforms.INVISIBLE_BLOCK, 240, 155])
        level_bound.append([platforms.INVISIBLE_BLOCK, 400, 195])
        level_bound.append([platforms.INVISIBLE_BLOCK, 540, 235])
        
        level_bound.append([platforms.INVISIBLE_BLOCK, 850, 720])
        level_bound.append([platforms.INVISIBLE_BLOCK, 1520, 720])
        
        level_bound.append([platforms.INVISIBLE_BLOCK, 1790, 370])
        level_bound.append([platforms.INVISIBLE_BLOCK, 1985, 200])
        level_bound.append([platforms.INVISIBLE_BLOCK, 2475, 200])


        
        for brick in level_bound:
            bound = platforms.Rope(brick[0])
            bound.rect.x = brick[1]
            bound.rect.y = brick[2]
            self.bound_list.add(bound)
            
        #Add a custom moving platform   
       
        #Left Floating Platform
        block = platforms.MovingPlatform(platforms.FLOATING_STONE)
        block.rect.x = 550
        block.rect.y = 330
        block.boundary_top = 330
        block.boundary_bottom = 665
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)        
        
        #Middle Left Floating Platform
        block = platforms.MovingPlatform(platforms.FLOATING_GRASS)
        block.rect.x = 860
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = 665
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        #Middle Right Floating Platform
        block = platforms.MovingPlatform(platforms.FLOATING_GRASS)
        block.rect.x = 1460
        block.rect.y = 500
        block.boundary_top = 500
        block.boundary_bottom = 665
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        #Right Floating Platform
        block = platforms.MovingPlatform(platforms.FLOATING_STONE)
        block.rect.x = 1750
        block.rect.y = 450
        block.boundary_top = 450
        block.boundary_bottom = 665
        block.change_y = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
# =============================================================================
#         #Top Right Left Floating Platform
#         block = platforms.MovingPlatform(platforms.FLOATING_STONE)
#         block.rect.x = 1950
#         block.rect.y = 200
#         block.boundary_top = 200
#         block.boundary_bottom = 350
#         block.change_y = 1
#         block.player = self.player
#         block.level = self
#         self.platform_list.add(block)
# =============================================================================

        # Test Enemies
        """ Enemies for Demonstration"""
# =============================================================================
#         enemy = Enemyspotted.Enemy_Bandit(400, 650, 240, 400)
#         enemy.player = self.player
#         enemy.level = self
#         self.enemy_list.add(enemy)
# =============================================================================
        
# =============================================================================
#         enemy = Enemyspotted.Enemy_Blob(400, 650, 240, 400)
#         enemy.player = self.player
#         enemy.level = self
#         self.enemy_list.add(enemy)        
# =============================================================================
        
# =============================================================================
#         enemy = Enemyspotted.Enemy_Midget(400, 650, 240, 400)
#         enemy.player = self.player
#         enemy.level = self
#         self.enemy_list.add(enemy)
# =============================================================================
          
        """ Enemies for Game """
        #Spawn Enemies
        Platform_Areas_Bottom = []
        Platform_Areas_Top_Left = []
        Platform_Areas_Top_Right = []
        
        Bottom_Left_Area = [[0, 845], 650, 4] #[x bounds], [y location], [number of max type of enemies]
        Top_Left_Area_1 = [[0, 240], 160, 1]
        Top_Left_Area_2 = [[240, 400], 200, 1]
        Top_Left_Area_3 = [[400, 480], 240, 1]
        Bottom_Right_Area = [[1530, constants.SCREEN_WIDTH], 650, 4]
        Right_Middle_Area = [[1800, constants.SCREEN_WIDTH], 370, 4]
        Right_Top_Area = [[2000, 2480], 190, 3]
        
        Platform_Areas_Bottom.append(Bottom_Left_Area)
        Platform_Areas_Bottom.append(Bottom_Right_Area)
        
        Platform_Areas_Top_Left.append(Top_Left_Area_1)
        Platform_Areas_Top_Left.append(Top_Left_Area_2)
        Platform_Areas_Top_Left.append(Top_Left_Area_3)
        
        Platform_Areas_Top_Right.append(Right_Middle_Area)
        Platform_Areas_Top_Right.append(Right_Top_Area)
        
        for area in Platform_Areas_Bottom:
            for _ in range(area[2]):
                 x = random.randint(area[0][0], area[0][1])
                 y = area[1]       
                 left_bound = area[0][0]
                 right_bound = area[0][1]
                 enemy = Enemyspotted.Enemy_Bandit(x, y, left_bound, right_bound)
                 enemy.player = self.player
                 enemy.level = self
                 self.enemy_list.add(enemy)
                 
        for area in Platform_Areas_Top_Left:
            for _ in range(area[2]):
                 x = random.randint(area[0][0], area[0][1])
                 y = area[1]       
                 left_bound = area[0][0]
                 right_bound = area[0][1]
                 enemy = Enemyspotted.Enemy_Blob(x, y, left_bound, right_bound)
                 enemy.player = self.player
                 enemy.level = self
                 self.enemy_list.add(enemy)  
                 
        for area in Platform_Areas_Top_Right:
            for _ in range(area[2]):
                 x = random.randint(area[0][0], area[0][1])
                 y = area[1]       
                 left_bound = area[0][0]
                 right_bound = area[0][1]
                 enemy = Enemyspotted.Enemy_Midget(x, y, left_bound, right_bound)
                 enemy.player = self.player
                 enemy.level = self
                 self.enemy_list.add(enemy)  
                 
                 
# =============================================================================
#         Platform_Areas = []
#         Platform_Areas.append(Bottom_Left_Area)
#         Platform_Areas.append(Top_Left_Area_1)
#         Platform_Areas.append(Top_Left_Area_2)
#         Platform_Areas.append(Top_Left_Area_3)
#         Platform_Areas.append(Bottom_Right_Area)
#         Platform_Areas.append(Right_Middle_Area)
#         Platform_Areas.append(Right_Top_Area)
# =============================================================================

        
# =============================================================================
#         for area in Platform_Areas:
#             for _ in range(area[2]):
#                 x = random.randint(area[0][0], area[0][1])
#                 y = area[1]       
#                 left_bound = area[0][0]
#                 right_bound = area[0][1]
#                 if area[1] == 650:
#                     enemy = Enemyspotted.Enemy_Bandit(x, y, left_bound, right_bound)
#                     enemy.player = self.player
#                     enemy.level = self
#                     self.enemy_list.add(enemy)
#                 elif area[1] == 160 or 200 or 240:
#                     enemy = Enemyspotted.Enemy_Blob(x, y, left_bound, right_bound)
#                     enemy.player = self.player
#                     enemy.level = self
#                     self.enemy_list.add(enemy)
#                 elif area[1] == 190 or 370:
#                     enemy = Enemyspotted.Enemy_Midget(x, y, left_bound, right_bound)
#                     enemy.player = self.player
#                     enemy.level = self
#                     self.enemy_list.add(enemy)
# =============================================================================
    
            


# Create platforms for the level
# =============================================================================
# class Level_02(Level):
# 
#     def __init__(self, player):
# 
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
#         # Go through the array and add platforms
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
