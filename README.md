# jupyter-from-python
Here we solve the problem of going from python file to jupyter notebook, something that is very easy in the reverse.

## Use
```
python jupyter_from_py.py <your_script>.py
```
You should have a new file named `<your_script>.ipynb`.

## Example
To run an example of this script:
1. Run `python jupyter_from_py.py example.py` in a terminal, from this directory
1. You should now see a notebook titled example.ipynb

## Tips
If you are bounding back and forth between notebooks and python files, it's useful to set up these two aliases:
```
alias jupyter-to-py='ipython nbconvert --to=python'
alias jupyter-from-py='python <path_to_repo>/jupyter_from_py.py'
```

This way you can easily convert between both formats.
