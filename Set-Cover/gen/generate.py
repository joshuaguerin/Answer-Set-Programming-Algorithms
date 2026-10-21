# File: generate.py
# Author: Samuel Ortion
#
# Description: Set generator for the Set Cover and Exact Set Cover solvers
# Use: python3 generate.py -n n -k k > filename.lp
#   where: n is the number of element in the universe
#   k is the number of subset of the universe
#   filename.lp is the instance file to write to
#
#    Each of n and k are optional (defaults n=10, k=3).
#    The redirect (> filename.lp) can be ommitted (to print to stdout).
#  

import argparse
from random import randint, sample

# Process arguments
parser = argparse.ArgumentParser()

parser.add_argument('-n', default=10, type = int,
                    help = "Number of element in the universe set. (Default = 10)")
parser.add_argument('-k', default=4, type=int,
                    help = "The number of subsets (Default=4)")
args = parser.parse_args()
num_elements = args.n
elements = list(range(num_elements))
num_subsets = args.k
# Generate all subsets randomly but one
subsets = []
for i in range(num_subsets - 1):
    subset_size = randint(1, num_elements)
    subset = sample(elements, subset_size)
    subsets.append(subset)
# Add the remaining elements of the universe in another set,
# to ensure all elements are represented at least once
union = set([element for element in subset
                  for subset in subsets])
missing = set(elements).difference(union)
subsets.append(list(missing))

# Write the universe
for element in elements:
    print(f"universe({element}).")

# Write the content of each subset
for index, subset in enumerate(subsets):
    for element in subset:
        print(f"is_in({index}, {element}).")

