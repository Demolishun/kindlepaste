# setup.py
from distutils.core import setup
import py2exe
from glob import glob

excludes = []
dll_excludes = ['msvcp90.dll']
includes = []
packages = []

opts = { 
    "py2exe": { 
        "includes":includes, 
        "excludes":excludes,
        "dll_excludes":dll_excludes,
        "packages":packages,
        "bundle_files": 2,
        "compressed": 1, # compress the library archive

    } 
}       
setup(windows=["guikindlepaste.py"], options=opts)
