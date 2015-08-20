from utility_functions import *
from cell import *

class zombie(cell):

    def __init__(self,lattice,x,y):
        cell.__init__(self,lattice,x,y)
        self.species = 'zombie'
        lattice.zombieCellMap[x][y] = True
        self.hunger = 0.0
        self.moveToDesire = 10.0
        self.moveAwayDanger = 20.0
        self.moveToOther = 1.0
        self.moveNowhere = 5.0
        
    def eatFood(self,lattice,cellList):
        
        if lattice.cellMap[self.x][self.y]:
            self.hunger = 0.0
            for tik in range(len(cellList.celist)):
                if cellList.celist[tik].x == self.x and cellList.celist[tik].y == self.y:
                    lattice.cellMap[self.x][self.y] = False
                    cellList.celist.pop(tik)
                    break 
 
    def updateCell(self,lattice,cellList):
       
        self.eatFood(lattice,cellList)
        self.moveCell(lattice)
    
    def printCell(self,screen,lattice,printStep,printStep_max):
         
        xVec,yVec = self.generateAnimationVectors(lattice,printStep_max)
        pygame.draw.circle(screen,(0,0,0),(xVec[printStep],yVec[printStep]),10)
        pygame.draw.circle(screen,(138,43,226),(xVec[printStep],yVec[printStep]),9)

    
