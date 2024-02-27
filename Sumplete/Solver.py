from HumanStrat import Madness
from GridMaker import GetGrid
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Constraint import Constraint
import argparse

parser = argparse.ArgumentParser(description='Welcome to the Sumplete Solver! \n If given no argument it solves the daily 7x7')
parser.add_argument('-S', '--size', type=int, choices=range(3, 10), help='The size of the puzzle')
parser.add_argument('-M', '--method', type=str, choices=['H', 'C'], help='The method to solve the puzzle')

args = parser.parse_args()

print(f"Puzzle Size: {args.size}")
print(f"Solve Method: {args.method}")

s = args.size
m = args.method

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

game = GetGrid(s, driver)

answer = []
circle = []

if m in ("H", None):
    done, game, circle, answer = Madness(game, circle, answer)

if m == "C":
    circle, answer = Constraint(game, circle, answer)

tiles_to_click = driver.find_elements(By.CLASS_NAME, 'cell')
current = 0
for tile in tiles_to_click:
    if current in answer:
        driver.execute_script("arguments[0].scrollIntoView(true);", tile)
        tile.click()
    current += 1

current = 0
for tile in tiles_to_click:
    if current in circle:
        driver.execute_script("arguments[0].scrollIntoView(true);", tile)
        tile.click()
        tile.click()
    current += 1

print("Puzzle Solved! press a key to continue")
input()
print("Program Finished.")

driver.quit()