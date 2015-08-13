import pygame
import numpy as np
from lookcells import *
from scipy import stats

class zombieCell:

    def __init__(self,lattice,x,y):
        self.x = x
        self.y = y
        lattice.zombieCellMap[x][y] = True
        self.hunger = 0.0
        
    def eatFood(self,lattice,cellList):
        
        if lattice.cellMap[self.x][self.y]:
            self.hunger = 0.0
            for tik in range(len(cellList.celist)):
                if cellList.celist[tik].x == self.x and cellList.celist[tik].y == self.y:
                    lattice.cellMap[self.x][self.y] = False
                    cellList.celist.pop(tik)
                    break
    
    def whereHeat(self,lattice):
        
        thatHeat = 0.0
        heatDirection = [0,0]
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        
        for tik in range(len(adjCells[:])):
            xpos = adjCells[tik][0]
            ypos = adjCells[tik][1]
            if lattice.heatMap[xpos][ypos] > thatHeat:
                thatHeat = lattice.heatMap[xpos][ypos]
                heatDirection[0] = adjCells[tik][0]
                heatDirection[1] = adjCells[tik][1]

        return heatDirection

    def weightWalk(self,lattice,heatDirection):

        weights = []
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        nCells = len(adjCells[:])
        for tik in range(nCells):
            if adjCells[tik][0] == heatDirection[0] and adjCells[tik][1] == heatDirection[1]:
                weights.append(16.0)
            else:
                weights.append(1.0)

        weights.append(10.0 * self.hunger)
        norm = sum(weights)
        for tik in range(len(weights)):
            weights[tik] = weights[tik]/norm

        return weights

    def generateNextPosition(self,lattice,weights):

        draw = [np.random.uniform(), np.random.uniform()]
        shift = [0,0]
        adjCells = getAdjacent(lattice.wallMap,self.x,self.y)
        cellNum = np.array([ x for x in range(len(adjCells[:])+1)])
        probs = np.array(weights)
        choice = discreteDraw(cellNum,probs)
        if choice == len(cellNum)-1:
            shift = [0,0]
        else:
            shift = [adjCells[int(choice)][2],adjCells[int(choice)][3]]

        return shift
 
    def moveCell(self,lattice):
        
        heatDirection = self.whereHeat(lattice)
        weights = self.weightWalk(lattice,heatDirection) 
        shift = self.generateNextPosition(lattice,weights)

        lattice.cellMap[self.x][self.y] = False
        self.x = self.x + shift[0]
        self.y = self.y + shift[1]
        
        minL = 0
        maxL = len(lattice.points[0])-1
        if self.x > maxL:
            self.x = minL
        elif self.x < minL:
            self.x = maxL
        if self.y > maxL:
            self.y = minL
        elif self.y < minL:
            self.y = maxL
    
    def updateCellMap(self,lattice):
        
        minL = 0
        maxL = 29
        
        if self.x > maxL:
            if self.y > maxL:
                lattice.cellMap[minL][minL] = True
            elif self.y < minL:
                lattice.cellMap[minL][maxL] = True
        elif self.x < minL:
            if self.y > maxL:
                lattice.cellMap[maxL][minL] = True
            elif self.y < minL:
                lattice.cellMap[maxL][maxL] = True
        elif self.y > maxL:
            if self.x > maxL:
                lattice.cellMap[minL][minL] = True
            elif self.x < minL:
                lattice.cellMap[maxL][minL] = True
        elif self.y < minL:
            if self.x > maxL:
                lattice.cellMap[minL][maxL] = True
            elif self.x < minL:
                lattice.cellMap[maxL][maxL] = True
        else: 
            lattice.cellMap[self.x][self.y] = True
            
    def updateCell(self,lattice,cellList):
       
        self.eatFood(lattice,cellList)
        self.moveCell(lattice)
        self.updateCellMap(lattice) 
        self.hunger = self.hunger + 0.05

    def printCell(self,screen,lattice):
        pygame.draw.circle(screen,(138,43,226),(lattice.points[self.x][self.y].location[0],lattice.points[self.x][self.y].location[1]),10)


