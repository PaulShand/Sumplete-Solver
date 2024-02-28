
# Sumplete-Solver

I've developed an advanced strategy to efficiently solve Sumplete puzzles, leveraging constraint satisfaction techniques. This innovative approach ensures the solving of puzzles at the highest difficulty level in under 3 seconds. The primary goal is to offer an optimized solution framework that serves as a valuable tool for enthusiasts and researchers in computational puzzle solving.

## Utilization

The solution utilizes the `selenium.webdriver` to automatically open a browser and load a customized game of Sumplete based on the command prompt instructions. It then solves the puzzle using either constraint satisfaction algorithms or a method that mimics human solving strategies.

The command syntax is as follows:

```
Solver.py [-h] [-S {3,4,5,6,7,8,9}] [-M {H,C}]
```

- `-S` sets the size of the puzzle. If omitted, the solver defaults to solving the daily 7x7 puzzle.
- `-M` selects the solving method: `H` for human-like or `C` for constraint-based solving. Note: The constraint method cannot solve expert-level puzzles of size 7x7 and above due to the complex guessing challenges at that level.

## Result

Upon execution, a web browser page will open displaying the solved puzzle. The page remains open for review until you press return, which closes the browser and terminates the program.

## How It Works

The solver operates by interpreting command prompt instructions to navigate to the puzzle website and gather necessary data using `GridMaker`, which returns a list of all required sums along with their associated cells that form each group. Depending on the selected method, the solver then iterates through a series of logical steps, marking cells with crosses and circles until all cells are filled and the puzzle is solved.
