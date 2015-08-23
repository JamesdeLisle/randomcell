from utility_functions import *
from cell import *

class mother(cell):

    def __init__(self,actorLattices,x,y):
        cell.__init__(self,x,y)
        self.species = 'mother'
        actorLattices.mother.Map[x][y] = True
        self.foodDropTimer = 1.0
        self.moveToDesire = 12.0
        self.moveAwayDanger = 1.0
        self.moveToOther = 1.0
        self.moveNowhere = 5.0
        self.output = 2.0

    def dropFood(self,actorLattices,foodList):
        
        if self.foodDropTimer < 0.0:
            foodList.addCell(actorLattices,self.x,self.y)
            self.foodDropTimer = 1.0
            

    def updateCell(self,fluidLattices,actorLattices,foodList):
       
        self.moveCell(fluidLattices,actorLattices)
        self.dropFood(actorLattices,foodList)
        self.foodDropTimer = self.foodDropTimer - 0.1

    def printCell(self,screen,actorLattices,printStep,printStep_max): 
        
        xVec,yVec = self.generateAnimationVectors(actorLattices,printStep_max)
        pygame.draw.circle(screen,(0,0,0),(xVec[printStep],yVec[printStep]),10)
        pygame.draw.circle(screen,(255,165,0),(xVec[printStep],yVec[printStep]),9)


