# File: generate.py
# Author: Jackson Madsen

# Description: Set generator for Bin Packing problem solver
# Use: python3 generate.py -n n -w w > filename.lp
#	where: n is the number of items to generate
#	       w is the maximum weight of an item
#	       filename.lp is the location to save the instance file to
#	Each of n and w can be omitted (Defaults n=10, w=5)
#	The redirect (> filename.lp) can be omitted (to print to stdout)


import random
import argparse

# Process Arguments
parser = argparse.ArgumentParser()

parser.add_argument('-n', default = 10, type = int,
			help = "The number of items to generate. (Default = 10)")

parser.add_argument('-w', default = 5, type = int,
			help = "The maximum weight of an item, non-inclusive. (Default = 5)")

args = parser.parse_args()

print("% Possible items")
# Print all possible items
print(f"item(1..{args.n}).")
print()

print("% Item definitions\n% item(number, cost).")
# Assign weights to each individual item
for i in range(1, args.n + 1):
  print(f"item({i}, {random.randint(1,args.w)}).")
