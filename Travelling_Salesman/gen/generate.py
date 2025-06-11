# File: generate.py
# Author: Jackson Madsen

# Description: Graph generator for Traveling Saleman/Hamiltonian Path problem solver
# Use: python3 genereate.py -n n -f f -w w > filename.lp
#	where: n is the number of nodes in the graph
#	       f is a connecting factor for the graph generation from 0 to 1,
#		0 will produce a spanning tree, 1 will produce a completely connected graph
#	       w is the maximum weight of an edge in the graph, inclusive
#	       filename.lp is the file to write the instance to
#	Each of n, f, w can be omitted (Default n=4, f=0.5, w=10)
#	The redirect (> filename.lp) can be omitted (to write to stdout)


import random
import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('-n', default = 4, type = int,
			help = "The number of nodes to include in the graph. (Default = 4)")

parser.add_argument('-f', default = 0.5, type = float,
			help = '''Connecting factor for the graph generation from 0-1.
				0 makes a spanning tree, 1 creates a completely connected graph (Default 0.5)''')

parser.add_argument('-w', default = 10, type = int,
			help = "Maximum weight of an edge in the graph, inclusive. (Default = 10)")

args = parser.parse_args()

numNodes = args.n
connectFactor = args.f
maxWeight = args.w

# List all the nodes
printStr = "node("
for i in range(numNodes):
  printStr += f"{i} ; "

print("% Individual Nodes for the graph")
print(f"{printStr[:-2]}).\n")

# Create a n x n matrix filled with zeros. 0 will represent blanks and 1 will represent an edge at that coordinate
matrix = [[0 for _ in range(numNodes)] for _ in range(numNodes)]

# Converts which square of the matrix we are looking at into row and col
def coordFinder(square, size):
  row = square // size
  col = square % size
  return (row, col)

def matrixSum(matrix):
  return sum(map(sum,matrix))

def nodeDegree(matrix, node):
  # We do not need to subtract matrix[node][node] because that value is always 0 since we are avoiding self-loops
  total = sum(matrix[node])
  for col in matrix:
    total += col[node]

  return total

# Based on Dirac's Theorem on Hamiltonian Cycles, the minimum connections each edge must have is n / 2
minDegree = math.ceil(numNodes / 2)

for index, col in enumerate(matrix):
  while nodeDegree(matrix, index) < minDegree:
    randNode = random.randint(0,numNodes-1)
    while randNode == index or matrix[randNode][index] != 0:
      randNode = random.randint(0,numNodes-1)

    col[randNode] = 1

maxEdges = connectFactor * ((numNodes**2) - numNodes) / 2

# Start adding random edges if needed
while matrixSum(matrix) < maxEdges:
  randSquare = random.randint(0, (numNodes**2) - 1)
  row, col = coordFinder(randSquare, numNodes)
  while row == col or matrix[col][row] != 0 or matrix[row][col] != 0:
    randSquare = random.randint(0, (numNodes**2) - 1)
    row, col = coordFinder(randSquare, numNodes)

  matrix[col][row] = 1

# Iterate through the matrix and print out the edges
print("% Edges of the Graph")
for cIndex, col in enumerate(matrix):
  for rIndex, row in enumerate(col):
    if row == 1:
      print(f"edge({cIndex}, {rIndex}, {random.randint(1,maxWeight)}).")

