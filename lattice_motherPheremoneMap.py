from utility_functions import *
from lattice import *

class motherPheremoneMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ 0.0 for x in range(self.width)] for y in range(self.height)]
        self.dissipation = 0.95
        self.cutoff = 1e-2
 
