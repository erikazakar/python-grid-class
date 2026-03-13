# python-grid-class

This project implements a Python class that models a square grid of blocks where each block can be occupied or vacant.

The class includes methods for:

- printing grid structures
- adding and removing occupancies
- copying grids
- vertical and horizontal reflections
- clockwise rotations
- grid comparisons
- logical grid addition

This project demonstrates object-oriented programming in Python.

## Example Output

Example grid:

□ ■ ■  
■ ■ □  
■ □ ■  

Vertical reflection:

■ □ ■  
■ ■ □  
□ ■ ■  

Clockwise rotation:

■ ■ □  
□ ■ □  
■ ■ □  
## Example Usage

```python
from grids import Grid

x = Grid(3, [(0,1),(0,2),(1,0),(1,1),(2,0),(2,2)])

print(x)

print(x.v_reflected())

print(x.rotated())
