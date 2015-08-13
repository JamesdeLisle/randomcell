import pygame
import numpy as np
from numpy.random import random_sample

def discreteDraw(values,probabilities):

    bins = np.add.accumulate(probabilities)
    out = values[np.digitize(random_sample(1),bins)]
    return round(out[0])

def getAdjacent(wallMap,x,y):

    adjCells = []
    maxL = 29
    minL = 0
    for x_shift in range(-1,2):
        for y_shift in range(-1,2):
            adjx = x + x_shift
            adjy = y + y_shift
            if not (x_shift == 0 and y_shift == 0):
                if adjx > maxL:
                    if adjy > maxL:
                        if wallMap[minL][minL]:
                            pass
                        else:
                            adjCells.append([minL,minL,x_shift,y_shift]) 
                    elif adjy < minL:
                        if wallMap[minL][maxL]:
                            pass
                        else:
                            adjCells.append([minL,maxL,x_shift,y_shift])
                    else:
                        if wallMap[minL][adjy]:
                            pass
                        else:
                            adjCells.append([minL,adjy,x_shift,y_shift]) 
                elif adjx < minL:
                    if adjy > maxL:
                        if wallMap[maxL][minL]:
                            pass
                        else:
                            adjCells.append([maxL,minL,x_shift,y_shift]) 
                    elif adjy < minL:
                        if wallMap[maxL][maxL]:
                            pass
                        else:
                            adjCells.append([maxL,maxL,x_shift,y_shift]) 
                    else:
                        if wallMap[maxL][adjy]:
                            pass
                        else:
                            adjCells.append([maxL,adjy,x_shift,y_shift])
                elif adjy > maxL:
                    if adjx > maxL:
                        if wallMap[minL][minL]:
                            pass
                        else:
                            adjCells.append([minL,minL,x_shift,y_shift])
                    elif adjx < minL:
                        if wallMap[maxL][minL]:
                            pass
                        else:
                            adjCells.append([maxL,minL,x_shift,y_shift])     
                    else:
                        if wallMap[adjx][minL]:
                            pass
                        else:
                            adjCells.append([adjx,minL,x_shift,y_shift])     
                elif adjy < minL:
                    if adjx > maxL:
                        if wallMap[minL][maxL]:
                            pass
                        else:
                            adjCells.append([minL,maxL,x_shift,y_shift])
                    elif adjx < minL:
                        if wallMap[maxL][maxL]:
                            pass
                        else:
                            adjCells.append([maxL,maxL,x_shift,y_shift])     
                    else:
                        if wallMap[adjx][maxL]:
                            pass
                        else:
                            adjCells.append([adjx,maxL,x_shift,y_shift])
                else: 
                    if wallMap[adjx][adjy]:
                        pass
                    else:
                        adjCells.append([adjx,adjy,x_shift,y_shift])
    
    return adjCells
                   
def giveCoord(x,y):
    
    incoord = [x,y]
    outcoord = [0,0]
    for tik in range(2):
        if incoord[tik] > 29:
            outcoord[tik] = 0
        elif incoord[tik] < 0:
            outcoord[tik] = 29
        else:
            outcoord = incoord

    return outcoord














