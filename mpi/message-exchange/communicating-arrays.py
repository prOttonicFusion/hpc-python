from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

data = np.empty(100000, dtype=float)  # Data to be sent
buff = np.empty(100000, dtype=float)  # Receive buffer
data[:] = rank

if (rank == 0):
    comm.Recv(buff, source=1)
    comm.Send(data, dest=1)  # Send array (without pickling)
elif (rank == 1):
    comm.Send(data, dest=0)
    comm.Recv(buff, source=0)

print("Rank: %d, Array[0]: %i" % (rank, buff[0]))
