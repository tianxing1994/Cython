import os
import pyximport


dirname = os.path.dirname(__file__)
build_dir = os.path.join(dirname, ".pyxbld")

pyximport.install(build_dir=build_dir, language_level=2)
from cython_support import hello_world