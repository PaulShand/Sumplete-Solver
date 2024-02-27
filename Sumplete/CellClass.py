from enum import Enum
import random
from typing import List
import itertools

class CellState(Enum):
    blank = 1
    cross = 2
    circle = 3

class Cell:
    def __init__(self, number: int, pos: int):
        self.number = number
        self.pos = pos
        self.select = CellState.blank
    
    def __hash__(self):
        return hash((self.number, self.pos))

    def __eq__(self, other):
        return (self.number, self.pos) == (other.number, other.pos)

    def __str__(self):
        return str(self.number)

    def Cross(self):
        self.select = CellState.cross
    
    def UnCross(self):
        self.select = CellState.blank

    def Circle(self):
        self.select = CellState.circle

class Sum:
    def __init__(self, goal: int):
        self.goal = goal
        self.numbers = []

    def addList(self, numbers: List[Cell]):
        self.numbers = numbers

    def form(self):
        return [i.number for i in self.numbers if i.select is not CellState.cross]

    def __print__(self):
        out = [str(self.goal)]
        for i in self.numbers:
            out.append(i.number)
        print(out)
    
    def update(self):
        for x in self.numbers:
            if x.select is CellState.cross:
                self.numbers.remove(x)
            elif x.select is CellState.circle:
                self.goal -= x.number
                self.numbers.remove(x)

    def Check(self):
        arr = [x.number for x in self.numbers if x.select in (CellState.blank, CellState.circle)]

        combinations_sums = [sum(combination) for r in range(1, len(arr) + 1) for combination in itertools.combinations(arr, r)]

        if self.goal in combinations_sums or self.goal == 0:
            return False
        else:
            return True
        

def test_game():
    BIGLIST = []
    reference = []
    for i in range(9):
        num = random.randint(1, 10)
        reference.append(num)
        BIGLIST.append(Cell(num, i))  # Fixed: Use Cell instead of cell

    game = [Sum(11), Sum(22), Sum(33)]

    print("Reference numbers:", reference)

    game[0].addList(BIGLIST[:3])
    game[1].addList([BIGLIST[0], BIGLIST[3], BIGLIST[6]])

    print("Initial form for game[0]:", game[0].form())
    print("Initial form for game[1]:", game[1].form())

    BIGLIST[0].Cross()

    print("Form for game[0] after crossing first cell:", game[0].form())
    print("Form for game[1] after crossing first cell:", game[1].form())

if __name__ == "__main__":
    test_game()