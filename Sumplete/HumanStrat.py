import itertools
from CellClass import Cell, Sum, CellState
from copy import deepcopy

def possible(arr, goal):
    combinations_sums = []
    for r in range(1, len(arr) + 1):
        for combination in itertools.combinations(arr, r):
            combinations_sums.append(sum(combination))
    if goal in combinations_sums:
        return True
    else:
        return False

def Madness(game, circle, answer):
    flag = 0
    while flag < 4:
        for S in game:
            S.update()
            for num in S.numbers:
                if num.select is CellState.blank:
                    goal = S.goal - num.number
                    arr = S.form().copy()
                    arr.remove(num.number)
                    if not possible(arr, goal) and goal != 0:
                        flag = 0
                        num.Cross()
                        answer.append(num.pos)

                    if not possible(arr, S.goal) and S.goal != 0:
                        flag = 0
                        num.Circle()
                        circle.append(num.pos)
            S.update()
            if S.Check():
                return False, game, circle, answer

        flag += 1

    if (len(game)/2)*(len(game)/2) != (len(answer)+len(circle)):
        blank_list = []
        for S in game[:int(len(game)/2)]:
            for num in S.numbers:
                if num.select is CellState.blank:
                    blank_list.append(num)
        for num in blank_list:
            newG = deepcopy(game)
            newC = deepcopy(circle)
            newA = deepcopy(answer)
            
            corresponding_num = next((cell for sum_group in newG for cell in sum_group.numbers if cell.pos == num.pos), None)
            
            if corresponding_num:
                corresponding_num.Cross()
                newA.append(corresponding_num.pos)
                done, newG, newC, newA = Madness(newG, newC, newA)
                
                if done:
                    return True, newG, newC, newA
                else:
                    corresponding_num.UnCross()
                    newA.remove(corresponding_num.pos)

        return False, newG, newC, newA

    else:
        return True, game, circle, answer
