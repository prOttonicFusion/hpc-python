import os
import numpy as np

def maxmem():
    # Check maximum memory from /proc/
    # Based on Python Cookbook
    # http://code.activestate.com/recipes/286222/
    # Works on most Linux systems but not in Mac OSX or Windows

    _scale = {'kB': 1024.0, 'mB': 1024.0 * 1024.0,
              'KB': 1024.0, 'MB': 1024.0 * 1024.0}

    _proc_status = '/proc/{0}/status'.format(os.getpid())
    with open(_proc_status) as f:
        v = f.read()

    # Find VmHWM value
    i = v.index('VmHWM:')
    v = v[i:].split(None, 3)
    return float(v[1]) * _scale[v[2]]

overhead = maxmem()

a = np.random.random((1024, 1024, 10))
b = np.random.random((1024, 1024, 10))
#c = a - b
#c = 3.0 * a - 5.6 * b
#c = 3.0 * a - 5.6 * b + np.cos(a) - np.sin(b)
c = 3.0 * a - 5.5 * b + (np.cos(a) - np.sin(b))
#c = (np.cos(a) - np.sin(b)) + 3.0 * a - 5.6 * b

maxMemoryUsage = maxmem() - overhead
print('Used at most {} bytes of memory'.format(maxMemoryUsage))