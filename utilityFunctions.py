import pygame
import numpy as np
from numpy.random import random_sample

def discreteDraw(values,probabilities):

    bins = np.add.accumulate(probabilities)
    out = values[np.digitize(random_sample(1),bins)]
    return round(out[0])

def drawQuantities(screen,cellList,myfont):
 
    label = myfont.render('Drone Count: %d' % (len(cellList.celist)),4,(0,0,0))
    screen.blit(label,(150,30))

def wrapBoundaries(min_, val, max_):
    return min_ if val > max_ else max_ if val < min_ else val

def keepInBoundaries(min_, val, max_):
    return min_ if val < min_ else max_ if val > max_ else val

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
                
def detectInput(key):

    if key[pygame.K_w]:
        pass















