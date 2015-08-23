from lattice_droneMap import *
from lattice_emptyMap import *
from lattice_foodMap import *
from lattice_heatMap import *
from lattice_heroMap import *
from lattice_motherMap import *
from lattice_motherPheremoneMap import *
from lattice_smellMap import *
from lattice_wallMap import *
from lattice_zombieMap import *
from lattice_zombiePheremoneMap import *


class actorLattice:

    def __init__(self,width,height):

        self.drone = droneMap(width,height)
        self.food = foodMap(width,height)
        self.mother = motherMap(width,height)
        self.zombie = zombieMap(width,height)
        self.hero = heroMap(width,height)
        
class fluidLattice:

    def __init__(self,width,height):
        
        self.empty = emptyMap(width,height)
        self.wall = wallMap(width,height)
        self.heat = heatMap(width,height)
        self.smell = smellMap(width,height)
        self.motherPheremone = motherPheremoneMap(width,height)
        self.zombiePheremone = zombiePheremoneMap(width,height)


