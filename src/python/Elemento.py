import numpy as np
import math
from No import *


class Elemento:
    def __init__(self, no1: No, no2: No, theta, el_type, l=None, k=None, ae=None, ei=None):
        self.no1 = no1
        self.no2 = no2
        self.theta = theta
        self.n = math.sin(math.radians(theta))
        self.m = math.cos(math.radians(theta))
        self.type = el_type
        self.k = k               # Mola
        self.ae = ae             # Barra
        self.l = l               # Barra Viga Portico
        self.ei = ei             # Viga Portico
        self.phi = 12*ei/l**3    # Viga Portico
        self.lmbda = 6*ei/l**2   # Viga Portico
        self.rho = 2*ei/l        # Viga Portico

    def matriz_local(self):
        mat = np.array([self.no1.gl_x, self.no1.gl_y])


