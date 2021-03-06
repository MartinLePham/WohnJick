import pygame

from spritesheet_functions import SpriteSheet

#Defines Platform Types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite
BLACK_DOT             = (112, 272, 16, 16)

GRASS_FLOOR_SKINNY    = (308, 186, 28, 22)
GRASS_FLOOR_THICK     = (192, 186, 48, 38)
GRASS_FLOOR_GRASSY    = (256, 180, 32, 44)

STONE_FLOOR           = (384, 187, 32, 21)

STONE_PLATFORM_SHORT     = (537, 56, 32, 32)
STONE_PLATFORM_LONG      = (601, 56, 48, 32)

GRASS_CLIFF_LEFT      = (40, 186, 88, 102)
GRASS_CLIFF_LEFT_FILL = (40, 210, 31, 78)
GRASS_CLIFF_RIGHT     = (512, 186, 44, 86)
GRASS_CLIFF_RIGHT_FILL = (512, 212, 44, 60)

STONE_CLIFF_LEFT      = (325, 43, 59, 97)
STONE_CLIFF_MIDDLE    = (400, 43, 16, 96)
STONE_CLIFF_RIGHT     = (432, 43, 59, 97)
STONE_CLIFF_FILL      = (400, 65, 16, 48)

BRIDGE_LEFT           = (583, 188, 41, 30)
BRIDGE_MIDDLE         = (640, 187, 32, 31)
BRIDGE_RIGHT          = (688, 188, 41, 30)

FLOATING_GRASS        = (50, 28, 58, 65)
FLOATING_STONE        = (48, 121, 48, 39)

ROPE                  = (1, 0, 6, 23)

INVISIBLE_BLOCK       = (0, 0, 28, 29)

class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("images/tileset.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

class Rope(pygame.sprite.Sprite):
    """ Ropes to climb """
    
    player = None
    
    def __init__(self, sprite_sheet_data):
        
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('images/Invisible_Block.png')
        
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])
        self.rect = self.image.get_rect()
    
# =============================================================================
#     def update(self):
#         
#         hit = pygame.sprite.collide_rect(self, self.player)
#         if hit:
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_UP:
#                         self.player.Climb()
#                         self.player.rect.right = self.rect.left
#                         self.player.change_y = 5
#                     elif event.key == pygame.k_DOWN:
#                         self.player.rect.right = self.rect.left
#                         self.player.change_y = -5
# =============================================================================
    
class MovingPlatform(Platform):
    """ Platform that moves """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):

        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # If we are moving right, set our right side to the left side of the platform we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # If we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
