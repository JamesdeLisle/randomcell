import pygame
from drone import *
from food import *
from zombie import *
from cell import *
from mother import *

class allCells:

    def __init__(self):
        self.celist = []

    def addCell(self,lattice,x,y):
        self.celist.append(drone(lattice,x,y))

    def updateCells(self,screen,lattice,foodList,cellList):
        map(lambda cell: cell.updateCell(lattice,foodList,cellList), self.celist)

    def printCells(self,screen,lattice):
        map(lambda cell: cell.printCell(screen,lattice), self.celist)

    def numberOfCells(self):
        return len(self.celist)

class allFood:

    def __init__(self):
        self.foodList = []

    def addFood(self,lattice,x,y):
        self.foodList.append(food(lattice,x,y))

    def updateFoods(self,screen,lattice):
        map(lambda food: food.printFood(screen,lattice), self.foodList)

class allZombies:
    def __init__(self):
        self.zombieList = []

    def addZombie(self,lattice,x,y):
        self.zombieList.append(zombie(lattice,x,y))

    def updateZombies(self,screen,lattice,cellList):
        map(lambda zombie: zombie.updateCell(lattice,cellList), self.zombieList)

    def printZombies(self,screen,lattice):
        map(lambda zombie: zombie.printCell(screen,lattice), self.zombieList)

    def numberOfCells(self):
        return len(self.zombieList)

class allMothers:
    def __init__(self):
        self.motherList = []

    def addMother(self,lattice,x,y):
        self.motherList.append(mother(lattice,x,y))

    def updateMothers(self,screen,lattice,foodList):
        map(lambda mother: mother.updateCell(lattice,foodList), self.motherList)

    def printMothers(self,screen,lattice):
        map(lambda mother: mother.printCell(screen,lattice), self.motherList)

    def numberOfCells(self):
        return len(self.motherList)

def placeFood(lattice,foodList):
    
    mouse_position = pygame.mouse.get_pos()
    locx = 0
    locy = 0
    diffprev = 1000.0
    diffcurr = 1000.0
    
    for tik1 in range(lattice.height):
        diffcurr = lattice.points[tik1][0].location[1] - mouse_position[1]
        if abs(diffcurr) < abs(diffprev):
            locx = tik1
            diffprev = diffcurr 
    diffprev = 1000.0
    diffcurr = 1000.0

    for tik1 in range(lattice.width):
        diffcurr = lattice.points[5][tik1].location[0] - mouse_position[0]
        
        if abs(diffcurr) < abs(diffprev):
            locy = tik1
            diffprev = diffcurr
    
    if lattice.foodMap[locx][locy]:
        pass
    elif lattice.wallMap[locx][locy]:
        pass
    else:
        foodList.addFood(lattice,locx,locy)

def createChildren(lattice,cellList):

    for tik1 in range(len(cellList.celist)):
        for tik2 in range(len(cellList.celist)):
            if cellList.celist[tik1].x == cellList.celist[tik2].x and \
                    cellList.celist[tik1].x == cellList.celist[tik2].x and \
                    cellList.celist[tik1].birthometer == 0 and \
                    cellList.celist[tik2].birthometer == 0 and \
                    cellList.celist[tik1].hunger < 0.25 and \
                    cellList.celist[tik2].hunger < 0.25 and \
                    tik1 != tik2:
                cellList.addCell(lattice,cellList.celist[tik1].x,cellList.celist[tik1].y)
                cellList.celist[tik1].birthometer = 20
                cellList.celist[tik2].birthometer = 20

def killDying(lattice,cellList):

    for tik1 in range(len(cellList.celist)):
        if cellList.celist[tik1].deathsdoor > 1.0:
            lattice.cellMap[cellList.celist[tik1].x][cellList.celist[tik1].y] = False
            cellList.celist.pop(tik1)
            break
  
   
