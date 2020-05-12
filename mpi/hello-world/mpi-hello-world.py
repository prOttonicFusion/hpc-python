from mpi4py import MPI

comm = MPI.COMM_WORLD   # Communicator object 

size = comm.Get_size()  # Number of CPUs
rank = comm.Get_rank()  # Rank of current CPU

print("Hello, World! From CPU %d out of %d" % (rank, size))
