from cell import *
from utility_functions import *

class hero(cell):
    
    def __init__(self,lattice,x,y):
        cell.__init__(self,lattice,x,y)
        self.species = 'hero'
        lattice.heroMap[x][y] = True

    def printCell(self, screen, lattice, printStep, printStep_max):
        
        xVec,yVec = self.generateAnimationVectors(lattice,printStep_max)
        pygame.draw.polygon(screen,(0,0,0),((xVec[printStep]-10,yVec[printStep]),(xVec[printStep],yVec[printStep]-10),(xVec[printStep]+10,yVec[printStep]),(xVec[printStep],yVec[printStep]+10)))
        pygame.draw.polygon(screen,(0,128,255),((xVec[printStep]-9,yVec[printStep]),(xVec[printStep],yVec[printStep]-9),(xVec[printStep]+9,yVec[printStep]),(xVec[printStep],yVec[printStep]+9)))
       
    def moveCell(self,lattice,shift):
        
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        nCells = len(adjCells[:])
        move_flag = False

        for tik in range(nCells):
            if self.x + shift[0] == adjCells[tik][0] and self.y + shift[1] == adjCells[tik][1]:
                move_flag = True
        
        if not move_flag:
            shift = [0,0]

        self.updateCellMap(lattice,False)
        self.previous_x = self.x
        self.previous_y = self.y
        self.x = self.x + shift[0]
        self.y = self.y + shift[1]
        self.updateCellMap(lattice,True)
        minLx = 0
        minLy = 0
        maxLy = lattice.width
        maxLx = lattice.height
        self.x = wrapBoundaries(minLx,self.x,maxLx)
        self.y = wrapBoundaries(minLy,self.y,maxLy)

    def dropFood(self,lattice,foodList):
         
        foodList.addFood(lattice,self.x,self.y)


    def updateCell(self,lattice,shift):

        self.moveCell(lattice,shift) 
