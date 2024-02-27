from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
from CellClass import Cell, Sum
import time


def GetGrid(s, driver):
    url = 'https://sumplete.com/'
    if s is None:
        url = 'https://sumplete.com/master/'

    driver.get(url)
    if s is not None:
        dropdown = Select(driver.find_element(By.ID, "size"))
        dropdown.select_by_value(str(s))

        if s > 5:
            dropdown = Select(driver.find_element(By.ID, "level"))
            options = dropdown.options
            last_option_index = len(options) - 1
            dropdown.select_by_index(last_option_index)

        new_puzzle_button = driver.find_element(By.ID, "new")
        new_puzzle_button.click()
        time.sleep(1)

    grid = driver.find_element(By.ID, 'grid')
    cells = grid.find_elements(By.CLASS_NAME, 'cell')
    cell_data = [cell.text for cell in cells]

    s = int(math.sqrt(len(cell_data)))
    if s ** 2 != len(cell_data):
        raise ValueError("Sumplete grid is not square")

    print(f"Solving: {s - 1}x{s - 1}")

    numbers = []
    game = []

    for index, value in enumerate(cell_data[:-1]):
        if ((index + 1) % s == 0) or (index + 1 > s*(s-1)):
            game.append(Sum(int(value)))
        else:
            numbers.append(Cell(int(value), int(index)))

    s = s - 1
    for i in range(s):
        game[i].addList(numbers[(s*i):((s*i)+s)])

    for i in range(s):
        game[i + (s)].addList([numbers[(j*s)+i] for j in range(s)])

    print("grid loaded")
    return game
