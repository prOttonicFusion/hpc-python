import timeit

N = 20

tpython = timeit.timeit(stmt='fibonacci(30)',
              setup='from fib import fibonacci', number=N)

tcython = timeit.timeit(stmt='fibonacci(30)',
              setup='from cyt_fib import fibonacci', number=N)

print('Mean wall-times:')
print(' Python: ', tpython/N)
print(' Cython: ', tcython/N)