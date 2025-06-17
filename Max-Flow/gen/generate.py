# File: generate.py
# Author: Jackson Madsen

# Description: Graph generator for Independent Set problem solver
# Use: python3 genereate.py -n n -f f -w w > filename.lp
#	where: n is the number of nodes in the graph
#	       f is a connecting factor for the graph generation from 0 to 1,
#		0 will produce a spanning tree, 1 will produce a completely connected graph
#	       w is the maximum weight of an edge in the graph, inclusive
#	       filename.lp is the file to write the instance to
#	Each of n, f, w can be omitted (Default n=5, f=0.5, w=10)
#	The redirect (> filename.lp) can be omitted (to write to stdout)


import random
import argparse
import sys

# While this implementation isn't particularly efficient for large (500+ node)
# graphs, the recursion limit below can be adjusted by the user if 1k+
# node generation is desired.
# sys.setrecursionlimit(10000)

parser = argparse.ArgumentParser()

parser.add_argument('-n', default = 5, type = int,
			help = "The number of nodes to include in the graph. (Default = 5)")

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

# Define and Print start stop
print("% Start stop for the graph")
start = random.randint(0,numNodes-1)
stop = random.randint(0, numNodes-1)
while start == stop:
  stop = random.randint(0,numNodes-1)

print(f"start({start}).")
print(f"terminal({stop}).\n")

# Partition how many nodes will be in each layer by Stars & Bars method
stars = ['*'] * (numNodes - 2) +['|'] * (numNodes - 2)
partition = []

random.shuffle(stars)

count = 0
for item in stars:
  if item == '*':
    count += 1
  elif item == '|' and count != 0:
    partition.append(count)
    count = 0

if count != 0:
  partition.append(count)

cols = [set() for _ in range(len(partition))]

def checkPrevious(node, matrix):
  for col in matrix:
    if node in col:
      return True

  return False

for index, col in enumerate(cols):
    while len(col) < partition[index]:
      randNode = random.randint(0, numNodes - 1)
      while randNode == start or randNode == stop or checkPrevious(randNode, cols):
        randNode = random.randint(0, numNodes - 1)

      col.add(randNode)

cols = [{start}] + cols + [{stop}]

print("% edge(start, end, capacity)")
for index, col in enumerate(cols):
  # Start of the list connects to all the nodes
  if index == 0:
    for node in cols[index+1]:
      print(f"edge({start}, {node}, {random.randint(1, maxWeight)}).")

  # Last Tier will connect to the sink node
  elif index <= len(cols) - 2:
    for node1 in col:
      for node2 in cols[index + 1]:
        print(f"edge({node1}, {node2}, {random.randint(1, maxWeight)}).")

  # End of the list will already have all the edges flowing into it, so we skip it
  elif index == len(cols) - 1:
    print()
  # Otherwise we can make random edges as desired
  else:
    for node in col:
      if random.random() < connectFactor:
        print(f"edge({node}, {random.choice(list(cols[index+1]))}, {random.randint(1, maxWeight)}).")
