from lookcells import *
from cell import *

class mother(cell):

    def __init__(self,lattice,x,y):
        cell.__init__(self,lattice,x,y)
        self.species = 'mother'
        lattice.motherMap[x][y] = True
        self.foodDropTimer = 1.0

    def dropFood(self,lattice,foodList):
        
        if self.foodDropTimer < 0.0:
            foodList.addFood(lattice,self.x,self.y)
            self.foodDropTimer = 1.0
            

    def updateCell(self,lattice,foodList):
       
        self.moveCell(lattice)
        self.dropFood(lattice,foodList)
        self.foodDropTimer = self.foodDropTimer - 0.1

    def printCell(self,screen,lattice):
        pygame.draw.circle(screen,(255,165,0),(lattice.points[self.x][self.y].location[0],lattice.points[self.x][self.y].location[1]),10)


