# File: generate.py
# Author: Jackson Madsen

# Description: Set generator for subset sum problem solver
# Use: python3 generate.py -v v -n n -w w > filename.lp
#	where: v is the upper limit on the value of the items, inclusive
#	       n is the the number of items to generate, inclusive
#	       w is the maximum weight of the items, non-inclusive
#	       filename.lp is the location to write the instance tfo
#	Each of v, n, w are optional (Defaults: v=10, n=25, w=10)
#	The redirect (> filename.lp) can be omitted (to print to stdout)

import random
import argparse

# Process arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', default=10, type=int,
                    help="Upper limit on the value of the items, inclusive. (Default: 10)")
parser.add_argument('-n', default=25, type=int,
                    help="Set the number of items to generate. (Default: 25)")
parser.add_argument('-w', default=10, type=int,
		    help="Set the maximum weight of the items, non-inclusive. (Default: 10)")
args = parser.parse_args()

maxVal = args.v
maxItems = args.n
maxWeight= args.w

# Here we use the stars and bars method to generate a random permutation
# The number of stars is equal to the number of items in the set
# The number of bars is equal to the upper limit on the value of the items
# When we shuffle, the list, we count the number of stars before encountering a bar,
# if there are none, then we have no items of that value. We start at value 1
stars = ['*'] * maxItems + ['|'] * maxVal

random.shuffle(stars)

partition = []

count = 0
for item in stars:
  if item == '*':
    count += 1
  elif item == '|':
    partition.append(count)
    count = 0

for index, num in enumerate(partition):
  if num != 0:
    printStr = f"item({index + 1}, "
    if num == 1:
      printStr += str(random.randint(1, maxWeight))
    else:
      printStr += "("
      for _ in range(num):
        printStr += f"{random.randint(1, maxWeight)} ; "
      printStr = printStr[:-2] + ")"
    printStr += ")."
    print(printStr)







