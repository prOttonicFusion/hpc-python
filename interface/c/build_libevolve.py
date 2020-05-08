from cffi import FFI
ffibuilder = FFI()

# List all functions that we want to include
ffibuilder.cdef("""
    void evolve(double *u, double *u_previous, int nx, int ny, 
            double a, double dt, double dx2, double dy2);  
                """)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_libevolve",
"""
         void evolve(double *u, double *u_previous, int nx, int ny,
                     double a, double dt, double dx2, double dy2);
""",
    sources=['evolve.c'],   
    extra_compile_args=['-O3'],
    library_dirs=['.'],
    # libraries=['evolve'],
)
ffibuilder.compile(verbose=True)
