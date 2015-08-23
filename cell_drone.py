from utility_functions import *
from cell import *
import numpy as np

class drone(cell):

    def __init__(self,actorLattices,x,y):
        cell.__init__(self,x,y)
        self.species = 'drone'
        actorLattices.drone.Map[x][y] = True
        self.birthometer = 0
        self.deathsdoor = 0.0
        self.moveToDesire = 8.0
        self.moveAwayDanger = 1000.0
        self.moveToOther = 1.0
        self.moveNowhere = 5.0
        self.output = 0.0 #(1 - self.hunger) * 2.0

        
    def eatFood(self,actorLattices,foodList):
        
        if actorLattices.food.Map[self.x][self.y]:
            self.hunger = 0.0
            actorLattices.food.Map[self.x][self.y] = False
            for tik in range(len(foodList.actorList)):
                if foodList.actorList[tik].x == self.x and foodList.actorList[tik].y == self.y:
                    foodList.actorList.pop(tik)
                    break    

    def updateCell(self,fluidLattices,actorLattices,foodList):
       
        self.eatFood(actorLattices,foodList)
        self.moveCell(fluidLattices,actorLattices)
        self.hunger = self.hunger + 0.01
        self.birthometer = self.birthometer - 1
        self.output = (1 - self.hunger) * 2.0

        if self.birthometer < 1:
            self.birthometer = 0
        if self.hunger > 1.0:
            self.deathsdoor = self.deathsdoor + 0.1

    def printCell(self, screen, actorLattices, printStep, printStep_max):
        
        green = round((1-self.hunger)*255) 
        blue = round(self.hunger*255)
        green = keepInBoundaries(0,green,255)
        blue = keepInBoundaries(0,blue,255)
        
        xVec,yVec = self.generateAnimationVectors(actorLattices, printStep_max) 
        pygame.draw.circle(screen,(0,0,0),(xVec[printStep],yVec[printStep]),10)
        pygame.draw.circle(screen,(0,green,blue),(xVec[printStep],yVec[printStep]),9)
        


