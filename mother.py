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

    def printCell(self,screen,lattice,printStep,printStep_max):
        
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
        pygame.draw.circle(screen,(255,165,0),(xVec[printStep],yVec[printStep]),9)


