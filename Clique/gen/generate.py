# File: generate.py
# Author: Jackson Madsen

# Description: Graph generator for clique problem solver
# Use: python3 genereate.py -n num -k num > filename.lp
#      python3 generate.py -n num > filename.lp
#      python3 generate.py -k num > filename.lp
#      python3 generate.py > filename.lp

import argparse
from random import randint

# Process arguments
parser = argparse.ArgumentParser()

parser.add_argument('-n', default = 10, type = int, 
			help = "Upper limit on number of nodes, non-inclusive. (Default = 10)")
parser.add_argument('-k', default = 3, type = int,
			help = "The clique size that is guaranteed to be found in the graph (Default = 3)")
args = parser.parse_args()

numNodes = args.n
cliqueSize = args.k

# Generate all possible nodes
print("node(", sep = "", end = "")
for x in range(1, numNodes):
  print(x, " ; ", sep = "", end = "")
print(numNodes, ").", sep ="")

# Collect arbitrary nodes that will form the clique
connected = set()
while len(connected) < cliqueSize:
  index = randint(1, numNodes)
  connected.add(index)

connected = list(connected)

# Generate edges, with some random additional edges thrown in as well
for i in range(len(connected)-1):
  currNode = connected[i]
  nextNode = connected[i+1]

  print(f"edge({currNode}, {nextNode}", sep = "", end = "")

  # Add a random number of additional nodes, up to the maxNumber of nodes
  # Keeps track of seen nodes to make sure no duplicates
  '''
  seen = set()
  for _ in range(randint(0, numNodes)):
    randNode = randint(0, numNodes)
    if randNode not in seen and randNode != currNode and randNode != nextNode:
      seen.add(randNode)
      print(f" ; {randNode}", sep = "", end = "")
  '''
  print(").")

print(f"edge({connected[-1]}, {connected[0]}).", sep = "")
















