# File: generate.py
# Author: Michael Huelsman

# Description: CNF
# Use: python3 generate.py <n> <c> -l <l> -u <u> > filename.lp
#	where:
#          <n> is the number of literals in the formula.
#          <c> is the number of clauses to generate.
#          <l> is the lower limit on the number of literals per clause (default: 1).
#          <u> is the upper limit on the number of literals per clause (default: 4).
#	       filename.lp is the file to write the instance to
#	The redirect (> filename.lp) can be omitted (to write to stdout)


import argparse
import random

def main(args):
    literals = [i+1 for i in range(args.n)]
    clauses = set()
    # Generate clauses
    while len(clauses) < args.c:
        # Select literals for the new clause.
        lits = random.randint(args.l, args.u)
        clause = random.sample(literals, lits)
        # Randomly negate literals.
        for idx in range(len(clause)):
            clause[idx] *= random.choice([-1, 1])
        # Add clause if it has not already been generated.
        clause = tuple(clause)
        if clause not in clauses:
            clauses.add(clause)
    # Write out the logic program
    for idx, clause in enumerate(clauses):
        for literal in clause:
            print(f'clause({idx+1},{literal}).')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='CNF Formula Generator')
    parser.add_argument('n', type=int, help='The number of literals in the formula.')
    parser.add_argument('c', type=int, help='The number of clauses to generate.')
    parser.add_argument('-l', type=int, default=1, help='The lower limit on the number of literals per clause (default: 1).')
    parser.add_argument('-u', type=int, default=4, help='The upper limit on the number of literals per clause (default: 4).')
    main(parser.parse_args())
