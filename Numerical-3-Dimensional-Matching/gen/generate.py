# File: generate.py
# Author: Jackson Madsen

# Description: Set generator for Numerical 3-Dimension problem solver
# Use: python3 generate.py -s s -n n > filename.lp
#	where: s is the the size of each set, inclusive
#	       n is the target value for the triples
#	       filename.lp is the location to write the instance to
#	Each of s, n are optional (Defaults: s=5, n=10)
#	The redirect (> filename.lp) can be omitted (to print to stdout)

import random
import argparse

# Process arguments
parser = argparse.ArgumentParser()
parser.add_argument('-n', default=10, type=int,
                    help="Target vale for the triples. (Default: 10)")
parser.add_argument('-s', default=5, type=int,
                    help="Set the size of each set. (Default: 5)")
args = parser.parse_args()

targetVal = args.n
maxSize = args.s

# Here we use the stars and bars method to generate a random permutation
# The total number of stars is the target value.
# Each bar will partition the list such that the number of stars before encountering a bar will be the value that gets appended.
# When we shuffle, the list is partitioned and gives us one of the triples.
# Read in the values from the shuffled list, then appened those to one of each of the lists.
# Repeat n times until we have 3 sets of the requested size from the User.
stars = ['*'] * targetVal + ['|'] * 2

sets = [[], [] ,[]]

while len(sets[0]) < maxSize:
  random.shuffle(stars)
  partition = []

  count = 0
  for item in stars:
    if item == '*':
      count += 1
    elif item == '|':
      partition.append(count)
      count = 0
  partition.append(count)

  for index, item in enumerate(partition):
    sets[index].append(str(item))

  random.shuffle(stars)

char = 'x'

for part in sets:
  seperator = " ; "
  printStr = f"{char}( {seperator.join(part)}"
  print(printStr[:-3],").")

  char = chr(ord(char) + 1)
