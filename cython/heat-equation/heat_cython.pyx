cimport cython
import numpy as np
cimport numpy as cnp    # Import for NumPY C-API
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
@cython.profile(True)
cdef void evolve(cnp.ndarray[cnp.double_t, ndim=2] u, 
            cnp.ndarray[cnp.double_t, ndim=2] u_previous,		
            double a, double dt, double dx2, double dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    cdef int n = u.shape[0]
    cdef int m = u.shape[1]
    cdef int i, j

    # Replace division with multiplication
    cdef double dx2i = 1.0 / dx2
    cdef double dy2i = 1.0 / dy2

    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) * dx2i + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
                 u_previous[i, j-1]) * dy2i )
    for i in range(0,n):
        for j in range(0,m):
            u_previous[i,j] = u[i,j]

cpdef iterate(cnp.ndarray[cnp.double_t, ndim=2] field, 
            cnp.ndarray[cnp.double_t, ndim=2] field0, 
            double a, double dx, double dy, 
            int timesteps, int image_interval):
    """Run fixed number of time steps of heat equation"""

    cdef double dx2 = dx**2
    cdef double dy2 = dy**2
    cdef int m

    # For stability, this is the largest interval possible
    # for the size of the time-step:
    cdef double dt = dx2*dy2 / ( 2*a*(dx2+dy2) )    

    for m in range(1, timesteps+1):
        evolve(field, field0, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)

cpdef init_fields(filename):
    # Read the initial temperature field from file
    cdef cnp.ndarray[cnp.double_t, ndim=2] field = np.loadtxt(filename)
    cdef cnp.ndarray[cnp.double_t, ndim=2] field0 = field.copy() # Array for field of previous time step
    return field, field0

def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))


