"""Module: grids
This module contains contains the definition of a grid class and its associated methods.
 The grid class models a grid of blocks, where each blocl can either be occupied or vacant 
 """
class Grid:
    """A class showing a sqaure grid of blocks. where each block can either be occupied or vacant

Methods used:
- _n(int): the size of the grid (n x n)
- _occupanices(list): the list of tupules representing coordinates of occupied blocks
- _rows(list of lists): the 2d list that represents the grid, where True means a block is occupied and False mean a block is not
- __repr__(): Returns a string representation of the Grid object to recreate it.
- __str__(): Returns a string representation of the grid for easy display.
- get_occupancies(): Returns a copy of the list of occupied coordinates.
- get_row(i): Returns a copy of the i-th row.
- add_occupancy(coords): Adds an occupancy at the specified coordinates.
- del_occupancy(coords): Removes an occupancy at the specified coordinates.
- copy(): Returns a copy of the Grid object.
- v_reflected(): Returns a new Grid object with a vertical reflection of the current grid.
- h_reflected(): Returns a new Grid object with a horizontal reflection of the current grid.
- rotated(): Returns a new Grid object with a clockwise rotation.
- __add__(h): Returns a new Grid object representing the union of two grids.
- __eq__(h): Checks if the current grid is equal to another grid.
- __le__(h): Checks if the current grid is less than or equal to another grid.
- __ge__(h): Checks if the current grid is greater than or equal to another grid.
 """
    def __init__(self, n, occupancies):
        self._n = n
        self._occupancies = occupancies
        self._rows = [[False]*self._n for _ in range(self._n)]
        for row, col in self._occupancies:
            self._rows[row][col] = True

##q1
    def __repr__(self):
        return f"Grid(n ={self._n}, occupancies ={self._occupancies})"
    
 #q2
    def __str__(self):
        grid = ""
        for row in self._rows:
            for block in row:
                if block == True:
                    grid += "■ "
                else:
                    grid += "□ "
            grid += "\n"
        return grid

 #q3
    def get_occupancies(self):
        return self._occupancies.copy()
    
#q4
    def get_row(self, i):
        return self._rows[i].copy()
    
#q5
    def add_occupancy(self, coords):
        location = self._rows[coords[0]][coords[1]]
        if location == False:
            self._rows[coords[0]][coords[1]] = True
            self._occupancies.append(coords)
        return self
    
#q6
    def del_occupancy(self, coords):
        location = self._rows[coords[0]][coords[1]]
        if location == True:
            self._rows[coords[0]][coords[1]] = False
            self._occupancies.remove(coords)
        return self

#q7 
    def copy(self):
        return Grid(self._n, self._occupancies.copy())
    
 #q8
    def v_reflected(self):
        rows2 = [None] * len(self._rows)
        for i in range(0, len(self._rows)):
            rows2[i] = self._rows[i]
        for row in rows2:
            row.reverse()

        reversedOccupancies = [] 
        for i in range(len(rows2)):
            for j in range(len(rows2[i])):
                if rows2[i][j] == True:
                    reversedOccupancies.append((i, j))

        return Grid(len(rows2), reversedOccupancies)

#q9
    def h_reflected(self):
        rows2 = [None] * len(self._rows)
        for i in range(0, len(self._rows)):
            rows2[i] = self._rows[i]
        rows2.reverse()

        reversedOccupancies = [] 
        for i in range(len(rows2)):
            for j in range(len(rows2[i])):
                if rows2[i][j] == True:
                    reversedOccupancies.append((i, j))

        return Grid(len(rows2), reversedOccupancies)

 #q10
    def rotated(self):
        newoccupancies = []

        for row, col in self._occupancies:
            r = col
            c = self._n - 1 -row
            newoccupancies.append((r, c))
        return Grid(self._n, newoccupancies)
    
#q11
    def __add__(self, h):
        newOccupancies = [] 
        for i in range(len(self._rows)):
            for j in range(len(self._rows[i])):
                if self._rows[i][j] != h._rows[i][j]:
                    newOccupancies.append((i, j))
        print(newOccupancies)
        return Grid(len(self._rows), newOccupancies)
    
#q12
    def __eq__(self, h):
        if self._n != h._n:
            return False
        if self._rows == h._rows:
            return True
        else: 
            return False
#q13
    def__le__(self, h):
        if self._n != h._n:
            return False
        for row in range(self._n):
            for col in range(self._n):
                if self._rows[row][col] and not h._rows[row][col]:
                    return False
        return True 
#q14
    def__ge__(self, h):
        if self._n != h._n:
            return False
        for row in range(self._n):
            for col in range(seld._n):
                if h._rows[row][col] and not self._rows[row][col]:
                    return False
        return True         

#q15
    if __name__ == "__main__"
    x = Grid(3, [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2)])

    print(x)
    print(x.vertical_reflection())
    print(x.rotate_clockwise())



