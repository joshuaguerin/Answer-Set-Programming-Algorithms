# File: generate.py
# Author: Jackson Madsen

# Description: Graph generator for clique problem solver
# Use: python3 genereate.py -n n > filename.lp
#	where: n is the number of nodes in the graph
#	       filename.lp is the file to write the instance to
#	n can be omitted (Default = 10)
#	The redirect (> filename.lp) can be omitted (to write to stdout)


import random
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', default = 10, type = int,
			help = "The number of nodes to include in the graph. (Default = 10)")

args = parser.parse_args()

# List all the nodes

printStr = "node("
for i in range(args.n):
  printStr += f"{i} ; "

print(f"{printStr[:-2]}).")

# Make a list of the nodes and a list to keep track of what nodes are already connected
nodes = [x for x in range(args.n)]
seen = [set() for _ in range(args.n)]


for index, node in enumerate(nodes):
  connected = False
  printStr = f"edge({node} , "

  for _ in range(random.randint(0, args.n - 1)):
    randNode = random.randint(0, args.n - 1)
    if randNode not in seen[index]:
      connected = True
      seen[index].add(randNode)
      printStr += f"{randNode} ; "

  if connected:
    print(f"{printStr[:-2]}).")

