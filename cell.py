import pygame
import numpy as np
from utility_functions import *
from scipy import stats

class cell(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.previous_x = 0
        self.previous_y = 0
        self.hunger = 0.0
    
    def whereMotives(self,fluidLattices):
        
        thatDanger = 0.0
        thatDesire = 0.0
        dangerDirection = [0,0]
        desireDirection = [0,0]
        adjCells = getAdjacent(fluidLattices.wall.Map,self.x,self.y)
        
        for tik in range(len(adjCells[:])):
            xAdj = adjCells[tik][0]
            yAdj = adjCells[tik][1]
        
            if self.species == 'drone':
                thisDanger = fluidLattices.zombiePheremone.Map[xAdj][yAdj]
                thisDesire = fluidLattices.smell.Map[xAdj][yAdj]
            elif self.species == 'zombie':
                thisDanger = fluidLattices.motherPheremone.Map[xAdj][yAdj]
                thisDesire = fluidLattices.heat.Map[xAdj][yAdj]
            elif self.species == 'mother':
                thisDanger = fluidLattices.empty.Map[xAdj][yAdj]
                thisDesire = fluidLattices.heat.Map[xAdj][yAdj] 

            if thisDanger > thatDanger:
                thatDanger = thisDanger
                dangerDirection[0] = adjCells[tik][0]
                dangerDirection[1] = adjCells[tik][1]
            
            if thisDesire > thatDesire:
                thatDesire = thisDesire
                desireDirection[0] = adjCells[tik][0]
                desireDirection[1] = adjCells[tik][1]

        return (dangerDirection,desireDirection)
 
    def weightWalk(self,fluidLattices,motiveDirection):

        weightsDesire = []
        weightsDanger = []
        adjCells = getAdjacent(fluidLattices.wall.Map,self.x,self.y)
        nCells = len(adjCells[:])
        
        for tik in range(nCells):
            if adjCells[tik][0] == motiveDirection[1][0] and adjCells[tik][1] == motiveDirection[1][1]:
                weightsDesire.append(self.moveToDesire)
            else:
                weightsDesire.append(self.moveToOther)

            if adjCells[tik][0] == motiveDirection[0][0] and adjCells[tik][1] == motiveDirection[0][1]: 
                    weightsDanger.append(1.0/self.moveAwayDanger)
            else:
                weightsDanger.append(self.moveToOther)
         
        weightsDanger.append(self.moveNowhere * self.hunger)
        normDanger = sum(weightsDanger)
        weightsDesire.append(self.moveNowhere * self.hunger)
        normDesire = sum(weightsDesire)
        weightsDanger = [ a/normDanger for a in weightsDanger ]
        weightsDesire = [ a/normDesire for a in weightsDesire ] 
        weightsDanger = [ round(a,2) for a in weightsDanger ]
        weightsDesire = [ round(a,2) for a in weightsDesire ]
        weights = [ a*b for a,b in zip(weightsDanger,weightsDesire)]
        norm = sum(weights)
        weights = [ a/norm for a in weights]
        
        return weights  
    
    def generateNextPosition(self,fluidLattices,weights):

        draw = [np.random.uniform(), np.random.uniform()]
        shift = [0,0]
        adjCells = getAdjacent(fluidLattices.wall.Map,self.x,self.y)
        cellNum = np.array([ x for x in range(len(adjCells[:])+1)])
        probs = np.array(weights)
        choice = discreteDraw(cellNum,probs)

        if choice == len(cellNum)-1:
            shift = [0,0]
        else:
            shift = [adjCells[int(choice)][2],adjCells[int(choice)][3]]

        return shift
   
    def updateCellMap(self,actorLattices,flag):
        
        if self.species == 'drone':
            actorLattices.drone.Map[self.x][self.y] = flag
        elif self.species == 'zombie':
            actorLattices.zombie.Map[self.x][self.y] = flag
        elif self.species == 'mother':
            actorLattices.mother.Map[self.x][self.y] = flag
        elif self.species == 'hero':
            actorLattices.hero.Map[self.x][self.y] = flag

    def moveCell(self,fluidLattices,actorLattices):
        
        motiveDirection = self.whereMotives(fluidLattices)
        weights = self.weightWalk(fluidLattices,motiveDirection) 
        shift = self.generateNextPosition(fluidLattices,weights)
 
        self.updateCellMap(actorLattices,False)
        self.previous_x = self.x
        self.previous_y = self.y
        self.x = self.x + shift[0]
        self.y = self.y + shift[1]
        self.updateCellMap(actorLattices,True)
        minLx = 0
        minLy = 0
        maxLy = actorLattices.drone.width
        maxLx = actorLattices.drone.height
        self.x = wrapBoundaries(minLx,self.x,maxLx)
        self.y = wrapBoundaries(minLy,self.y,maxLy)

    def generateAnimationVectors(self,actorLattices,printStep_max):
        
        xpos = actorLattices.drone.points[self.x][self.y].location[0]
        ypos = actorLattices.drone.points[self.x][self.y].location[1]
        xmin = actorLattices.drone.points[self.previous_x][self.previous_y].location[0]
        xmax = actorLattices.drone.points[self.x][self.y].location[0]
        ymin = actorLattices.drone.points[self.previous_x][self.previous_y].location[1]
        ymax = actorLattices.drone.points[self.x][self.y].location[1]
        xVec = np.linspace(xmin,xmax,printStep_max).tolist()
        yVec = np.linspace(ymin,ymax,printStep_max).tolist()
        xVec = [ int(round(x)) for x in xVec ]
        yVec = [ int(round(x)) for x in yVec ]

        return xVec,yVec
        
    
 
