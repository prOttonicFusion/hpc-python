## Interfacing with Fortran

The file [evolve.f90](evolve.f90) contain a pure Fortran implementation of the
single time step in heat equation. Use **f2py** for creating Python interface,
and use the Fortran function instead the Python function in
(heat.py)[heat.py].
You may need to insert `f2py` attributes into the Fortran file.

### Solution

1. Run `f2py3 -c evolve.f90 -m fortran_evolve_module`
2. Run `python3 heat_main.py`