from lattice_actors import *
from lattice_fluids import *

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


