# File: generate.py
# Author: Jackson Madsen

# Description: Set generator for Bin Packing problem solver
# Use: python3 generate.py -n n -k k > filename.lp


import random
import argparse

# Process Arguments
parser = argparse.ArgumentParser()

parser.add_argument('-n', default = 10, type = int,
			help = "The number of items to generate. (Default = 10)")

parser.add_argument('-w', default = 5, type = int,
			help = "The maximum weight that an item can weigh, non-inclusive. (Default = 5)")

args = parser.parse_args()

# Print all possible items
print(f"item(1..{args.n}).")

# Assign weights to each individual item
for i in range(1, args.n + 1):
  print(f"item({i}, {random.randint(1,args.w)}).")
