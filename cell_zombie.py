from lookcells import *
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
        pygame.draw.circle(screen,(138,43,226),(xVec[printStep],yVec[printStep]),9)

    
