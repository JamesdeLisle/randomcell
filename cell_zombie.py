from utility_functions import *
from cell import *

class zombie(cell):

    def __init__(self,actorLattices,x,y):
        cell.__init__(self,x,y)
        self.species = 'zombie'
        actorLattices.zombie.Map[x][y] = True
        self.hunger = 0.0
        self.moveToDesire = 10.0
        self.moveAwayDanger = 20.0
        self.moveToOther = 1.0
        self.moveNowhere = 5.0
        self.output = 2.0
        
    def eatFood(self,actorLattices,droneList):
        
        if actorLattices.drone.Map[self.x][self.y]:
            self.hunger = 0.0
            for tik in range(len(droneList.actorList)):
                if droneList.actorList[tik].x == self.x and droneList.actorList[tik].y == self.y:
                    actorLattices.drone.Map[self.x][self.y] = False
                    droneList.actorList.pop(tik)
                    break 
 
    def updateCell(self,fluidLattices, actorLattices, droneList):
       
        self.eatFood(actorLattices,droneList)
        self.moveCell(fluidLattices,actorLattices)
    
    def printCell(self,screen,actorLattices,printStep,printStep_max):
         
        xVec,yVec = self.generateAnimationVectors(actorLattices,printStep_max)
        pygame.draw.circle(screen,(0,0,0),(xVec[printStep],yVec[printStep]),10)
        pygame.draw.circle(screen,(138,43,226),(xVec[printStep],yVec[printStep]),9)

    
