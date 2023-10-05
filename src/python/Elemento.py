import numpy as np
import math
from No import *


class Elemento:
    def __init__(self, no1: No, no2: No, theta, el_type, l=None, k=None, ae=None, ei=None):
        self.no1 = no1
        self.no2 = no2
        self.theta = float(theta)
        self.n = round(math.sin(theta), 6)
        self.m = round(math.cos(theta), 6)
        self.el_type = el_type
        if self.el_type == "Mola":
            self.k = float(k)                          # Mola
        else:
            self.l = float(l)                          # Barra Viga Portico
            if self.el_type == "Barra":
                self.ae = float(ae)                    # Barra
            else:
                self.ei = float(ei)                    # Viga Portico
                self.phi = 12*float(ei)/float(l)**3    # Viga Portico
                self.lmbda = 6*float(ei)/float(l)**2   # Viga Portico
                self.rho = 2*float(ei)/float(l)        # Viga Portico
        self.ke = 0

    def __repr__(self):
        return f"""{self.el_type} ({self.no1} {self.no2})"""

    def matriz_local(self):
        if self.el_type == "Mola":
            self.ke = self.k * np.array([[self.m * self.m, self.m * self.n, -self.m * self.m, -self.m * self.n, 0, 0],
                                    [self.m * self.n, self.n * self.n, -self.m * self.n, -self.n * self.n, 0, 0],
                                    [-self.m * self.m, -self.m * self.n, self.m * self.m, self.m * self.n, 0, 0],
                                    [-self.m * self.n, -self.n * self.n, self.m * self.n, self.n * self.n, 0, 0],
                                    [0,                0,                0,               0,               0, 0],
                                    [0, 0, 0, 0, 0, 0, ]])

        elif self.el_type == "Barra":
            self.ke = (self.ae/self.l) * np.array([[self.m * self.m, self.m * self.n, -self.m * self.m, -self.m * self.n, 0, 0],
                                              [self.m * self.n, self.n * self.n, -self.m * self.n, -self.n * self.n, 0, 0],
                                              [-self.m * self.m, -self.m * self.n, self.m * self.m, self.m * self.n, 0, 0],
                                              [-self.m * self.n, -self.n * self.n, self.m * self.n, self.n * self.n, 0, 0],
                                              [0, 0, 0, 0, 0, 0],
                                              [0, 0, 0, 0, 0, 0, ]])

        elif self.el_type == "Viga":
            self.ke = np.array([[self.phi * self.n * self.n, -self.phi * self.m * self.n, self.lmbda * self.n, -self.phi * self.n * self.n,  self.phi * self.m * self.n,  -self.lmbda * self.n],
                           [-self.phi * self.m * self.n, self.phi * self.m * self.m, self.lmbda * self.m, self.phi * self.m * self.n,   -self.phi * self.m * self.m, self.lmbda * self.m],
                           [-self.lmbda * self.n,        self.lmbda * self.m,        2 * self.rho,        self.lmbda * self.n,          -self.lmbda * self.m,        self.rho],
                           [-self.phi * self.n * self.n, self.phi * self.m * self.n, self.lmbda * self.n, self.phi * self.n * self.n,   -self.phi * self.m * self.n, self.lmbda * self.n],
                           [self.phi * self.m * self.n, -self.phi * self.m * self.m, -self.lmbda * self.m, -self.phi * self.m * self.n, self.phi * self.m * self.m,  -self.lmbda * self.m],
                           [-self.lmbda * self.n,        self.lmbda * self.m,        self.rho,            self.lmbda * self.n,          -self.lmbda * self.m,        2 * self.rho]])

        elif self.el_type == "Portico":
            self.ke = (self.ae / self.l) * np.array([[self.m * self.m, self.m * self.n, 0, -self.m * self.m, -self.m * self.n, 0],
                                      [self.m * self.n, self.n * self.n, 0, -self.m * self.n, -self.n * self.n, 0],
                                      [0, 0, 0, 0, 0, 0],
                                      [-self.m * self.m, -self.m * self.n, 0, self.m * self.m, self.m * self.n, 0],
                                      [-self.m * self.n, -self.n * self.n, 0, self.m * self.n, self.n * self.n, 0],
                                      [0, 0, 0, 0, 0, 0, ]])

            self.ke = self.ke + np.array([[self.phi * self.n * self.n, -self.phi * self.m * self.n, self.lmbda * self.n, -self.phi * self.n * self.n, self.phi * self.m * self.n, -self.lmbda * self.n],
                                [-self.phi * self.m * self.n, self.phi * self.m * self.m, self.lmbda * self.m, self.phi * self.m * self.n, -self.phi * self.m * self.m, self.lmbda * self.m],
                                [-self.lmbda * self.n, self.lmbda * self.m, 2 * self.rho, self.lmbda * self.n, -self.lmbda * self.m, self.rho],
                                [-self.phi * self.n * self.n, self.phi * self.m * self.n, self.lmbda * self.n, self.phi * self.n * self.n, -self.phi * self.m * self.n, self.lmbda * self.n],
                                [self.phi * self.m * self.n, -self.phi * self.m * self.m, -self.lmbda * self.n, -self.phi * self.m * self.n, self.phi * self.m * self.m, -self.lmbda * self.m],
                                [-self.lmbda * self.n, self.lmbda * self.m, self.rho, self.lmbda * self.n, -self.lmbda * self.m, 2 * self.rho]])
        print(self.ke)
        return np.round(self.ke, decimals=4)

