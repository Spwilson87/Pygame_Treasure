import pygame



pygame.init()

width = 800
height = 800
white_colour = (255, 255, 255)

game_window = pygame.display.set_mode((width,height))

clock = pygame.time.Clock()

def run_game_loop():
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
        game_window.fill(white_colour)
        pygame.display.update()

        clock.tick(60)

run_game_loop()

pygame.quit()
quit()