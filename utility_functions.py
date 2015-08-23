import pygame
import numpy as np
from numpy.random import random_sample
from levelgen import *

def discreteDraw(values,probabilities):

    bins = np.add.accumulate(probabilities)
    out = values[np.digitize(random_sample(1),bins)]
    return round(out[0])

def drawQuantities(screen,droneList,myfont):
 
    label = myfont.render('Drone Count: %d' % (len(droneList.actorList)),4,(0,0,0))
    screen.blit(label,(150,30))

def wrapBoundaries(min_, val, max_):
    return min_ if val > max_ else max_ if val < min_ else val

def keepInBoundaries(min_, val, max_):
    return min_ if val < min_ else max_ if val > max_ else val

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

def getAdjacent(wallMap,x,y):

    adjCells = []
    maxLy = len(wallMap[0][:])-1
    minLy = 0
    maxLx = len(wallMap[:])-1
    minLx = 0
    for x_shift in range(-1,2):
        for y_shift in range(-1,2):
            adjx = x + x_shift
            adjy = y + y_shift
            if not (x_shift == 0 and y_shift == 0):
                if adjx > maxLx:
                    if adjy > maxLy:
                        if wallMap[minLx][minLy]:
                            pass
                        else:
                            adjCells.append([minLx,minLy,x_shift,y_shift]) 
                    elif adjy < minLy:
                        if wallMap[minLx][maxLy]:
                            pass
                        else:
                            adjCells.append([minLx,maxLy,x_shift,y_shift])
                    else:
                        if wallMap[minLx][adjy]:
                            pass
                        else:
                            adjCells.append([minLx,adjy,x_shift,y_shift]) 
                elif adjx < minLx:
                    if adjy > maxLy:
                        if wallMap[maxLx][minLy]:
                            pass
                        else:
                            adjCells.append([maxLx,minLy,x_shift,y_shift]) 
                    elif adjy < minLy:
                        if wallMap[maxLx][maxLy]:
                            pass
                        else:
                            adjCells.append([maxLx,maxLy,x_shift,y_shift]) 
                    else:
                        if wallMap[maxLx][adjy]:
                            pass
                        else:
                            adjCells.append([maxLx,adjy,x_shift,y_shift])
                elif adjy > maxLy:
                    if adjx > maxLx:
                        if wallMap[minLx][minLy]:
                            pass
                        else:
                            adjCells.append([minLx,minLy,x_shift,y_shift])
                    elif adjx < minLx:
                        if wallMap[maxLx][minLy]:
                            pass
                        else:
                            adjCells.append([maxLx,minLy,x_shift,y_shift])     
                    else:
                        if wallMap[adjx][minLy]:
                            pass
                        else:
                            adjCells.append([adjx,minLy,x_shift,y_shift])     
                elif adjy < minLy:
                    if adjx > maxLx:
                        if wallMap[minLx][maxLy]:
                            pass
                        else:
                            adjCells.append([minLx,maxLy,x_shift,y_shift])
                    elif adjx < minLx:
                        if wallMap[maxLx][maxLy]:
                            pass
                        else:
                            adjCells.append([maxLx,maxLy,x_shift,y_shift])     
                    else:
                        if wallMap[adjx][maxLy]:
                            pass
                        else:
                            adjCells.append([adjx,maxLy,x_shift,y_shift])
                else: 
                    if wallMap[adjx][adjy]:
                        pass
                    else:
                        adjCells.append([adjx,adjy,x_shift,y_shift])
    
    return adjCells
                
def detectInput(key,shift,space):
    
    if key[pygame.K_w]:
        if key[pygame.K_a]:
            shift = [-1,-1]
        elif key[pygame.K_d]:
            shift = [-1,1]
        else:
            shift = [-1,0]
    elif key[pygame.K_a]:
        if key[pygame.K_w]:
            shift = [-1,-1]
        elif key[pygame.K_s]:
            shift = [1,-1]
        else:
            shift = [0,-1]
    elif key[pygame.K_s]:
        if key[pygame.K_a]:
            shift = [1,-1]
        elif key[pygame.K_d]:
            shift = [1,1]
        else:
            shift = [1,0]
    elif key[pygame.K_d]:
        if key[pygame.K_s]:
            shift = [1,1]
        elif key[pygame.K_w]:
            shift = [-1,1]
        else:
            shift = [0,1]
    elif key[pygame.K_SPACE]:
        space = True

    return shift,space















