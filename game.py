# imports pygame module
import pygame

# imports GameObject from gameObject.py
from gameObject import GameObject

#imports Player from player.py
from player import Player

# imports Enemy from enemy.py
from enemy import Enemy

# imports bgm and plays using pygame mixer
file = 'assets/theme.wav'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

# user pygame mixer to load sounds from assets to be called upon when needed
win = pygame.mixer.Sound('assets/win.wav')
die = pygame.mixer.Sound('assets/die.wav')
death = pygame.mixer.Sound('assets/death.wav')

# creates class called Game
class Game:
    # defines pygame configs like window size, clock rate, background image and location of static image treasure
    def __init__(self):
        self.width = 800
        self.height = 800
        self.white_colour = (255, 255, 255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        self.clock = pygame.time.Clock()

        self.background = GameObject(0,0, self.width, self.height, 'assets/background.png')

        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')
        

      
        self.level = 1.0

        self.reset_map()

    # adds more enemys depnding on player level
    def reset_map(self):

        self.player = Player(375, 700, 50, 50, 'assets/player.png', 8)

        speed = 1 + (self.level * 2)

        if self.level >= 6.0:
            self.enemies = [
                Enemy(0, 350, 200, 200, 'assets/boss.png', speed),
                
            ]
            die.play()

        elif self.level >= 5.0:
            self.enemies = [
                Enemy(0, 590, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 490, 50, 50, 'assets/enemy.png', speed),
                Enemy(0, 290, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 190, 50, 50, 'assets/enemy.png', speed)
            ]

        elif self.level >= 4.0:
            self.enemies = [
                Enemy(0, 590, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 490, 50, 50, 'assets/enemy.png', speed),
                Enemy(0, 290, 50, 50, 'assets/enemy.png', speed)
            ]

        elif self.level >= 2.0:
            self.enemies = [
                Enemy(0, 590, 50, 50, 'assets/enemy.png', speed),
                Enemy(750, 490, 50, 50, 'assets/enemy.png', speed),
            ]

        else:
            self.enemies = [
                Enemy(0, 590, 50, 50, 'assets/enemy.png', speed)
            ]
       
    # draws image assets 
    def draw_objects(self):
        self.game_window.fill(self.white_colour)

        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))

        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))

        pygame.display.update()

    # defines the player can only move vertical and enemy horizontal
    def move_objects(self, player_direction):
        self.player.move(player_direction, self.height)
        for enemy in self.enemies:
            enemy.move(self.width)

    # checks if the player collides
    def check_if_collided(self):

        # checks if player and enemy collides and plays death sound and resets level to 1.0
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                death.play()
                self.level =1.0
                return True

        # checks if player and treasure collides and plays win sound and adds 0.5 to level
        if self.detect_collision(self.player, self.treasure):
            win.play()
            self.level += 0.5
            return True
        return False

    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False

        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False

        return True

        

# defines the main game loop and what happens when certain keys are pressed
    def run_game_loop(self):

        # sets player start direction
        player_direction = 0

        while True:
            # Handle events
            events = pygame.event.get()
            for event in events:

                # checks if pygame has been closed
                if event.type == pygame.QUIT:
                    return

                    # checks if key is pressed down
                elif event.type == pygame.KEYDOWN:

                    # if up key is pressed moves player direction by -1 wich moves player up one
                    if event.key == pygame.K_UP:
                        player_direction = -1

                    # if down key is pressed moves player direction by 1 wich moves player down 1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1

                # checks when a key has been released
                elif event.type == pygame. KEYUP:

                    # checks if up or down key has been released sets player direction to 0 which stops player movement
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

            # uses the move_objects function from Game class to move player with run_game_loop function
            self.move_objects(player_direction)
            
            # Updates the display to refelct changes in movement
            self.draw_objects()

            # Detect collisions between player and enemy which upon collide resets the game, if the player collides with the treasure it uses reset_map to go to next level
            if self.check_if_collided():
                self.reset_map()

            # sets the clock rate
            self.clock.tick(60)