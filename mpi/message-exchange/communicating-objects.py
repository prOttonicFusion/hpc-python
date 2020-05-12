from mpi4py import MPI

comm = MPI.COMM_WORLD

size = comm.Get_size()
rank = comm.Get_rank()

dictionary = {'rank': rank}

if (rank == 0):
    msg = comm.recv(source=1)
    comm.send(dictionary, dest=1)  # Send pickled dictionary
elif (rank == 1):
    comm.send(dictionary, dest=0)
    msg = comm.recv(source=0)

print("Rank: %d, Received message: %i" % (rank, msg['rank']))
