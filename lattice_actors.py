from utility_functions import *
from lattice import *

class droneMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ False for x in range(self.width)] for y in range(self.height)]

class foodMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ False for x in range(self.width)] for y in range(self.height)]

class heroMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ False for x in range(self.width)] for y in range(self.height)]

class motherMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ False for x in range(self.width)] for y in range(self.height)]

class zombieMap(lattice):

    def __init__(self,width,height):
        lattice.__init__(self,width,height)
        self.Map = [ [ False for x in range(self.width)] for y in range(self.height)]




        
