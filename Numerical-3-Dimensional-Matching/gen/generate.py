# File: generate.py
# Author: Jackson Madsen

# Description: Set generator for Numerical 3-Dimension problem solver
# Use: python3 generate.py -s s -n n > filename.lp
#	where: s is the maximum size of each set, inclusive
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

sets = []

for _ in range(maxSize):
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

  seen = False
  for index, part in enumerate(partition):
    for item in sets:
      if part == item[index]:
        seen = True

  if not seen:
    sets.append(partition)

  random.shuffle(stars)

char = 'x'

#print(sets)

x = []
y = []
z = []

for i in range(len(sets)):
  a, b, c = sets[i]
  x.append(a)
  y.append(b)
  z.append(c)

random.shuffle(x)
random.shuffle(y)
random.shuffle(z)

print("% GENERATE")
print("% Custom instance works with a parameter of n=", targetVal)

#print(x)
print("x(", end="")
for val in x[:-1]:
  print(val, end=" ; ")
print(x[-1], ").", sep="")

#print(y)
print("y(", end="")
for val in y[:-1]:
  print(val, end=" ; ")
print(y[-1], ").", sep="")

#print(z)
print("z(", end="")
for val in z[:-1]:
  print(val, end=" ; ")
print(z[-1], ").", sep="")

# for index in range(3):
#   printStr = f"{char}("

#   for part in sets:
#     printStr += f"{part[index]} ; "

#   print(printStr[:-3] + ").")

#   char = chr(ord(char) + 1)




