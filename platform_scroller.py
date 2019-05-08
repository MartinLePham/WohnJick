import pygame
from time import time
import constants
import levels
from Enemyspotted import Enemy_Midget
from Enemyspotted import Enemy_Bandit
from Enemyspotted import Enemy_Blob
from player import Player
import sound_library

def main():
    """ Main Program """
    pygame.mixer.init(44100, -16, 2, 2048)
    pygame.init()

    # Set the height and width of the screen
    size = [1400, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("WohnJick")

    # Create the player
    player = Player()
    
    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
#    level_list.append(levels.Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    
    player.rect.x = 1300
    player.rect.y = 450
    active_sprite_list.add(player)
    

    you_died =  pygame.transform.scale(pygame.image.load('images/you_died.jpg'), (1400,constants.SCREEN_HEIGHT))

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.RunLeft()
                if event.key == pygame.K_RIGHT:
                    player.RunRight()
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_DOWN:
                    player.Crouch()
                elif event.key == pygame.K_f:
                    player.Attack()
                elif event.key == pygame.K_r:
                    player.Shoot()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.Idle()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.Idle()
                if event.key == pygame.K_f:
                    player.Idle()
                if event.key == pygame.K_r:
                    player.Idle()
                if event.key == pygame.K_DOWN:
                    player.Idle()

        # Update the player.
        active_sprite_list.update(screen)

        # Update items in the level
        current_level.update(screen)

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 800:
            diff = player.rect.x - 800
            if current_level.world_shift - size[0] >= current_level.level_limit:
                player.rect.x = 800
                current_level.shift_world(-diff)
#                print(current_level.world_shift)
            else:
                current_level.shift_world(0)

        # If the player gets near the left side, shift the world right (+x)
        
        if player.rect.x < 800:
            diff = 800 - player.rect.x
            if current_level.world_shift < 0:
                player.rect.x = 800
                current_level.shift_world(diff)
            else:
                current_level.world_shift = 0
#        print(player.rect.x)
        if player.rect.left == 0:
            player.change_x = 0
            player.rect.left = 0
#            print('hit left')
        if player.rect.right == size[0]:
            player.change_x = 0
            player.rect.right = size[0]
#            print(constants.SCREEN_WIDTH + current_level.world_shift)
#            print('hit right')
            

            
        # If the player gets to the end of the level, go to the next level
# =============================================================================
#         current_position = player.rect.x + current_level.world_shift
#         if current_position < current_level.level_limit:
#             player.rect.x = 120
#             if current_level_no < len(level_list)-1:
#                 current_level_no += 1
#                 current_level = level_list[current_level_no]
#                 player.level = current_level
# =============================================================================

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        
        if player.Health() <= 0:
            if player.deathCount >= 34:
                start = time()
                while time() < start+5:
                    screen.blits(you_died, (0,0))
                    if time() > start+5:
                        done = True
    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
