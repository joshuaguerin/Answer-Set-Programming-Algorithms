# Instance Generator: CNF Boolean Satisfiability

## Description
The generator creates a random CNF Boolean Satisfiability instance based on user provided arguments.
The generator takes two required positional arguments:
  1. `n` the number of literals.
  2. `c` the number of clauses to generate.

The generator also takes two optional arguments:
  1. `-u` the upper bound on the number of literals per clause (default: 4).
  2. `-l` the lower bound on the number of literals per clause (default: 1).
