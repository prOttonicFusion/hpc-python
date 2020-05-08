import timeit

N = 3

tpython = timeit.timeit(stmt='main("bottle.dat",0.5,  0.01, 0.01, 200, 4000)',
              setup='from heat_main import main', number=N)

tcython = timeit.timeit(stmt='main("bottle.dat",0.5,  0.01, 0.01, 200, 4000)',
              setup='from heat_main_cython import main', number=N)

print('Mean wall-times:')
print(' Python: ', tpython/N)
print(' Cython: ', tcython/N)