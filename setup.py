import numpy as np
from math import sqrt, pi
from matplotlib import path

# Calculate the area of a polygon
def poly_area(polytope):
    x = polytope[:,0]
    y = polytope[:,1]
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

# -----------------------------------------------------------------------------------
# Setup
# -----------------------------------------------------------------------------------

bnd = np.array([[0, 0], [4, 0], [4, 4], [0, 4]])
gran = 100
heighPar = 20
seedNum = 6
sigma = 1/2*sqrt(poly_area(bnd)/seedNum/pi)

seeds = 4*np.random.rand(seedNum,2)
x_range = np.linspace(np.amin(bnd[:,0]),np.amax(bnd[:,0]),gran)
y_range = np.linspace(np.amin(bnd[:,1]),np.amax(bnd[:,1]),gran)
X, Y = np.meshgrid(x_range,y_range)