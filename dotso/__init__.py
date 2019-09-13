import os
import ctypes

dirname = os.path.dirname(__file__)
dotsodir = os.path.join(dirname, '.so')
dotso_hello_world = os.path.join(dotsodir, 'hello_world.so')

so = ctypes.cdll.LoadLibrary
hello_world = so(dotso_hello_world)
hello_world.restype = ctypes.c_char_p
