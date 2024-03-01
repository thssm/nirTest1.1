from ctypes import *
from sys import platform

add_lib = CDLL("./libmetascan.dll")
print("Successfully loaded ", add_lib)
print("Hello World!")
