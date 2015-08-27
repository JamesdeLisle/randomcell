import pygame
from cell_drone import *
from food import *
from cell_zombie import *
from cell import *
from cell_mother import *

class activeActors(object):

    def __init__(self):
        self.actorList = []

    def numberOfCells(self):
        return len(self.actorList)

class allDrones(activeActors):

    def __init__(self):
        activeActors.__init__(self)

    def addCell(self,actorLattices,x,y):
        self.actorList.append(drone(actorLattices,x,y))

    def updateCells(self,fluidLattices,actorLattices,foodList):
        map(lambda drone: drone.updateCell(fluidLattices,actorLattices,foodList), self.actorList)

    def printCells(self,screen, actorLattices, printStep, printStep_max):
        map(lambda drone: drone.printCell(screen,actorLattices,printStep,printStep_max), self.actorList)


class allFood(activeActors):

    def __init__(self):
        activeActors.__init__(self)

    def addCell(self,actorLattices,x,y):
        self.actorList.append(food(actorLattices,x,y))

    def printCells(self,screen,actorLattices):
        map(lambda food: food.printCell(screen,actorLattices), self.actorList)

class allZombies(activeActors):

    def __init__(self):
        activeActors.__init__(self)

    def addCell(self,actorLattices,x,y):
        self.actorList.append(zombie(actorLattices,x,y))

    def updateCells(self,fluidLattices, actorLattices, droneList):
        map(lambda zombie: zombie.updateCell(fluidLattices, actorLattices, droneList), self.actorList)

    def printCells(self,screen,actorLattices,printStep,printStep_max):
        map(lambda zombie: zombie.printCell(screen,actorLattices,printStep,printStep_max), self.actorList)

class allMothers(activeActors):

    def __init__(self):
        activeActors.__init__(self)

    def addCell(self,actorLattices,x,y):
        self.actorList.append(mother(actorLattices,x,y))

    def updateCells(self,fluidLattices,actorLattices,foodList):
        map(lambda mother: mother.updateCell(fluidLattices,actorLattices,foodList), self.actorList)

    def printCells(self,screen,actorLattices,printStep,printStep_max):
        map(lambda mother: mother.printCell(screen,actorLattices,printStep,printStep_max), self.actorList)

def placeFood(fluidLattices,actorLattices,foodList):
 
    mouse_position = pygame.mouse.get_pos()
    locx = 0
    locy = 0
    diffprev = 1000.0
    diffcurr = 1000.0
    
    for tik1 in range(actorLattices.drone.height):
        diffcurr = actorLattices.drone.points[tik1][0].location[1] - mouse_position[1]
        if abs(diffcurr) < abs(diffprev):
            locx = tik1
            diffprev = diffcurr 
    diffprev = 1000.0
    diffcurr = 1000.0

    for tik1 in range(actorLattices.drone.width):
        diffcurr = actorLattices.drone.points[5][tik1].location[0] - mouse_position[0]
        
        if abs(diffcurr) < abs(diffprev):
            locy = tik1
            diffprev = diffcurr
    
    if actorLattices.food.Map[locx][locy]:
        pass
    elif fluidLattices.wall.Map[locx][locy]:
        pass
    else:
        foodList.addCell(actorLattices,locx,locy)

def createChildren(actorLattices,droneList):

    for tik1 in range(len(droneList.actorList)):
        for tik2 in range(len(droneList.actorList)):
            if droneList.actorList[tik1].x == droneList.actorList[tik2].x and \
                    droneList.actorList[tik1].x == droneList.actorList[tik2].x and \
                    droneList.actorList[tik1].birthometer == 0 and \
                    droneList.actorList[tik2].birthometer == 0 and \
                    droneList.actorList[tik1].hunger < 0.25 and \
                    droneList.actorList[tik2].hunger < 0.25 and \
                    tik1 != tik2:
                droneList.addCell(actorLattices,droneList.actorList[tik1].x,droneList.actorList[tik1].y)
                droneList.actorList[tik1].birthometer = 100
                droneList.actorList[tik2].birthometer = 100

def killDying(actorLattices,droneList):

    for tik1 in range(len(droneList.actorList)):
        if droneList.actorList[tik1].deathsdoor > 1.0:
            actorLattices.drone.Map[droneList.actorList[tik1].x][droneList.actorList[tik1].y] = False
            droneList.actorList.pop(tik1)
            break
  
   
