#Started on 2/16/2020 at 4:36 pm.
import pygame # If you have python installed, type + run "pip install pygame" in cmd to install pygame.
import time
import sys
import random

# Initialize the program.
pygame.init()

# Define initial variable values.
WIN_WIDTH = 400
WIN_HEIGHT = 400
white = (255,255,255)

# Set the Pygame display values.
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(white)

pygame.display.set_caption('2D Rubiks Cube')

clock = pygame.time.Clock()

def updateDisplay():
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			if event.type == pygame.KEYDOWN:
				if  event.key == pygame.K_q:
					pygame.quit()
					exit()

		pygame.display.update()
		clock.tick(30)


updateDisplay()