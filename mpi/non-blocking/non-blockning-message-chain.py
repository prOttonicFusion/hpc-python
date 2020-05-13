from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n = 100
data = np.full(n, rank, int)
buff = np.empty(n, int)
data[:] = rank

target = rank + 1
src = rank - 1
if rank == 0:
    src = MPI.PROC_NULL
if rank == size - 1:
    target = MPI.PROC_NULL

req = []
req.append(comm.Isend(data, dest=target))
req.append(comm.Irecv(buff, source=src))

MPI.Request.waitall(req)

if (rank < size-1):
    print("Rank {}: Sent {} items".format(rank,n))
if (rank > 0):
    print("Rank {}: Buff[0] = {}".format(rank,buff[0]))
