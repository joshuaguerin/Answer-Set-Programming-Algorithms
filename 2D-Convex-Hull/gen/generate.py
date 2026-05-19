#!/usr/bin/env python3


import random
import argparse
import math
import copy
parser = argparse.ArgumentParser()

parser.add_argument(
    "-n",
    default=4,
    type=int,
    help="The number of points to include in the graph. (Default = 8)",
)

parser.add_argument("-p", default="0", type=float, help="Use positive values only (0/1)")

parser.add_argument("-d", default=10, type=int, help="Maximum distance from origin ")

args = parser.parse_args()


numPoints = args.n
onlyPositive = args.p
maxDistance = args.d


numericRanges = range(0,maxDistance +1, 1) if onlyPositive == "0" else range(-maxDistance, maxDistance+ 1, 1)

lines = []

for iter in range(numPoints):
    aVal = random.choice(numericRanges)
    bVal = random.choice(numericRanges)
        
    new_line = f"point ({aVal}, {bVal} )."
    lines.append(new_line)


output_filename = "instance.lp"

for line in lines:
    print(f"{line} \n")

with open(output_filename, "w") as file:
    for line in lines:
        file.write(f"{line} \n")




