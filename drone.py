from lookcells import *
from cell import *
import numpy as np

class drone(cell):

    def __init__(self,lattice,x,y):
        cell.__init__(self,lattice,x,y)
        self.species = 'drone'
        lattice.cellMap[x][y] = True
        self.birthometer = 0
        self.deathsdoor = 0.0
        
    def eatFood(self,lattice,foodList):
        
        if lattice.foodMap[self.x][self.y]:
            self.hunger = 0.0
            lattice.foodMap[self.x][self.y] = False
            for tik in range(len(foodList.foodList)):
                if foodList.foodList[tik].x == self.x and foodList.foodList[tik].y == self.y:
                    foodList.foodList.pop(tik)
                    break    

    def updateCell(self,lattice,foodList,cellList):
       
        self.eatFood(lattice,foodList)
        self.moveCell(lattice)
        self.hunger = self.hunger + 0.01
        self.birthometer = self.birthometer - 1
        
        if self.birthometer < 1:
            self.birthometer = 0
        if self.hunger > 1.0:
            self.deathsdoor = self.deathsdoor + 0.1

    def printCell(self, screen, lattice, printStep, printStep_max):
        
        green = round((1-self.hunger)*255) 
        blue = round(self.hunger*255)
        green = keepInBoundaries(0,green,255)
        blue = keepInBoundaries(0,blue,255)
        xpos = lattice.points[self.x][self.y].location[0]
        ypos = lattice.points[self.x][self.y].location[1]

        xmin = lattice.points[self.previous_x][self.previous_y].location[0]
        xmax = lattice.points[self.x][self.y].location[0]
        ymin = lattice.points[self.previous_x][self.previous_y].location[1]
        ymax = lattice.points[self.x][self.y].location[1]

        xVec = np.linspace(xmin,xmax,printStep_max).tolist()
        yVec = np.linspace(ymin,ymax,printStep_max).tolist()

        xVec = [ int(round(x)) for x in xVec ]
        yVec = [ int(round(x)) for x in yVec ]

        pygame.draw.circle(screen,(0,0,0),(xVec[printStep],yVec[printStep]),10)
        pygame.draw.circle(screen,(0,green,blue),(xVec[printStep],yVec[printStep]),9)
        


