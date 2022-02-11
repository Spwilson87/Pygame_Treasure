# used to run game

# imports pygame module
import pygame

# imports Game class from game.py 
from game import Game

# starts pygame
pygame.init()

#defines game variable as Game from game.py import
game = Game()

# uses run_game_loop object from Game class which is imported from game.py
game.run_game_loop()


pygame.quit()
quit()