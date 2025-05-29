# File: generate.py
# Author: Joshua Guerin

# Description: Set generator for subset sum problem solver
# Use: python3 generate.py -u u -s s > filename.lp
#	where: u is the upper limit (non-inclusive) for the values of the set
#	       s is the size of the set
#	       filename.lp is the instance file to write to
#	Each of s and u are optional (defaults u=100, s=100)
#	The redirect (> filename.lp) can be omitted (to print to stdout)



import argparse
from random import randint

# Process arguments
parser = argparse.ArgumentParser()
parser.add_argument('-u', default=100, type=int,
                    help="Upper limit on integer size, non-inclusive. (Default: 100)")
parser.add_argument('-s', default=100, type=int,
                    help="Set size: number of values generated. (Default: 100)")
args = parser.parse_args()

upper_limit = args.u
set_size = args.s

# Generate value(). predicate for given parameters.
randint(1, upper_limit)
print("value(", end="")
for i in range(1, set_size):
    print(randint(1, upper_limit), " ; ", sep="", end="")
print(randint(1, upper_limit), ").", sep="")


