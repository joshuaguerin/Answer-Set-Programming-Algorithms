# File: generate.py
# Author: Jackson Madsen

# Description: Set generator for Bin Packing problem solver
# Use: python3 generate.py -n n -w w > filename.lp
#	where: n is the number of cells to remove
#	n can be omitted (Defaults n=10)
#	The redirect (> filename.lp) can be omitted (to print to stdout)

import random
import argparse

# Process Arguments
parser = argparse.ArgumentParser()

parser.add_argument('-n', default = 18, type = int,
			help = "The number of items to generate. (Default = 18)")

args = parser.parse_args()

toRemove = args.n

def isValid(board, row, col, num):
  # Check Rows and Cols
  for i in range(9):
    if board[row][i] == num or board[i][col] == num:
      return False

  # Check grids
  startRow = 3 * (row // 3)
  startCol = 3 * (col // 3)
  for i in range(3):
    for j in range(3):
      if board[startRow + i][startCol + j] == num:
        return False

  return True

def dfsSudoku(board):
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0:
        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
          if isValid(board, row, col, num):
            board[row][col] = num
            if dfsSudoku(board):
              return True
            board[row][col] = 0

        return False
  return True

board = [[0 for _ in range(9)] for _ in range(9)]
dfsSudoku(board)

for _ in range(toRemove):
  randRow = random.randint(0,8)
  randCol = random.randint(0,8)
  while board[randRow][randCol] == 0:
    randRow = random.randint(0,8)
    randCol = random.randint(0,8)

  board[randRow][randCol] = 0

print("% sudoku(row, col, num) where row, col are 1-indexed")
for row in range(len(board)):
  printed = False
  for col in range(len(board[row])):
    if board[row][col] != 0:
      print(f"sudoku({row + 1}, {col + 1}, {board[row][col]}).", end = " ")
      printed = True
  if printed:
    print()

