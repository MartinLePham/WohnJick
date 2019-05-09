import pygame
import time
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
    sound_library.pygame.mixer.music.play(-1)
    
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
    

#    you_died =  pygame.transform.scale(pygame.image.load('images/you_died.jpg'), (1400,constants.SCREEN_HEIGHT))

    #Loop until closed
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User input
            if event.type == pygame.QUIT:
                done = True

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

        # Update the player
        active_sprite_list.update(screen)

        # Update items in the level
        current_level.update(screen)

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 800:
            diff = player.rect.x - 800
            if current_level.world_shift - size[0] >= current_level.level_limit:
                player.rect.x = 800 #Reset player to the middle
                current_level.shift_world(-diff)
            else: #Don't shift if player near right side of the screen
                current_level.shift_world(0)

        # If the player gets near the left side, shift the world right (+x)
        
        if player.rect.x < 800:
            diff = 800 - player.rect.x
            if current_level.world_shift < 0:
                player.rect.x = 800 #Reset player to the middle
                current_level.shift_world(diff)
            else: #Don't shift if player near left side of screen
                current_level.world_shift = 0

        # If player hits the left or right screen
        if player.rect.left == 0:
            player.change_x = 0
            player.rect.left = 0

        if player.rect.right == size[0]:
            player.change_x = 0
            player.rect.right = size[0]
            

        # Draw Everything
        current_level.draw(screen)
        active_sprite_list.draw(screen)


        # Limit to 60 frames per second
        clock.tick(60)

        # Update the screen with what we've drawn.
        pygame.display.flip()

        if player.Health() <= 0:
            if player.deathCount >= 34:
                done = True

    pygame.quit()

if __name__ == "__main__":
    main()
