from CellClass import Cell, Sum, CellState
from itertools import combinations

def PC(Sum):
    n = len(Sum.numbers)
    result = []

    elements = [i for i in Sum.numbers if i.select != CellState.cross]
    must = {i for i in Sum.numbers if i.select == CellState.circle}
    for r in range(n + 1):
        for combo in combinations(elements, r):
            combo_set = set(combo)
            if must.issubset(combo_set) and sum(i.number for i in combo) == Sum.goal:
                result.append([i for i in (combo)])

    return result

def find_intersection(lists):

    intersection_set = set(lists[0])
    for lst in lists[1:]:
        intersection_set &= set(lst)

    intersection_list = list(intersection_set)
    return intersection_list

def find_union(lists, sets):

    union = set(lists[0])

    for lst in lists[1:]:
        union |= set(lst)

    union = sets - union
    union = list(union)
    return union


def Constraint(game, circle, answer):
    for x in range(100):
        C = []
        for i in game:
            C.append(PC(i))
        for i in range(len(C)):
            for j in find_intersection(C[i]):
                if j.select != CellState.circle:
                    j.select = CellState.circle
                    circle.append(j.pos)

            for j in find_union(C[i], set([x for x in game[i].numbers if x.select != CellState.cross])):
                answer.append(j.pos)
                j.select = CellState.cross
    

    return circle, answer