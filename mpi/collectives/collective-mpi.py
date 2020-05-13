from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of MPI tasks has to be 4.'

if rank == 0:
    print('First collective:')

if rank == 0:
    data = numpy.arange(8)
else:
    data = numpy.empty(8, int)

comm.Bcast(data, root=0)
print('  Task {0}: {1}'.format(rank, data))


# Prepare data vectors ..
data = numpy.arange(8) + size*rank
# .. and receive buffers
buff = numpy.full(8, -1, int)

# ... wait for every rank to finish ...
comm.barrier()
if rank == 0:
    print('')
    print('-' * 32)
    print('')
    print('Data vectors:')
print('  Task {0}: {1}'.format(rank, data))
comm.barrier()
if rank == 0:
    print('')
    print('c)')

# Scatter elements from task 0 to the first 2 columns of the other 3
comm.Scatter(data, buff[:2], root=0)
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('d)')

# Gather the elements from the 2 first columns of each cpu to cpu 1
comm.Gather(data[:2], buff, root=1)
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('e)')

# Partial sums using two communicator objects
color = rank // 2
sub_comm = comm.Split(color)
sub_comm.Reduce(data, buff, op=MPI.SUM, root=0)
print('  Task {0}: {1}'.format(rank, buff))
