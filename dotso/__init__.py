import os
import ctypes

dirname = os.path.dirname(__file__)
dotso_hello_world = os.path.join(dirname, 'hello_world.so')

so = ctypes.cdll.LoadLibrary
hello_world = so(dotso_hello_world)
