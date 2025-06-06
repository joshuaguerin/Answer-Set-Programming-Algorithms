# File: generate.py
# Author: Jackson Madsen

# Description: Graph generator for vertex-cover problem solver
# Use: python3 genereate.py -n n -f f > filename.lp
#	where: n is the number of nodes in the graph
#	       f is a connecting factor for the graph generation from 0 to 1,
#		0 will produce a spanning tree, 1 will produce a completely connected graph
#	       filename.lp is the file to write the instance to
#	n can be omitted (Default = 10)
#	The redirect (> filename.lp) can be omitted (to write to stdout)


import random
import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('-n', default = 10, type = int,
			help = "The number of nodes to include in the graph. (Default = 10)")

parser.add_argument('-f', default = 0.5, type = float,
			help = '''Connecting factor for the graph generation from 0-1.
				0 makes a spanning tree, 1 creates a completely connected graph (Default 0.5)''')

args = parser.parse_args()

numNodes = args.n
connectFactor = args.f

# List all the nodes
printStr = "node("
for i in range(numNodes):
  printStr += f"{i} ; "

print("% Individual Nodes for the graph")
print(f"{printStr[:-2]}).\n")

# Create a n x n matrix filled with zeros. 0 will represent blanks and 1 will represent an edge at that coordinate
matrix = [[0 for _ in range(numNodes)] for _ in range(numNodes)]

def coordFinder(square, size):
  row = square // size
  col = square % size
  return (row, col)

def matrixSum(matrix):
    return sum(map(sum, matrix))

def dfsTreeGen(col, visited):
  visited[col] = True
  for row in range(numNodes):
    if not visited[row] and matrix[row][col] == 0:
      matrix[col][row] = 1
      dfsTreeGen(row, visited)

visited = [False] * numNodes
dfsTreeGen(0, visited)

maxEdges = (numNodes * (numNodes - 1)) / 2
numEdges = math.ceil(maxEdges * connectFactor)
print(numEdges)

while matrixSum(matrix) < numEdges:
  randSquare = random.randint(0, (numNodes**2) - 1)
  row, col = coordFinder(randSquare, numNodes)
  while row == col or matrix[col][row] != 0 or matrix[row][col] != 0:
    randSquare = random.randint(0, (numNodes**2) - 1)
    row, col = coordFinder(randSquare, numNodes)

  matrix[col][row] = 1

for i in range(len(matrix)):
    for j in range(len(matrix)):
      print(matrix[j][i], end="")
    print("")

