import pygame
import numpy as np
from numpy.random import random_sample

def discreteDraw(values,probabilities):

    bins = np.add.accumulate(probabilities)
    out = values[np.digitize(random_sample(1),bins)]
    return round(out[0])

def getAdjacent(wallMap,x,y):

    adjCells = []
    minX = 0
    maxX = len(wallMap) - 1
    minY = 0
    maxY = len(wallMap[0]) - 1

    for x_shift in range(-1,2):
        for y_shift in range(-1,2):
            adjx = x + x_shift
            adjy = y + y_shift
            if (
                not (x_shift == 0 and y_shift == 0) and
                not adjx > maxX and
                not adjx < minX and
                not adjy > maxY and
                not adjy < minY and
                not wallMap[adjx][adjy]
            ):
                adjCells.append([adjx, adjy, x_shift, y_shift])


    return adjCells













