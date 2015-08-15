import numpy
from numpy.random import random_integers as rand

def maze(width, height, complexity=.01, density=.25):
    # TODO work with odd input width and height
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    density    = int(density * (shape[0] // 2 * shape[1] // 2))
    Z = numpy.zeros(shape, dtype=bool)
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1

    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_

    return Z.tolist()


