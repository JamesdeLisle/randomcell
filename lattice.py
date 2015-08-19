import pygame
from lookcells import *
from levelgen import *


class latAttribute:

    def __init__(self,x,y):
        self.location = [110+(x*20),110+(y*20)]
         
def createWallMap(width,height):

    wallMap = [ [ False for x in range(width)] for y in range(height)]
   
    level = 0
    
    if level == 0:
        wallMap = generate_maze(width,height)
    elif level == 1:
        for tik1 in range(height):
            for tik2 in range(width):
                if tik1 % 2 == 0 and tik2 % 2 == 0:
                    wallMap[tik1][tik2] = True
    elif level == 2:
        for tik1 in range(height):
            for tik2 in range(width):
                if 10 <= tik1 <= 20  and 10 <= tik2 <= 20:
                    wallMap[tik1][tik2] = True
    elif level == 3:
        for tik1 in range(height):
            for tik2 in range(width):
                if 0 < tik1 < 15  and tik2 == 10:
                    wallMap[tik1][tik2] = True

    return wallMap

class lattice:

    def __init__(self,width,height):

        self.width = width
        self.height = height
        self.points = [ [ latAttribute(x,y) for x in range(self.width)] for y in range(self.height)]
        self.wallMap = createWallMap(width,height)
        self.heatMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.cellMap = [ [ False for x in range(self.width)] for y in range(self.height)]
        self.foodMap = [ [ False for x in range(self.width)] for y in range(self.height)]
        self.smellMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.zombieCellMap = [ [ False for x in range(self.width)] for y in range(self.height)]
        self.motherMap = [ [ False for x in range(self.width)] for y in range(self.height)]
        self.motherPherMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.zombiePherMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]

        self.emptyMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        
    def updateMaps(self,cellList,zombieList,motherList):
       
        tempHeatMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        tempSmellMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        tempZombiePherMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        tempMotherPherMap = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        
        for tik1 in range(self.height):
            for tik2 in range(self.width):
                self.heatMap[tik1][tik2] = self.heatMap[tik1][tik2] * 0.95
                self.smellMap[tik1][tik2] = self.smellMap[tik1][tik2] * 0.8
                self.motherPherMap[tik1][tik2] = self.motherPherMap[tik1][tik2] * 0.95 
                self.zombiePherMap[tik1][tik2] = self.zombiePherMap[tik1][tik2] * 0.95

                if self.cellMap[tik1][tik2]:
                    for tik3 in range(len(cellList.celist)):
                        if cellList.celist[tik3].x == tik1 and cellList.celist[tik3].y == tik2:
                            self.heatMap[tik1][tik2] = (1 - cellList.celist[tik3].hunger) * 2.0
                
                if self.foodMap[tik1][tik2]:
                    self.smellMap[tik1][tik2] = 1.0
                
                if self.motherMap[tik1][tik2]:
                    for tik3 in range(len(motherList.motherList)):
                        if motherList.motherList[tik3].x == tik1 and motherList.motherList[tik3].y == tik2:
                            self.motherPherMap[tik1][tik2] = 2.0

                if self.zombieCellMap[tik1][tik2]:
                    for tik3 in range(len(zombieList.zombieList)):
                        if zombieList.zombieList[tik3].x == tik1 and zombieList.zombieList[tik3].y == tik2:
                            self.zombiePherMap[tik1][tik2] = 2.0
                
                adjCells = getAdjacent(self.wallMap,tik1,tik2)

                if len(adjCells) == 0:
                    pass
                else:
                    scale = 1.0/len(adjCells[:])
                    for tik3 in range(len(adjCells[:])):
                        xpos = adjCells[tik3][0]
                        ypos = adjCells[tik3][1]
                        tempHeatMap[xpos][ypos] = tempHeatMap[xpos][ypos] + self.heatMap[tik1][tik2] * scale
                        tempSmellMap[xpos][ypos] = tempSmellMap[xpos][ypos] + self.smellMap[tik1][tik2] * scale
                        tempZombiePherMap[xpos][ypos] = tempZombiePherMap[xpos][ypos] + self.zombiePherMap[tik1][tik2] * scale
                        tempMotherPherMap[xpos][ypos] = tempMotherPherMap[xpos][ypos] + self.motherPherMap[tik1][tik2] * scale
                        
                if tempHeatMap[tik1][tik2] < 1e-2:
                    tempHeatMap[tik1][tik2] = 0
                if tempMotherPherMap[tik1][tik2] < 1e-2:
                    tempMotherPherMap[tik1][tik2] = 0
                if tempZombiePherMap[tik1][tik2] < 1e-1:
                    tempZombiePherMap[tik1][tik2] = 0

        self.heatMap = tempHeatMap
        self.smellMap = tempSmellMap
        self.motherPherMap = tempMotherPherMap
        self.zombiePherMap = tempZombiePherMap

    def colorWallMap(self,screen):

        for tik1 in range(self.height):
            for tik2 in range(self.width):
                xpos = self.points[tik1][tik2].location[0]-9
                ypos = self.points[tik1][tik2].location[1]-9
                width = 19
                height = 19
                if self.wallMap[tik1][tik2]:
                    pygame.draw.rect(screen,(0,0,0),(xpos,ypos,width,height))
    
    def colorSmellMap(self,screen):
        
        for tik1 in range(self.height):
            for tik2 in range(self.width):
                len(self.heatMap[0]) 
                
                cValue = round((1-self.smellMap[tik1][tik2])*255/1.5)

                cValue = keepInBoundaries(0,cValue,255)
                 
                xpos = self.points[tik1][tik2].location[0]
                ypos = self.points[tik1][tik2].location[1]
                if self.smellMap[tik1][tik2] > 1e-2 and cValue < 250:
                    pygame.draw.circle(screen,(cValue,255,cValue),(xpos,ypos),4)
                 
    def colorHeatMap(self,screen):
        
        for tik1 in range(self.height):
            for tik2 in range(self.width):
                len(self.heatMap[0]) 
                cValue = round((1-self.heatMap[tik1][tik2])*255)
                cValue = keepInBoundaries(0,cValue,255) 
                xpos = self.points[tik1][tik2].location[0]-9
                ypos = self.points[tik1][tik2].location[1]-9
                width = 18
                height = 18
                if self.heatMap[tik1][tik2] != 0:
                    pygame.draw.rect(screen,(255,cValue,cValue),(xpos,ypos,width,height))
                

