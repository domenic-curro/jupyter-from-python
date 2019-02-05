"""Create a notebook containing code from a script.

Run as:  python jupyter_from_py.py my_script.py
"""
import sys

import nbformat
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell


CELL_TYPE_UNKNOWN = 0
CELL_TYPE_CODE = 1
CELL_TYPE_MARKDOWN = 2

IDENTIFIER_CODE = '# In[ ]:'
IDENTIFIER_MARKDOWN = '# ##'

def celltype_for_line(line):
    if IDENTIFIER_MARKDOWN in line:
        return CELL_TYPE_MARKDOWN
    elif IDENTIFIER_CODE in line:
        return CELL_TYPE_CODE
    else:
        return CELL_TYPE_UNKNOWN

if __name__ == '__main__':
    nb = new_notebook()

    try:
        # with open('example.py') as f:
        with open(sys.argv[1]) as f:
            code = f.read()
    except:
        print('> ERROR')
        print('> USAGE: python jupyter_from_py.py my_script.py')
        print('> You did not provide a python script, or it could not be read.')
        quit()

    lines = code.split('\n')
    lines_clean = []
    for line in lines:
        if not '# coding' in line and not '#!' in line:
            lines_clean += [line]
    lines = lines_clean

    cell_blocks = []

    current_cell_type = CELL_TYPE_CODE
    cell_lines = []

    # initial logic
    if celltype_for_line(lines[0]) == CELL_TYPE_UNKNOWN or celltype_for_line(line[0]) == CELL_TYPE_CODE:
        current_cell_type = CELL_TYPE_CODE
    else:
        current_cell_type = CELL_TYPE_MARKDOWN
    cell_lines += [lines[0]]

    # continuing logic
    for line in lines[1:]:
        is_same_cell = celltype_for_line(line) == CELL_TYPE_UNKNOWN

        if is_same_cell:
            # continue adding to the cell
            cell_lines += [line]
        else:
            # store the cell and start a new one
            cell_blocks += [(current_cell_type, cell_lines)]
            cell_lines = [line]
            current_cell_type = celltype_for_line(line)

    # closing logic (store the last cell)
    cell_blocks += [(current_cell_type, cell_lines)]

    for cell_type, code in cell_blocks:
        code = '\n'.join(code)

        is_cell_empty = len(code.strip()) == 0
        if is_cell_empty:
            continue

        if cell_type == CELL_TYPE_CODE:
            code = code.replace(IDENTIFIER_CODE, '')
            nb.cells.append(new_code_cell(code.strip()))
        elif cell_type == CELL_TYPE_MARKDOWN:
            code = code.replace(IDENTIFIER_MARKDOWN, '##')
            nb.cells.append(new_markdown_cell(code.strip()))
        else:
            assert False

    nbformat.write(nb, sys.argv[1].split('.py')[0] + '.ipynb')
    # nbformat.write(nb, 'example.py'.split('.py')[0] + '.ipynb')