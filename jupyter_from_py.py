"""Create a notebook containing code from a script.

Run as:  python jupyter_from_py.py my_script.py
"""
import sys

import nbformat
from nbformat.v4 import new_notebook, new_code_cell

nb = new_notebook()

try:
    with open(sys.argv[1]) as f:
        code = f.read()
except:
    print('> ERROR')
    print('> USAGE: python jupyter_from_py.py my_script.py')
    print('> You did not provide a python script, or it could not be read.')
    quit()

nb.cells.append(new_code_cell(code))
nbformat.write(nb, sys.argv[1]+'.ipynb')
