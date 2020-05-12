from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 100
data = np.full(n, rank, int)
buff = np.empty(n, int)
data[:] = rank

# ALT 1:
for i in range(0,size):
    if (rank == i and i < size-1):
        comm.Send(data, dest=i+1)
        print("Rank {}: Sent {} items".format(rank,n))
    if (rank == i and i > 0):
        comm.Recv(buff, source=i-1)
        print("Rank {}: Buff[0] = {}".format(rank,buff[0]))

# ALT 2:
target = rank + 1
src = rank - 1
if target >= size:
    target = MPI.PROC_NULL
if src < 0:
    src = MPI.PROC_NULL

comm.Sendrecv(data, dest=target, recvbuf=buff, source=src)
if (rank < size-1):
    print("Rank {}: Sent {} items".format(rank,n))
if (rank > 0):
    print("Rank {}: Buff[0] = {}".format(rank,buff[0]))
