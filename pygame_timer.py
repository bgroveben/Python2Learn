import pygame

start_ticks = pygame.time.get_ticks()
while guesses < 2:
    # OTHER GAME CODE HERE
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    if seconds > 60:
        print ("You've ran out of time!")
        break
