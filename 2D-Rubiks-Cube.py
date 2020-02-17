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
palette = [(255, 255, 255),(21, 255, 0),(255, 0, 0),(0, 10, 255),(255, 162, 0),(255, 255, 0)]

# Set the Pygame display values.
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill((123, 123, 123))

pygame.display.set_caption('2D Rubiks Cube')

clock = pygame.time.Clock()

# Reusable function to return desired text object, which can be displayed.
def drawText(labelText, xPos, yPos):
	font = pygame.font.Font('freesansbold.ttf', 12)
	text = font.render(labelText, True, (0, 0, 0))
	textRect = text.get_rect()
	#textRect.center = (xPos // 2, yPos // 2)
	textRect.center = (xPos+15, yPos+15)
	return screen.blit(text, textRect)


# The class for any of the 54 pieces of the cube being processed.
class Piece:
	def __init__(self, indexU, indexF, indexR, indexB, indexL, indexD, stickerColor, pieceLabel, pieceType):
		self.indexU = indexU
		self.indexF = indexF
		self.indexR = indexR
		self.indexB = indexB
		self.indexL = indexL
		self.indexD = indexD
		self.stickerColor = stickerColor
		self.color = palette[self.stickerColor]
		self.pieceLabel = pieceLabel
		self.xPos = 0
		self.yPos = 0
		self.pieceType = pieceType

	def determineEdgePosition(self):
		if self.indexU == 1:
			self.xPos = 140
			self.yPos = 65
		elif self.indexU == 2:
			self.xPos = 110
			self.yPos = 95
		elif self.indexU == 3:
			self.xPos = 140
			self.yPos = 125
		elif self.indexU == 4:
			self.xPos = 170
			self.yPos = 95
		
		if self.indexF == 1:
			self.xPos = 140
			self.yPos = 155
		elif self.indexF == 2:
			self.xPos = 110
			self.yPos = 185
		elif self.indexF == 3:
			self.xPos = 140
			self.yPos = 215
		elif self.indexF == 4:
			self.xPos = 170
			self.yPos = 185
		
		if self.indexR == 1:
			self.xPos = 230
			self.yPos = 155
		elif self.indexR == 2:
			self.xPos = 200
			self.yPos = 185
		elif self.indexR == 3:
			self.xPos = 230
			self.yPos = 215
		elif self.indexR == 4:
			self.xPos = 260
			self.yPos = 185
		
		if self.indexB == 1:
			self.xPos = 320
			self.yPos = 155;
		elif self.indexB == 2:
			self.xPos = 290
			self.yPos = 185;
		elif self.indexB == 3:
			self.xPos = 320
			self.yPos = 215;
		elif self.indexB == 4:
			self.xPos = 350
			self.yPos = 185;
		
		if self.indexL == 1:
			self.xPos = 50
			self.yPos = 155
		elif self.indexL == 2:
			self.xPos = 20
			self.yPos = 185
		elif self.indexL == 3:
			self.xPos = 50
			self.yPos = 215
		elif self.indexL == 4:
			self.xPos = 80
			self.yPos = 185
		
		if self.indexD == 1:
			self.xPos = 140
			self.yPos = 245
		elif self.indexD == 2:
			self.xPos = 110
			self.yPos = 275
		elif self.indexD == 3:
			self.xPos = 140
			self.yPos = 305
		elif self.indexD == 4:
			self.xPos = 170
			self.yPos = 275

	def determineCornerPosition(self):
		if self.indexU == 1:
		    self.xPos = 170
		    self.yPos = 65
		elif self.indexU == 2:
		    self.xPos = 110
		    self.yPos = 65
		elif self.indexU == 3:
		    self.xPos = 110
		    self.yPos = 125
		elif self.indexU == 4:
		    self.xPos = 170
		    self.yPos = 125

		if self.indexF == 1:
		    self.xPos = 170
		    self.yPos = 155
		elif self.indexF == 2:
		    self.xPos = 110
		    self.yPos = 155
		elif self.indexF == 3:
		    self.xPos = 110
		    self.yPos = 215
		elif self.indexF == 4:
		    self.xPos = 170
		    self.yPos = 215

		if self.indexR == 1:
		    self.xPos = 260
		    self.yPos = 155
		elif self.indexR == 2:
		    self.xPos = 200
		    self.yPos = 155
		elif self.indexR == 3:
		    self.xPos = 200
		    self.yPos = 215
		elif self.indexR == 4:
		    self.xPos = 260
		    self.yPos = 215

		if self.indexB == 1:
		    self.xPos = 350
		    self.yPos = 155
		elif self.indexB == 2:
		    self.xPos = 290
		    self.yPos = 155
		elif self.indexB == 3:
		    self.xPos = 290
		    self.yPos = 215
		elif self.indexB == 4:
		    self.xPos = 350
		    self.yPos = 215

		if self.indexL == 1:
		    self.xPos = 80
		    self.yPos = 155
		elif self.indexL == 2:
		    self.xPos = 20
		    self.yPos = 155
		elif self.indexL == 3:
		    self.xPos = 20
		    self.yPos = 215
		elif self.indexL == 4:
		    self.xPos = 80
		    self.yPos = 215

		if self.indexD == 1:
		    self.xPos = 170
		    self.yPos = 245

		elif self.indexD == 2:
		    self.xPos = 110
		    self.yPos = 245

		elif self.indexD == 3:
		    self.xPos = 110
		    self.yPos = 305

		elif self.indexD == 4:
		    self.xPos = 170
		    self.yPos = 305

	def determineCapPosition(self):
		if self.stickerColor == 0:
			self.xPos = 140
			self.yPos = 95
		elif self.stickerColor == 1:
			self.xPos = 140
			self.yPos = 185
		elif self.stickerColor == 2:
			self.xPos = 230
			self.yPos = 185
		elif self.stickerColor == 3:
			self.xPos = 320
			self.yPos = 185
		elif self.stickerColor == 4:
			self.xPos = 50
			self.yPos = 185
		elif self.stickerColor == 5:
			self.xPos = 140
			self.yPos = 275

	def drawSticker(self):
		if self.pieceType == "edge":
			self.determineEdgePosition()
		elif self.pieceType == "corner":
			self.determineCornerPosition()
		elif self.pieceType == "cap":
			self.determineCapPosition()

		pygame.draw.rect(screen, self.color, (self.xPos, self.yPos, 30, 30))

		drawText(self.pieceLabel, self.xPos, self.yPos)


# Make cube class? Cube.move processess the array from functions

# Define an array of all 54 edge pieces.
pieces = [Piece(1,0,0,0,0,0,0,"UB","edge"),
		  Piece(2,0,0,0,0,0,0,"UL","edge"),
		  Piece(3,0,0,0,0,0,0,"UF","edge"),
		  Piece(4,0,0,0,0,0,0,"UR","edge"),
		  Piece(0,1,0,0,0,0,1,"FU","edge"),
		  Piece(0,2,0,0,0,0,1,"FL","edge"),
		  Piece(0,3,0,0,0,0,1,"FD","edge"),
		  Piece(0,4,0,0,0,0,1,"FR","edge"),
		  Piece(0,0,1,0,0,0,2,"RU","edge"),
		  Piece(0,0,2,0,0,0,2,"RF","edge"),
		  Piece(0,0,3,0,0,0,2,"RD","edge"),
		  Piece(0,0,4,0,0,0,2,"RB","edge"),
		  Piece(0,0,0,1,0,0,3,"BU","edge"),
		  Piece(0,0,0,2,0,0,3,"BR","edge"),
		  Piece(0,0,0,3,0,0,3,"BD","edge"),
		  Piece(0,0,0,4,0,0,3,"BL","edge"),
		  Piece(0,0,0,0,1,0,4,"LU","edge"),
		  Piece(0,0,0,0,2,0,4,"LB","edge"),
		  Piece(0,0,0,0,3,0,4,"LD","edge"),
		  Piece(0,0,0,0,4,0,4,"LF","edge"),
          Piece(0,0,0,0,0,1,5,"DF","edge"),
          Piece(0,0,0,0,0,2,5,"DL","edge"),
          Piece(0,0,0,0,0,3,5,"DB","edge"),
          Piece(0,0,0,0,0,4,5,"DR","edge"),
          Piece(1,0,0,0,0,0,0,"UBR","corner"),
          Piece(2,0,0,0,0,0,0,"UBL","corner"), 
          Piece(3,0,0,0,0,0,0,"UFL","corner"), 
          Piece(4,0,0,0,0,0,0,"UFR","corner"),
          Piece(0,1,0,0,0,0,1,"FUR","corner"), 
          Piece(0,2,0,0,0,0,1,"FUL","corner"), 
          Piece(0,3,0,0,0,0,1,"FDL","corner"), 
          Piece(0,4,0,0,0,0,1,"FDR","corner"), 
          Piece(0,0,1,0,0,0,2,"RUB","corner"), 
          Piece(0,0,2,0,0,0,2,"RUF","corner"),
          Piece(0,0,3,0,0,0,2,"RDF","corner"), 
          Piece(0,0,4,0,0,0,2,"RDB","corner"), 
          Piece(0,0,0,1,0,0,3,"BUL","corner"), 
          Piece(0,0,0,2,0,0,3,"BUR","corner"), 
          Piece(0,0,0,3,0,0,3,"BDR","corner"), 
          Piece(0,0,0,4,0,0,3,"BDL","corner"), 
          Piece(0,0,0,0,1,0,4,"LUF","corner"), 
          Piece(0,0,0,0,2,0,4,"LUB","corner"), 
          Piece(0,0,0,0,3,0,4,"LDB","corner"), 
          Piece(0,0,0,0,4,0,4,"LDF","corner"), 
          Piece(0,0,0,0,0,1,5,"DFR","corner"), 
          Piece(0,0,0,0,0,2,5,"DFL","corner"),
          Piece(0,0,0,0,0,3,5,"DBL","corner"),
          Piece(0,0,0,0,0,4,5,"DBR","corner"),
          Piece(0,0,0,0,0,0,0,"U","cap"),
          Piece(0,0,0,0,0,0,1,"F","cap"),
          Piece(0,0,0,0,0,0,2,"R","cap"),
          Piece(0,0,0,0,0,0,3,"B","cap"),
          Piece(0,0,0,0,0,0,4,"L","cap"),
          Piece(0,0,0,0,0,0,5,"D","cap"),
]
# Define a seperate array to address 24 edge pieces.
edges = [pieces[0],pieces[1],pieces[2],pieces[3],
		 pieces[4],pieces[5],pieces[6],pieces[7],
		 pieces[8],pieces[9],pieces[10],pieces[11],
		 pieces[12],pieces[13],pieces[14],pieces[15],
		 pieces[16],pieces[17],pieces[18],pieces[19],
		 pieces[20],pieces[21],pieces[22],pieces[23]]
# Define a seperate array to address 24 corner pieces.  
corners = [pieces[24],pieces[25],pieces[26],pieces[27],
		   pieces[28],pieces[29],pieces[30],pieces[31],
		   pieces[32],pieces[33],pieces[34],pieces[35],
		   pieces[36],pieces[37],pieces[38],pieces[39],
		   pieces[40],pieces[41],pieces[42],pieces[43],
		   pieces[44],pieces[45],pieces[46],pieces[47]]
# Define a seperate array to address 6 cap pieces.  
caps = [pieces[48],
    	pieces[49],
    	pieces[50],
    	pieces[51],
    	pieces[52],
    	pieces[53]]

# Loop through the entire array of stickers.
def drawPieces():
	for i in range(len(caps)):
		caps[i].drawSticker()
	for i in range(len(edges)):
		corners[i].drawSticker()
		edges[i].drawSticker()
		
	
# Main loop to continuously draw objects and process user input.
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

		drawPieces()
		#pieces[0].drawSticker()

		pygame.display.update()
		clock.tick(30)


updateDisplay()