#Started on 2/16/2020 at 4:36 pm, finished on 3/18/2020 at 12:20 pm.
import pygame # if you have python installed, type + run "pip install pygame" in cmd to install pygame.
import time, sys, random

# PROBLEM: When I do U2, D2, then any F move, it gets all screwed up. My guess is that things aren't getting set to 0 and it can't update stuff properly.

# Currently, this program is Functional, not optimal.

# Initialize the program.
pygame.init()

# Define initial variable values.
WIN_WIDTH = 400
WIN_HEIGHT = 400
palette = [(255, 255, 255),(21, 255, 0),(255, 0, 0),(0, 10, 255),(255, 162, 0),(255, 255, 0)]

# Set the Pygame display values.
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
backgroundColor = 248, 248, 255
screen.fill(backgroundColor)

pygame.display.set_caption('2D Rubiks Cube')

clock = pygame.time.Clock()

# Reusable function to return desired text object, which can be displayed.
def drawText(labelText, xPos, yPos):
	font = pygame.font.Font('freesansbold.ttf', 12)
	text = font.render(labelText, True, (0, 0, 0))
	textRect = text.get_rect()
	#textRect.center = (xPos # 2, yPos # 2)
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
        if self.indexU == 2:
            self.xPos = 110
            self.yPos = 95
        if self.indexU == 3:
            self.xPos = 140
            self.yPos = 125
        if self.indexU == 4:
            self.xPos = 170
            self.yPos = 95
        

        if self.indexF == 1:
            self.xPos = 140
            self.yPos = 155
        if self.indexF == 2:
            self.xPos = 110
            self.yPos = 185
        if self.indexF == 3:
            self.xPos = 140
            self.yPos = 215
        if self.indexF == 4:
            self.xPos = 170
            self.yPos = 185
        

        if self.indexR == 1:
            self.xPos = 230
            self.yPos = 155
        if self.indexR == 2:
            self.xPos = 200
            self.yPos = 185
        if self.indexR == 3:
            self.xPos = 230
            self.yPos = 215
        if self.indexR == 4:
            self.xPos = 260
            self.yPos = 185
        

        if self.indexB == 1:
            self.xPos = 320
            self.yPos = 155
        if self.indexB == 2:
            self.xPos = 290
            self.yPos = 185
        if self.indexB == 3:
            self.xPos = 320
            self.yPos = 215
        if self.indexB == 4:
            self.xPos = 350
            self.yPos = 185
        

        if self.indexL == 1:
            self.xPos = 50
            self.yPos = 155
        if self.indexL == 2:
            self.xPos = 20
            self.yPos = 185
        if self.indexL == 3:
            self.xPos = 50
            self.yPos = 215
        if self.indexL == 4:
            self.xPos = 80
            self.yPos = 185
        
        if self.indexD == 1:
            self.xPos = 140
            self.yPos = 245
        if self.indexD == 2:
            self.xPos = 110
            self.yPos = 275
        if self.indexD == 3:
            self.xPos = 140
            self.yPos = 305
        if self.indexD == 4:
            self.xPos = 170
            self.yPos = 275

        #print("Could not place Edge? - InU: " + str(self.indexU) + " , InD" + str(self.indexD) + " , InF" + str(self.indexF) + " , InB" + str(self.indexB) + " , InL" + str(self.indexL) + " , InR" + str(self.indexR))


    def determineCornerPosition(self):
        if self.indexU == 1:
            self.xPos = 170
            self.yPos = 65
        if self.indexU == 2:
            self.xPos = 110
            self.yPos = 65
        if self.indexU == 3:
            self.xPos = 110
            self.yPos = 125
        if self.indexU == 4:
            self.xPos = 170
            self.yPos = 125
        
        if self.indexF == 1:
            self.xPos = 170
            self.yPos = 155
        if self.indexF == 2:
            self.xPos = 110
            self.yPos = 155
        if self.indexF == 3:
            self.xPos = 110
            self.yPos = 215
        if self.indexF == 4:
            self.xPos = 170
            self.yPos = 215
        
        if self.indexR == 1:
            self.xPos = 260
            self.yPos = 155
        if self.indexR == 2:
            self.xPos = 200
            self.yPos = 155
        if self.indexR == 3:
            self.xPos = 200
            self.yPos = 215
        if self.indexR == 4:
            self.xPos = 260
            self.yPos = 215
        
        if self.indexB == 1:
            self.xPos = 350
            self.yPos = 155
        if self.indexB == 2:
            self.xPos = 290
            self.yPos = 155
        if self.indexB == 3:
            self.xPos = 290
            self.yPos = 215
        if self.indexB == 4:
            self.xPos = 350
            self.yPos = 215
        
        if self.indexL == 1:
            self.xPos = 80
            self.yPos = 155
        if self.indexL == 2:
            self.xPos = 20
            self.yPos = 155
        if self.indexL == 3:
            self.xPos = 20
            self.yPos = 215
        if self.indexL == 4:
            self.xPos = 80
            self.yPos = 215
        
        if self.indexD == 1:
            self.xPos = 170
            self.yPos = 245
        if self.indexD == 2:
            self.xPos = 110
            self.yPos = 245
        if self.indexD == 3:
            self.xPos = 110
            self.yPos = 305
        if self.indexD == 4:
            self.xPos = 170
            self.yPos = 305

        #print("Could not place Corner? - InU: " + str(self.indexU) + " , InD" + str(self.indexD) + " , InF" + str(self.indexF) + " , InB" + str(self.indexB) + " , InL" + str(self.indexL) + " , InR" + str(self.indexR))

    def determineCapPosition(self):
        if self.stickerColor == 0:
            self.xPos = 140
            self.yPos = 95
        if self.stickerColor == 1:
            self.xPos = 140
            self.yPos = 185 
        if self.stickerColor == 2:
            self.xPos = 230
            self.yPos = 185
        if self.stickerColor == 3:
            self.xPos = 320
            self.yPos = 185
        if self.stickerColor == 4:
            self.xPos = 50
            self.yPos = 185
        if self.stickerColor == 5:
            self.xPos = 140
            self.yPos = 275
        #print("Could not place cap? - StickerColor: " + str(self.stickerColor))

    def drawSticker(self):
        if self.pieceType == "edge":
            self.determineEdgePosition()
        elif self.pieceType == "corner":
            self.determineCornerPosition()
        elif self.pieceType == "cap":
            self.determineCapPosition()

        pygame.draw.rect(screen, self.color, (self.xPos, self.yPos, 30, 30))
        pygame.draw.rect(screen, (0, 0, 0), (self.xPos, self.yPos, 30, 30), 1)

		#drawText(self.pieceLabel, self.xPos, self.yPos)


# Make cube class? Cube.move processess the array from functions

# Define an array of all 54 edge pieces.
pieces = [Piece(1,0,0,0,0,0,0,"UB","edge"),#0
		  Piece(2,0,0,0,0,0,0,"UL","edge"),#1
		  Piece(3,0,0,0,0,0,0,"UF","edge"),#2
		  Piece(4,0,0,0,0,0,0,"UR","edge"),#3
		  Piece(0,1,0,0,0,0,1,"FU","edge"),#4
		  Piece(0,2,0,0,0,0,1,"FL","edge"),#5
		  Piece(0,3,0,0,0,0,1,"FD","edge"),#6
		  Piece(0,4,0,0,0,0,1,"FR","edge"),#7
		  Piece(0,0,1,0,0,0,2,"RU","edge"),#8
		  Piece(0,0,2,0,0,0,2,"RF","edge"),#9
		  Piece(0,0,3,0,0,0,2,"RD","edge"),#10
		  Piece(0,0,4,0,0,0,2,"RB","edge"),#1
		  Piece(0,0,0,1,0,0,3,"BU","edge"),#1
		  Piece(0,0,0,2,0,0,3,"BR","edge"),#1
		  Piece(0,0,0,3,0,0,3,"BD","edge"),#1
		  Piece(0,0,0,4,0,0,3,"BL","edge"),#15
		  Piece(0,0,0,0,1,0,4,"LU","edge"),#1
		  Piece(0,0,0,0,2,0,4,"LB","edge"),#1
		  Piece(0,0,0,0,3,0,4,"LD","edge"),#1
		  Piece(0,0,0,0,4,0,4,"LF","edge"),#1
		  Piece(0,0,0,0,0,1,5,"DF","edge"),#20
		  Piece(0,0,0,0,0,2,5,"DL","edge"),#2
		  Piece(0,0,0,0,0,3,5,"DB","edge"),#2
		  Piece(0,0,0,0,0,4,5,"DR","edge"),#2
		  Piece(1,0,0,0,0,0,0,"UBR","corner"),#2
		  Piece(2,0,0,0,0,0,0,"UBL","corner"),#25
		  Piece(3,0,0,0,0,0,0,"UFL","corner"),#2
		  Piece(4,0,0,0,0,0,0,"UFR","corner"),#2
		  Piece(0,1,0,0,0,0,1,"FUR","corner"),#2
		  Piece(0,2,0,0,0,0,1,"FUL","corner"),#2
		  Piece(0,3,0,0,0,0,1,"FDL","corner"),#30
		  Piece(0,4,0,0,0,0,1,"FDR","corner"),#3
		  Piece(0,0,1,0,0,0,2,"RUB","corner"),#3
		  Piece(0,0,2,0,0,0,2,"RUF","corner"),#3
		  Piece(0,0,3,0,0,0,2,"RDF","corner"),#3
		  Piece(0,0,4,0,0,0,2,"RDB","corner"),#35
		  Piece(0,0,0,1,0,0,3,"BUL","corner"),#3
		  Piece(0,0,0,2,0,0,3,"BUR","corner"),#3
		  Piece(0,0,0,3,0,0,3,"BDR","corner"),#3
		  Piece(0,0,0,4,0,0,3,"BDL","corner"),#3
		  Piece(0,0,0,0,1,0,4,"LUF","corner"),#40
		  Piece(0,0,0,0,2,0,4,"LUB","corner"),#4
		  Piece(0,0,0,0,3,0,4,"LDB","corner"),#4
		  Piece(0,0,0,0,4,0,4,"LDF","corner"),#4
		  Piece(0,0,0,0,0,1,5,"DFR","corner"),#4
		  Piece(0,0,0,0,0,2,5,"DFL","corner"),#45
		  Piece(0,0,0,0,0,3,5,"DBL","corner"),#4
		  Piece(0,0,0,0,0,4,5,"DBR","corner"),#4
		  Piece(0,0,0,0,0,0,0,"U","cap"),#4
		  Piece(0,0,0,0,0,0,1,"F","cap"),#4
		  Piece(0,0,0,0,0,0,2,"R","cap"),#50
		  Piece(0,0,0,0,0,0,3,"B","cap"),#5
		  Piece(0,0,0,0,0,0,4,"L","cap"),#5
		  Piece(0,0,0,0,0,0,5,"D","cap"),#5
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
	screen.fill(backgroundColor)
	for i in range(len(caps)):
		caps[i].drawSticker()
	for i in range(len(edges)):
		corners[i].drawSticker()
		edges[i].drawSticker()


# Moving functions
def uMove():

    # If edge is in U layer, then move the corresponding piece(s) clockwise 
    for i in range(len(edges)):

        if edges[i].indexF == 0 and edges[i].indexR == 0 and edges[i].indexB == 0 and edges[i].indexL == 0 and edges[i].indexD == 0:

            edges[i].indexU-=1
            if edges[i].indexU > 4: edges[i].indexU-=4 
            if edges[i].indexU < 1: edges[i].indexU+=4 

        

        if edges[i].indexF == 1 :

            # Fu to Lu
            edges[i].indexF=0
            edges[i].indexL=1

         

        elif edges[i].indexF == 0 and edges[i].indexL == 1:
            
            # Fu to Bu
            edges[i].indexL=0
            edges[i].indexB=1

         

        elif edges[i].indexF == 0 and edges[i].indexB == 1:
            
            # Fu to Ru
            edges[i].indexB=0
            edges[i].indexR=1

         

        elif edges[i].indexF == 0 and edges[i].indexR == 1:
            
            # Fu to Fu
            edges[i].indexR=0
            edges[i].indexF=1

            

        drawPieces()

    
    
    # If corner is in U layer, then move the corresponding piece(s) clockwise 
    for i in range(len(corners)):

        if corners[i].indexF == 0 and corners[i].indexR == 0 and corners[i].indexB == 0 and corners[i].indexL == 0 and corners[i].indexD == 0:
            
            corners[i].indexU-=1
            if corners[i].indexU > 4: corners[i].indexU-=4 
            if corners[i].indexU < 1: corners[i].indexU+=4 

        

        if corners[i].indexF == 1 :
            
            # Fu to Lu
            corners[i].indexF=0
            corners[i].indexL=1

         

        elif corners[i].indexF == 0 and corners[i].indexL == 1:
            
            # Fu to Bu
            corners[i].indexL=0
            corners[i].indexB=1

         

        elif corners[i].indexF == 0 and corners[i].indexB == 1:
            
            # Fu to Ru
            corners[i].indexB=0
            corners[i].indexR=1

         

        elif corners[i].indexF == 0 and corners[i].indexR == 1:
            
            # Fu to Fu
            corners[i].indexR=0
            corners[i].indexF=1

            

        if corners[i].indexF == 2 :
            
            # Fu to Lu
            corners[i].indexF=0
            corners[i].indexL=2

         

        elif corners[i].indexF == 0 and corners[i].indexL == 2:
            
            # Fu to Bu
            corners[i].indexL=0
            corners[i].indexB=2

         

        elif corners[i].indexF == 0 and corners[i].indexB == 2:
            
            # Fu to Ru
            corners[i].indexB=0
            corners[i].indexR=2

         

        elif corners[i].indexF == 0 and corners[i].indexR == 2:
            
            # Fu to Fu
            corners[i].indexR=0
            corners[i].indexF=2

            

        drawPieces()

  
def uMovePrime():

    # If edge is in U layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexR == 0 and edges[i].indexB == 0 and edges[i].indexL == 0 and edges[i].indexD == 0:
            
            edges[i].indexU+=1
            if edges[i].indexU > 4: edges[i].indexU-=4 
            if edges[i].indexU < 1: edges[i].indexU+=4 

        

        if edges[i].indexF == 1:
            
            # Fd to Rd
            edges[i].indexF=0
            edges[i].indexR=1

         

        elif edges[i].indexF == 0 and edges[i].indexR == 1:
            
            # Fd to Bu
            edges[i].indexR=0
            edges[i].indexB=1

         

        elif edges[i].indexF == 0 and edges[i].indexB == 1:
            
            # Fd to Ld
            edges[i].indexB=0
            edges[i].indexL=1

         

        elif edges[i].indexF == 0 and edges[i].indexL == 1:
            
            # Fd to Fd
            edges[i].indexL=0
            edges[i].indexF=1

            

        drawPieces()

    

    # If corner is in U layer, then move the corresponding piece(s) counterclockwise
    for i in range(len(corners)):
        
        if corners[i].indexF == 0 and corners[i].indexR == 0 and corners[i].indexB == 0 and corners[i].indexL == 0 and corners[i].indexD == 0:
            
            corners[i].indexU+=1
            if corners[i].indexU > 4: corners[i].indexU-=4 
            if corners[i].indexU < 1: corners[i].indexU+=4 

        

        if corners[i].indexF == 1:
            
            # Fd to Rd
            corners[i].indexF=0
            corners[i].indexR=1

         

        elif corners[i].indexF == 0 and corners[i].indexR == 1:
            
            # Fd to Bu
            corners[i].indexR=0
            corners[i].indexB=1

         

        elif corners[i].indexF == 0 and corners[i].indexB == 1:
            
            # Fd to Ld
            corners[i].indexB=0
            corners[i].indexL=1

         

        elif corners[i].indexF == 0 and corners[i].indexL == 1:
            
            # Fd to Fd
            corners[i].indexL=0
            corners[i].indexF=1

            

        if corners[i].indexF == 2:
            
            # Fd to Rd
            corners[i].indexF=0
            corners[i].indexR=2

         

        elif corners[i].indexF == 0 and corners[i].indexR == 2:
            
            # Fd to Bu
            corners[i].indexR=0
            corners[i].indexB=2

         

        elif corners[i].indexF == 0 and corners[i].indexB == 2:
            
            # Fd to Ld
            corners[i].indexB=0
            corners[i].indexL=2

         

        elif corners[i].indexF == 0 and corners[i].indexL == 2:
            
            # Fd to Fd
            corners[i].indexL=0
            corners[i].indexF=2

            

        drawPieces()


def dMove():

    # If edges is in D layer, then move the corresponding piece(s) clockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexR == 0 and edges[i].indexB == 0 and edges[i].indexL == 0 and edges[i].indexU == 0:
            
            edges[i].indexD-=1
            if edges[i].indexD > 4: edges[i].indexD-=4  
            if edges[i].indexD < 1: edges[i].indexD+=4 

        

        if edges[i].indexF == 3 :
            
            # Fd to Rd
            edges[i].indexF=0
            edges[i].indexR=3

         

        elif edges[i].indexF == 0 and edges[i].indexR == 3:
            
            # Fd to Bu
            edges[i].indexR=0
            edges[i].indexB=3

         

        elif edges[i].indexF == 0 and edges[i].indexB == 3:
            
            # Fd to Ld
            edges[i].indexB=0
            edges[i].indexL=3

         

        elif edges[i].indexF == 0 and edges[i].indexL == 3:
            
            # Fd to Fd
            edges[i].indexL=0
            edges[i].indexF=3

            

        drawPieces()

    

    # If conirer is in D layer, then move the corresponding piece(s) clockwise 
    for i in range(len(corners)):
        
        if corners[i].indexF == 0 and corners[i].indexR == 0 and corners[i].indexB == 0 and corners[i].indexL == 0 and corners[i].indexU == 0:
            
            corners[i].indexD-=1
            if corners[i].indexD > 4: corners[i].indexD-=4  
            if corners[i].indexD < 1: corners[i].indexD+=4 

        

        if corners[i].indexF == 3 :
            
            # Fd to Rd
            corners[i].indexF=0
            corners[i].indexR=3

         

        elif corners[i].indexF == 0 and corners[i].indexR == 3:
            
            # Fd to Bu
            corners[i].indexR=0
            corners[i].indexB=3

         

        elif corners[i].indexF == 0 and corners[i].indexB == 3:
            
            # Fd to Ld
            corners[i].indexB=0
            corners[i].indexL=3

         

        elif corners[i].indexF == 0 and corners[i].indexL == 3:
            
            # Fd to Fd
            corners[i].indexL=0
            corners[i].indexF=3

            

        if corners[i].indexF == 4 :
            
            # Fd to Rd
            corners[i].indexF=0
            corners[i].indexR=4

         

        elif corners[i].indexF == 0 and corners[i].indexR == 4:
            
            # Fd to Bu
            corners[i].indexR=0
            corners[i].indexB=4

         

        elif corners[i].indexF == 0 and corners[i].indexB == 4:
            
            # Fd to Ld
            corners[i].indexB=0
            corners[i].indexL=4

         

        elif corners[i].indexF == 0 and corners[i].indexL == 4:
            
            # Fd to Fd
            corners[i].indexL=0
            corners[i].indexF=4

            


        drawPieces()

    
def dMovePrime():

    # If edge is in D layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexR == 0 and edges[i].indexB == 0 and edges[i].indexL == 0 and edges[i].indexD != 0:
            
            edges[i].indexD+=1
            if edges[i].indexD > 4: edges[i].indexD-=4  
            if edges[i].indexD < 1: edges[i].indexD+=4 

        

        if edges[i].indexF == 3 :
            
            # Fd to Ld
            edges[i].indexF=0
            edges[i].indexL=3

         

        elif edges[i].indexF == 0 and edges[i].indexL == 3:
            
            # Fd to Bu
            edges[i].indexL=0
            edges[i].indexB=3

         

        elif edges[i].indexF == 0 and edges[i].indexB == 3:
            
            # Fd to Rd
            edges[i].indexB=0
            edges[i].indexR=3

         

        elif edges[i].indexF == 0 and edges[i].indexR == 3:
            
            # Fd to Fd
            edges[i].indexR=0
            edges[i].indexF=3

            

        drawPieces()

    

    # If corner is in D layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(corners)):
        
        if corners[i].indexF == 0 and corners[i].indexR == 0 and corners[i].indexB == 0 and corners[i].indexL == 0 and corners[i].indexD != 0:
            
            corners[i].indexD+=1
            if corners[i].indexD > 4: corners[i].indexD-=4  
            if corners[i].indexD < 1: corners[i].indexD+=4 

        
        
        if corners[i].indexF == 3 :
            
            # Fd to Ld
            corners[i].indexF=0
            corners[i].indexL=3

         

        elif corners[i].indexF == 0 and corners[i].indexL == 3:
            
            # Fd to Bu
            corners[i].indexL=0
            corners[i].indexB=3

         

        elif corners[i].indexF == 0 and corners[i].indexB == 3:
            
            # Fd to Rd
            corners[i].indexB=0
            corners[i].indexR=3

         

        elif corners[i].indexF == 0 and corners[i].indexR == 3:
            
            # Fd to Fd
            corners[i].indexR=0
            corners[i].indexF=3

            

        if corners[i].indexF == 4 :
            
            # Fd to Ld
            corners[i].indexF=0
            corners[i].indexL=4

         

        elif corners[i].indexF == 0 and corners[i].indexL == 4:
            
            # Fd to Bu
            corners[i].indexL=0
            corners[i].indexB=4

         

        elif corners[i].indexF == 0 and corners[i].indexB == 4:
            
            # Fd to Rd
            corners[i].indexB=0
            corners[i].indexR=4

         

        elif corners[i].indexF == 0 and corners[i].indexR == 4:
            
            # Fd to Fd
            corners[i].indexR=0
            corners[i].indexF=4

            

        drawPieces()

    
def fMove():

    # If edge is in F layer, then move the corresponding piece(s) clockwise 
    for i in range(len(edges)):
        
        if edges[i].indexB == 0 and edges[i].indexR == 0 and edges[i].indexD == 0 and edges[i].indexL == 0 and edges[i].indexU == 0:
            
            edges[i].indexF-=1
            if edges[i].indexF > 4: edges[i].indexF-=4  
            if edges[i].indexF < 1: edges[i].indexF+=4 

        

        if edges[i].indexU == 3:
            
            # Uf to Rf
            edges[i].indexU=0
            edges[i].indexR=2

         

        elif edges[i].indexR == 2 and edges[i].indexD == 0:
            
            # Rf to Df
            edges[i].indexR=0
            edges[i].indexD=1

         

        elif edges[i].indexD == 1 and edges[i].indexL == 0:
            
            # Fd to Fl
            edges[i].indexD=0
            edges[i].indexL=4

         

        elif edges[i].indexL == 4 and edges[i].indexU == 0:
            
            # Fl to Fu
            edges[i].indexL=0
            edges[i].indexU=3

            

        drawPieces()

    

    # If corner is in F layer, then move the corresponding piece(s) clockwise 
    for i in range(len(corners)):
        
        if corners[i].indexB == 0 and corners[i].indexR == 0 and corners[i].indexD == 0 and corners[i].indexL == 0 and corners[i].indexU == 0:
            
            corners[i].indexF-=1
            if corners[i].indexF > 4: corners[i].indexF-=4  
            if corners[i].indexF < 1: corners[i].indexF+=4 

        

        if corners[i].indexU == 3:
            
            # Uf to Rf
            corners[i].indexU=0
            corners[i].indexR=2

         

        elif corners[i].indexR == 2 and corners[i].indexD == 0:
            
            # Rf to Df
            corners[i].indexR=0
            corners[i].indexD=1

         

        elif corners[i].indexD == 1 and corners[i].indexL == 0:
            
            # Fd to Fl
            corners[i].indexD=0
            corners[i].indexL=4

         

        elif corners[i].indexL == 4 and corners[i].indexU == 0:
            
            # Fl to Fu
            corners[i].indexL=0
            corners[i].indexU=3

            

        if corners[i].indexU == 4:
            
            # Uf to Rf
            corners[i].indexU=0
            corners[i].indexR=3

         

        elif corners[i].indexR == 3 and corners[i].indexD == 0:
            
            # Rf to Df
            corners[i].indexR=0
            corners[i].indexD=2

         

        elif corners[i].indexD == 2 and corners[i].indexL == 0:
            
            # Fd to Fl
            corners[i].indexD=0
            corners[i].indexL=1

         

        elif corners[i].indexL == 1 and corners[i].indexU == 0:
            
            # Fl to Fu
            corners[i].indexL=0
            corners[i].indexU=4

            

        drawPieces()

    
def fMovePrime():

    # If edge is in F layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(edges)):

        if edges[i].indexB == 0 and edges[i].indexR == 0 and edges[i].indexD == 0 and edges[i].indexL == 0 and edges[i].indexU == 0:
            
            edges[i].indexF+=1
            if edges[i].indexF > 4: edges[i].indexF-=4  
            if edges[i].indexF < 1: edges[i].indexF+=4 

        

        if edges[i].indexU == 3:
            
            # Uf to Lf
            edges[i].indexU=0
            edges[i].indexL=4

         

        elif edges[i].indexU == 0 and edges[i].indexL == 4:
            
            # Lf to Df
            edges[i].indexL=0
            edges[i].indexD=1

         

        elif edges[i].indexU == 0 and edges[i].indexD == 1:
            
            # Df to Rf
            edges[i].indexD=0
            edges[i].indexR=2

         

        elif edges[i].indexU == 0 and edges[i].indexR == 2:
            
            # Rf to Uf
            edges[i].indexR=0
            edges[i].indexU=3

            

        drawPieces()

    

    # If corner is in F layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(corners)):
        
        if corners[i].indexB == 0 and corners[i].indexR == 0 and corners[i].indexD == 0 and corners[i].indexL == 0 and corners[i].indexU == 0:
            
            corners[i].indexF+=1
            if corners[i].indexF > 4: corners[i].indexF-=4  
            if corners[i].indexF < 1: corners[i].indexF+=4 
        

        if corners[i].indexU == 3:
            
            # Uf to Lf
            corners[i].indexU=0
            corners[i].indexL=4

         

        elif corners[i].indexU == 0 and corners[i].indexL == 4:
            
            # Lf to Df
            corners[i].indexL=0
            corners[i].indexD=1

         

        elif corners[i].indexU == 0 and corners[i].indexD == 1:
            
            # Df to Rf
            corners[i].indexD=0
            corners[i].indexR=2

         

        elif corners[i].indexU == 0 and corners[i].indexR == 2:
            
            # Rf to Uf
            corners[i].indexR=0
            corners[i].indexU=3

            

        if corners[i].indexU == 4:
            
            # Uf to Lf
            corners[i].indexU=0
            corners[i].indexL=1

         

        elif corners[i].indexU == 0 and corners[i].indexL == 1:
            
            # Lf to Df
            corners[i].indexL=0
            corners[i].indexD=2

         

        elif corners[i].indexU == 0 and corners[i].indexD == 2:
            
            # Df to Rf
            corners[i].indexD=0
            corners[i].indexR=3

         

        elif corners[i].indexU == 0 and corners[i].indexR == 3:
            
            # Rf to Uf
            corners[i].indexR=0
            corners[i].indexU=4

            

        drawPieces()

    
def bMove():

    # If edge is in F layer, then move the corresponding piece(s) clockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexR == 0 and edges[i].indexD == 0 and edges[i].indexL == 0 and edges[i].indexU == 0:
            
            edges[i].indexB-=1
            if edges[i].indexB > 4: edges[i].indexB-=4  
            if edges[i].indexB < 1: edges[i].indexB+=4 

        

        if edges[i].indexU == 1:
            
            # Ub to Lb
            edges[i].indexU=0
            edges[i].indexL=2

         

        elif edges[i].indexL == 2 and edges[i].indexF == 0:
            
            # Lb to Db
            edges[i].indexL=0
            edges[i].indexD=3

         

        elif edges[i].indexD == 3 and edges[i].indexF == 0:
            
            # Db to Rb
            edges[i].indexD=0
            edges[i].indexR=4

         

        elif edges[i].indexR == 4 and edges[i].indexF == 0:
            
            # Rb to Ub
            edges[i].indexR=0
            edges[i].indexU=1

            

        drawPieces()

    

    # If corner is in F layer, then move the corresponding piece(s) clockwise 
    for i in range(len(corners)):
        
        if corners[i].indexF == 0 and corners[i].indexR == 0 and corners[i].indexD == 0 and corners[i].indexL == 0 and corners[i].indexU == 0:
            
            corners[i].indexB-=1
            if corners[i].indexB > 4: corners[i].indexB-=4  
            if corners[i].indexB < 1: corners[i].indexB+=4 

        
        if corners[i].indexU == 1:
            
            # Ub to Lb
            corners[i].indexU=0
            corners[i].indexL=2

        
             
        elif corners[i].indexL == 2 and corners[i].indexF == 0:
            
            # Lb to Db
            corners[i].indexL=0
            corners[i].indexD=3

         

        elif corners[i].indexD == 3 and corners[i].indexF == 0:
            
            # Db to Rb
            corners[i].indexD=0
            corners[i].indexR=4

         

        elif corners[i].indexR == 4 and corners[i].indexF == 0:
            
            # Rb to Ub
            corners[i].indexR=0
            corners[i].indexU=1

            

        if corners[i].indexU == 2:
            
            # Ub to Lb
            corners[i].indexU=0
            corners[i].indexL=3

         

        elif corners[i].indexL == 3 and corners[i].indexF == 0:
            
            # Lb to Db
            corners[i].indexL=0
            corners[i].indexD=4

         

        elif corners[i].indexD == 4 and corners[i].indexF == 0:
            
            # Db to Rb
            corners[i].indexD=0
            corners[i].indexR=1

         

        elif corners[i].indexR == 1 and corners[i].indexF == 0:
            
            # Rb to Ub
            corners[i].indexR=0
            corners[i].indexU=2

            

        drawPieces()

    
def bMovePrime():

    # If peice is in F layer, then move the corresponding piece(s) clockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexR == 0 and edges[i].indexD == 0 and edges[i].indexL == 0 and edges[i].indexU == 0:
            
            edges[i].indexB+=1
            if edges[i].indexB > 4: edges[i].indexB-=4  
            if edges[i].indexB < 1: edges[i].indexB+=4 

        

        if edges[i].indexU == 1:
            
            # Ub to Rb
            edges[i].indexU=0
            edges[i].indexR=4

         

        elif edges[i].indexR == 4 and edges[i].indexF == 0:
           
            # Rb to Db
            edges[i].indexR=0
            edges[i].indexD=3

         

        elif edges[i].indexD == 3 and edges[i].indexF == 0:
            
            # Db to Lb
            edges[i].indexD=0
            edges[i].indexL=2

         

        elif edges[i].indexL == 2 and edges[i].indexF == 0:
            
            # Lb to Ub
            edges[i].indexL=0
            edges[i].indexU=1

            

        drawPieces()

    

    # If corner is in F layer, then move the corresponding piece(s) clockwise 
    for i in range(len(corners)):
        
        if corners[i].indexF == 0 and corners[i].indexR == 0 and corners[i].indexD == 0 and corners[i].indexL == 0 and corners[i].indexU == 0:
            
            corners[i].indexB+=1
            if corners[i].indexB > 4: corners[i].indexB-=4  
            if corners[i].indexB < 1: corners[i].indexB+=4 

        

        if corners[i].indexU == 1:
            
            # Ub to Rb
            corners[i].indexU=0
            corners[i].indexR=4

         

        elif corners[i].indexR == 4 and corners[i].indexF == 0:
            
            # Rb to Db
            corners[i].indexR=0
            corners[i].indexD=3

         

        elif corners[i].indexD == 3 and corners[i].indexF == 0:
            
            # Db to Lb
            corners[i].indexD=0
            corners[i].indexL=2

         

        elif corners[i].indexL == 2 and corners[i].indexF == 0:
            
            # Lb to Ub
            corners[i].indexL=0
            corners[i].indexU=1

            

        if corners[i].indexU == 2:
            
            # Ub to Rb
            corners[i].indexU=0
            corners[i].indexR=1

         

        elif corners[i].indexR == 1 and corners[i].indexF == 0:
            
            # Rb to Db
            corners[i].indexR=0
            corners[i].indexD=4

         

        elif corners[i].indexD == 4 and corners[i].indexF == 0:
            
            # Db to Lb
            corners[i].indexD=0
            corners[i].indexL=3

         
        
        elif corners[i].indexL == 3 and corners[i].indexF == 0:
            
            # Lb to Ub
            corners[i].indexL=0
            corners[i].indexU=2

            

        drawPieces()


def rMove():

    # If peice is in R layer, then move the corresponding piece(s) clockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexB == 0 and edges[i].indexD == 0 and edges[i].indexL == 0 and edges[i].indexU == 0:
            
            edges[i].indexR-=1
            if edges[i].indexR > 4: edges[i].indexR-=4  
            if edges[i].indexR < 1: edges[i].indexR+=4 

        
        
        if edges[i].indexU == 4:
            
            # Ur to Br
            edges[i].indexU=0
            edges[i].indexB=2

         

        elif edges[i].indexB == 2 and edges[i].indexR == 0:
            
            # Br to Dr
            edges[i].indexB=0
            edges[i].indexD=4

         

        elif edges[i].indexD == 4 and edges[i].indexR == 0:
            
            # Dr to Fr
            edges[i].indexD=0
            edges[i].indexF=4

         

        elif edges[i].indexF == 4 and edges[i].indexR == 0:
            
            # Fr to Ur
            edges[i].indexF=0
            edges[i].indexU=4

            

        drawPieces()

    
        
    # If corner is in R layer, then move the corresponding piece(s) clockwise 
    for i in range(len(corners)):
        
        if corners[i].indexF == 0 and corners[i].indexB == 0 and corners[i].indexD == 0 and corners[i].indexL == 0 and corners[i].indexU == 0:
            
            corners[i].indexR-=1
            if corners[i].indexR > 4: corners[i].indexR-=4  
            if corners[i].indexR < 1: corners[i].indexR+=4 

        

        if corners[i].indexU == 4:

            # Ur to Br
            corners[i].indexU=0
            corners[i].indexB=2

         
        
        elif corners[i].indexB == 2 and corners[i].indexR == 0:
            
            # Br to Dr
            corners[i].indexB=0
            corners[i].indexD=4

         

        elif corners[i].indexD == 4 and corners[i].indexR == 0:
            
            # Dr to Fr
            corners[i].indexD=0
            corners[i].indexF=4

         

        elif corners[i].indexF == 4 and corners[i].indexR == 0:
            
            # Fr to Ur
            corners[i].indexF=0
            corners[i].indexU=4

            

        if corners[i].indexU == 1:
            
            # Ur to Br
            corners[i].indexU=0
            corners[i].indexB=3

         
        
        elif corners[i].indexB == 3 and corners[i].indexR == 0:
            
            # Br to Dr
            corners[i].indexB=0
            corners[i].indexD=1

         
        
        elif corners[i].indexD == 1 and corners[i].indexR == 0:
            
            # Dr to Fr
            corners[i].indexD=0
            corners[i].indexF=1

         
        
        elif corners[i].indexF == 1 and corners[i].indexR == 0:
            
            # Fr to Ur
            corners[i].indexF=0
            corners[i].indexU=1

            

        drawPieces()

    
def rMovePrime():

    # If edge is in R layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexB == 0 and edges[i].indexD == 0 and edges[i].indexL == 0 and edges[i].indexU == 0:
            
            edges[i].indexR+=1
            if edges[i].indexR > 4: edges[i].indexR-=4  
            if edges[i].indexR < 1: edges[i].indexR+=4 

        
        
        if edges[i].indexU == 4:
            
            # Ur to Fr
            edges[i].indexU=0
            edges[i].indexF=4

         
        
        elif edges[i].indexF == 4 and edges[i].indexR == 0:
            
            # Fr to Dr
            edges[i].indexF=0
            edges[i].indexD=4

         
        
        elif edges[i].indexD == 4 and edges[i].indexR == 0:
            
            # Dr to Br
            edges[i].indexD=0
            edges[i].indexB=2

         
        
        elif edges[i].indexB == 2 and edges[i].indexR == 0:
            
            # Br to Ur
            edges[i].indexB=0
            edges[i].indexU=4

            

        drawPieces()

    
        
    # If corner is in R layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(corners)):
        
        if corners[i].indexF == 0 and corners[i].indexB == 0 and corners[i].indexD == 0 and corners[i].indexL == 0 and corners[i].indexU == 0:
            
            corners[i].indexR+=1
            if corners[i].indexR > 4: corners[i].indexR-=4  
            if corners[i].indexR < 1: corners[i].indexR+=4 

        
        
        if corners[i].indexU == 4:
            
            # Ur to Fr
            corners[i].indexU=0
            corners[i].indexF=4

         
       
        elif corners[i].indexF == 4 and corners[i].indexR == 0:
            
            # Fr to Dr
            corners[i].indexF=0
            corners[i].indexD=4

         
        
        elif corners[i].indexD == 4 and corners[i].indexR == 0:
            
            # Dr to Br
            corners[i].indexD=0
            corners[i].indexB=2

         
        
        elif corners[i].indexB == 2 and corners[i].indexR == 0:
            
            # Br to Ur
            corners[i].indexB=0
            corners[i].indexU=4

            
        
        if corners[i].indexU == 1:
            
            # Ur to Fr
            corners[i].indexU=0
            corners[i].indexF=1

         
        
        elif corners[i].indexF == 1 and corners[i].indexR == 0:
            
            # Fr to Dr
            corners[i].indexF=0
            corners[i].indexD=1

         
        
        elif corners[i].indexD == 1 and corners[i].indexR == 0:
            
            # Dr to Br
            corners[i].indexD=0
            corners[i].indexB=3

         
        
        elif corners[i].indexB == 3 and corners[i].indexR == 0:
            
            # Br to Ur
            corners[i].indexB=0
            corners[i].indexU=1

            

        drawPieces()

    
def lMove():

    # If edge is in L layer, then move the corresponding piece(s) clockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexB == 0 and edges[i].indexD == 0 and edges[i].indexR == 0 and edges[i].indexU == 0:
            
            edges[i].indexL-=1
            if edges[i].indexL > 4: edges[i].indexL-=4  
            if edges[i].indexL < 1: edges[i].indexL+=4 

        
        
        if edges[i].indexU == 2:
            
            # Ul to Fl
            edges[i].indexU=0
            edges[i].indexF=2

         
       
        elif edges[i].indexF == 2 and edges[i].indexL == 0:
            
            # Fl to Dl
            edges[i].indexF=0
            edges[i].indexD=2

         
        
        elif edges[i].indexD == 2 and edges[i].indexL == 0:
            
            # Dl to Bl
            edges[i].indexD=0
            edges[i].indexB=4

         
        
        elif edges[i].indexB == 4 and edges[i].indexL == 0:
            
            # Fl to Ul
            edges[i].indexB=0
            edges[i].indexU=2

            

        drawPieces()

    
        
    # If corner is in L layer, then move the corresponding piece(s) clockwise 
    for i in range(len(corners)):
        
        if corners[i].indexF == 0 and corners[i].indexB == 0 and corners[i].indexD == 0 and corners[i].indexR == 0 and corners[i].indexU == 0:
            
            corners[i].indexL-=1
            if corners[i].indexL > 4: corners[i].indexL-=4  
            if corners[i].indexL < 1: corners[i].indexL+=4 

        
        
        if corners[i].indexU == 2:
            
            # Ul to Fl
            corners[i].indexU=0
            corners[i].indexF=2

         
        
        elif corners[i].indexF == 2 and corners[i].indexL == 0:
            
            # Fl to Dl
            corners[i].indexF=0
            corners[i].indexD=2

         
        
        elif corners[i].indexD == 2 and corners[i].indexL == 0:
            
            # Dl to Bl
            corners[i].indexD=0
            corners[i].indexB=4

         
        
        elif corners[i].indexB == 4 and corners[i].indexL == 0:
            
            # Fl to Ul
            corners[i].indexB=0
            corners[i].indexU=2

            

        if corners[i].indexU == 3:
            
            # Ul to Fl
            corners[i].indexU=0
            corners[i].indexF=3

        

        elif corners[i].indexF == 3 and corners[i].indexL == 0:
            
            # Fl to Dl
            corners[i].indexF=0
            corners[i].indexD=3

         

        elif corners[i].indexD == 3 and corners[i].indexL == 0:
            
            # Dl to Bl
            corners[i].indexD=0
            corners[i].indexB=1

         

        elif corners[i].indexB == 1 and corners[i].indexL == 0:
            
            # Fl to Ul
            corners[i].indexB=0
            corners[i].indexU=3

            

        drawPieces()

   
def lMovePrime():

    # If edge is in L layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(edges)):
        
        if edges[i].indexF == 0 and edges[i].indexB == 0 and edges[i].indexD == 0 and edges[i].indexR == 0 and edges[i].indexU == 0:
            
            edges[i].indexL-=1
            if edges[i].indexL > 4: edges[i].indexL-=4  
            if edges[i].indexL < 1: edges[i].indexL+=4 

        

        if edges[i].indexU == 2:
            
            # Ul to Bl
            edges[i].indexU=0
            edges[i].indexB=4

         

        elif edges[i].indexB == 4 and edges[i].indexL == 0:
            
            # Bl to Dl
            edges[i].indexB=0
            edges[i].indexD=2

         

        elif edges[i].indexD == 2 and edges[i].indexL == 0:
            
            # Dl to Fl
            edges[i].indexD=0
            edges[i].indexF=2

         

        elif edges[i].indexF == 2 and edges[i].indexL == 0:
            
            # Bl to Ul
            edges[i].indexF=0
            edges[i].indexU=2

            

        drawPieces()

    

    # If corner is in L layer, then move the corresponding piece(s) counterclockwise 
    for i in range(len(corners)):
       
        if corners[i].indexF == 0 and corners[i].indexB == 0 and corners[i].indexD == 0 and corners[i].indexR == 0 and corners[i].indexU == 0:
            
            corners[i].indexL-=1
            if corners[i].indexL > 4: corners[i].indexL-=4  
            if corners[i].indexL < 1: corners[i].indexL+=4 

        

        if corners[i].indexU == 2:
            
            # Ul to Bl
            corners[i].indexU=0
            corners[i].indexB=4

         

        elif corners[i].indexB == 4 and corners[i].indexL == 0:
            
            # Bl to Dl
            corners[i].indexB=0
            corners[i].indexD=2

        

        elif corners[i].indexD == 2 and corners[i].indexL == 0:
            
            # Dl to Fl
            corners[i].indexD=0
            corners[i].indexF=2

         

        elif corners[i].indexF == 2 and corners[i].indexL == 0:
            
            # Bl to Ul
            corners[i].indexF=0
            corners[i].indexU=2

            

        if corners[i].indexU == 3:
            
            # Ul to Bl
            corners[i].indexU=0
            corners[i].indexB=1

         

        elif corners[i].indexB == 1 and corners[i].indexL == 0:
            
            # Bl to Dl
            corners[i].indexB=0
            corners[i].indexD=3

        

        elif corners[i].indexD == 3 and corners[i].indexL == 0:
            
            # Dl to Fl
            corners[i].indexD=0
            corners[i].indexF=3

         

        elif corners[i].indexF == 3 and corners[i].indexL == 0:
            
            # Bl to Ul
            corners[i].indexF=0
            corners[i].indexU=3

            

        drawPieces()


def resetTheCube():
	global pieces, edges, corners, caps
	pieces = [Piece(1,0,0,0,0,0,0,"UB","edge"),#0
		  Piece(2,0,0,0,0,0,0,"UL","edge"),#1
		  Piece(3,0,0,0,0,0,0,"UF","edge"),#2
		  Piece(4,0,0,0,0,0,0,"UR","edge"),#3
		  Piece(0,1,0,0,0,0,1,"FU","edge"),#4
		  Piece(0,2,0,0,0,0,1,"FL","edge"),#5
		  Piece(0,3,0,0,0,0,1,"FD","edge"),#6
		  Piece(0,4,0,0,0,0,1,"FR","edge"),#7
		  Piece(0,0,1,0,0,0,2,"RU","edge"),#8
		  Piece(0,0,2,0,0,0,2,"RF","edge"),#9
		  Piece(0,0,3,0,0,0,2,"RD","edge"),#10
		  Piece(0,0,4,0,0,0,2,"RB","edge"),#1
		  Piece(0,0,0,1,0,0,3,"BU","edge"),#1
		  Piece(0,0,0,2,0,0,3,"BR","edge"),#1
		  Piece(0,0,0,3,0,0,3,"BD","edge"),#1
		  Piece(0,0,0,4,0,0,3,"BL","edge"),#15
		  Piece(0,0,0,0,1,0,4,"LU","edge"),#1
		  Piece(0,0,0,0,2,0,4,"LB","edge"),#1
		  Piece(0,0,0,0,3,0,4,"LD","edge"),#1
		  Piece(0,0,0,0,4,0,4,"LF","edge"),#1
		  Piece(0,0,0,0,0,1,5,"DF","edge"),#20
		  Piece(0,0,0,0,0,2,5,"DL","edge"),#2
		  Piece(0,0,0,0,0,3,5,"DB","edge"),#2
		  Piece(0,0,0,0,0,4,5,"DR","edge"),#2
		  Piece(1,0,0,0,0,0,0,"UBR","corner"),#2
		  Piece(2,0,0,0,0,0,0,"UBL","corner"),#25
		  Piece(3,0,0,0,0,0,0,"UFL","corner"),#2
		  Piece(4,0,0,0,0,0,0,"UFR","corner"),#2
		  Piece(0,1,0,0,0,0,1,"FUR","corner"),#2
		  Piece(0,2,0,0,0,0,1,"FUL","corner"),#2
		  Piece(0,3,0,0,0,0,1,"FDL","corner"),#30
		  Piece(0,4,0,0,0,0,1,"FDR","corner"),#3
		  Piece(0,0,1,0,0,0,2,"RUB","corner"),#3
		  Piece(0,0,2,0,0,0,2,"RUF","corner"),#3
		  Piece(0,0,3,0,0,0,2,"RDF","corner"),#3
		  Piece(0,0,4,0,0,0,2,"RDB","corner"),#35
		  Piece(0,0,0,1,0,0,3,"BUL","corner"),#3
		  Piece(0,0,0,2,0,0,3,"BUR","corner"),#3
		  Piece(0,0,0,3,0,0,3,"BDR","corner"),#3
		  Piece(0,0,0,4,0,0,3,"BDL","corner"),#3
		  Piece(0,0,0,0,1,0,4,"LUF","corner"),#40
		  Piece(0,0,0,0,2,0,4,"LUB","corner"),#4
		  Piece(0,0,0,0,3,0,4,"LDB","corner"),#4
		  Piece(0,0,0,0,4,0,4,"LDF","corner"),#4
		  Piece(0,0,0,0,0,1,5,"DFR","corner"),#4
		  Piece(0,0,0,0,0,2,5,"DFL","corner"),#45
		  Piece(0,0,0,0,0,3,5,"DBL","corner"),#4
		  Piece(0,0,0,0,0,4,5,"DBR","corner"),#4
		  Piece(0,0,0,0,0,0,0,"U","cap"),#4
		  Piece(0,0,0,0,0,0,1,"F","cap"),#4
		  Piece(0,0,0,0,0,0,2,"R","cap"),#50
		  Piece(0,0,0,0,0,0,3,"B","cap"),#5
		  Piece(0,0,0,0,0,0,4,"L","cap"),#5
		  Piece(0,0,0,0,0,0,5,"D","cap"),#5
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

addressableMoves = [uMove, uMovePrime, dMove, dMovePrime, fMove, fMovePrime, bMove, bMovePrime, rMove, rMovePrime, lMove, lMovePrime]

def scrambleTheCube():
	for i in range(20):
		random.choice(addressableMoves)()

# Main loop to continuously draw objects and process user input.
def updateDisplay():
	while True:

		for event in pygame.event.get():
			keyPressed = pygame.key.get_pressed()

			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					exit()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_e:
					resetTheCube()

				elif event.key == pygame.K_s:
					scrambleTheCube()
				if keyPressed[pygame.K_LSHIFT]:
					if event.key == pygame.K_u:
						uMovePrime()
					elif event.key == pygame.K_d:
						dMovePrime()
					elif event.key == pygame.K_f:
						fMovePrime()
					elif event.key == pygame.K_r:
						rMovePrime()
					elif event.key == pygame.K_l:
						lMovePrime()
					elif event.key == pygame.K_b:
						bMovePrime()

				elif not keyPressed[pygame.K_LSHIFT]:
					if event.key == pygame.K_u:
						uMove()
					elif event.key == pygame.K_d:
						dMove()
					elif event.key == pygame.K_f:
						fMove()
					elif event.key == pygame.K_r:
						rMove()
					elif event.key == pygame.K_l:
						lMove()
					elif event.key == pygame.K_b:
						bMove()

		drawPieces()
		drawText("Use the U,F,D,B,R, and L keys to rotate each face.", 180, 0)
		drawText("(hold l-shift for prime moves)", 170, 20)
		#pieces[0].drawSticker()

		pygame.display.update()
		clock.tick(30)


updateDisplay()
			