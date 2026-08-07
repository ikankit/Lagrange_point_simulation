import numpy as np

def lagrange_velocity(position, omega):
   

    x, y, z = position

    vx = -omega * y
    vy =  omega * x
    vz = 0.0

    return np.array([vx, vy, vz], dtype=float)