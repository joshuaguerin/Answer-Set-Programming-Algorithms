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


