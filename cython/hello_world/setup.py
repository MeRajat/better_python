from  distutils.core import setup
 
from Cython.Build import cythonize 

setup(
        name = "hello world ",
        ext_modules = cythonize("hello.pyx"),
)


