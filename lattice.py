import pygame
from utility_functions import *
from levelgen import *

class latAttribute:

    def __init__(self,x,y):
        self.location = [110+(x*20),110+(y*20)]

class lattice:

    def __init__(self,width,height):

        self.width = width
        self.height = height
        self.points = [ [ latAttribute(x,y) for x in range(self.width)] for y in range(self.height)] 
        
    def updateMap(self,wallMap,actorLists):
       
        temp = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
       
        for xPos in range(self.height):
            for yPos in range(self.width):
                self.Map[xPos][yPos] = self.Map[xPos][yPos] * self.dissipation
                
                for lists in range(len(actorLists[:])):
                    for actors in range(len(actorLists[lists].actorList)):
                        if actorLists[lists].actorList[actors].x == xPos and actorLists[lists].actorList[actors].y == yPos:
                            self.Map[xPos][yPos] = actorLists[lists].actorList[actors].output
                
                adjCells = getAdjacent(wallMap.Map,xPos,yPos)

                if len(adjCells) == 0:
                    pass
                else:
                    scale = 1.0/len(adjCells[:])
                    for adj in range(len(adjCells[:])):
                        xAdj = adjCells[adj][0]
                        yAdj = adjCells[adj][1]
                        temp[xAdj][yAdj] = temp[xAdj][yAdj] + self.Map[xPos][yPos] * scale
                        
                if temp[xPos][yPos] < self.cutoff:
                    temp[xPos][yPos] = 0.0  
         
        self.Map_old = self.Map
        self.Map = temp 
