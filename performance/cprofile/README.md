## Using cProfile

In this exercise we analyze the performance of heat equation solver with cProfile.

The file [heat_main.py](heat_main.py) contains the (very inefficient)
implementation of the two dimensional heat equation. Use `cProfile` for
investigating where the time is spent in the program. Note that the execution 
time can be between 40 - 60 s depending on your hardware. (You can see also 
results of the simulation in the *heat_nnn.png* output files). 

### Solution:

We analyze the program usingn `cProfile` by executing
```
python3 -m cProfile -o profile.dat heat_main.py
```
which outputs the results to `profile.dat`. These results can then be anayzed using
```
python3 -m pstats profile.dat
```
Inside the interactive profile shell, we can then strip the full file paths, sort based on run time and show the 10 most time consuming functions
```
Welcome to the profile statistics browser.
profile.dat% strip
profile.dat% sort time
profile.dat% stats 10
Mon Apr 27 11:22:25 2020    profile.dat

         611984 function calls (602810 primitive calls) in 12.967 seconds

   Ordered by: internal time
   List reduced from 3447 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      200   12.319    0.062   12.319    0.062 heat.py:9(evolve)
        2    0.070    0.035    0.070    0.035 {built-in method matplotlib._png.write_png}
      277    0.040    0.000    0.040    0.000 {built-in method marshal.loads}
      685    0.027    0.000    0.027    0.000 {built-in method numpy.core.multiarray.dot}
     3203    0.019    0.000    0.019    0.000 {built-in method numpy.core.multiarray.array}
       25    0.017    0.001    0.020    0.001 {built-in method _imp.create_dynamic}
     2467    0.017    0.000    0.028    0.000 inspect.py:614(cleandoc)
1213/1119    0.016    0.000    0.050    0.000 {built-in method builtins.__build_class__}
        8    0.012    0.001    0.012    0.002 {built-in method matplotlib._image.resample}
    40000    0.010    0.000    0.012    0.000 npyio.py:742(floatconv)

```
We can clearly see that the `evolve()` function consumes by far the most time, over 12 seconds!