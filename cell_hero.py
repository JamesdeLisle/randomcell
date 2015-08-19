from cell import *
from utilityFunctions import *

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

    def updateCell(self,lattice,shift):

        self.moveCell(lattice,shift)        
