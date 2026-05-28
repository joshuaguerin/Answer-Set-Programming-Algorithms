# Problem: CNF Boolean Satisfiability

## Description
Given a logical formula &phi; in conjunctive normal form (CNF), an AND of ORs, find an assignment to the literals in &phi; such that &phi; evaluates to true under that assignment.

Problems related to boolean satisfiability:

- SAT - Find a satisfying assignment.
- Max-SAT - Find an assignment which maximizes the number of satisfied clauses.

## Example

Given the formula:


&phi; = (a &or; b) &and; (&not;a &or; c &or; d) &and; (&not;b &or; &not;d)


A satisfying assignment is to set a = True, b = False, c = True, and d = True. This is not the only satisfying assignment to &phi;

## Problem Variants

### 2-SAT

The [2-Satisfiability problem](https://en.wikipedia.org/wiki/2-satisfiability) is a special case of CNF Satsifiability where clauses are limited to length 2. Unlike more general versions of CNF-SAT, 2-SAT is NL-Complete, and can be solved in Polynomail time.

### 3-SAT

The [3-Satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#3-satisfiability) is a special case of CNF Satisfiabiliyt where clauses are limited to length 3. Unlike 2-SAT, and like unrestricted CNF Satisfiability, 3-SAT is NP-Complete, and the only known algorithms that solve it run in exponential time in the worst case.

### MAX-SAT

The [Maximum Satisfiability problem](https://en.wikipedia.org/wiki/Maximum_satisfiability_problem) (MAX-SAT) is a *generalization* of the CNF Satisfiability problem. MAX-SAT allows unsolved clauses, and instead seeks to *maximize* the number of clauses that evaluate to True. This problem is in NP-Hard, making it more difficult to solve in practice than most other variants named here.

### Other SAT Forms

Many other forms of SAT exist, like DNF-SAT, which switches the roles of `and` and `or` operations.

## Theoretical Significance

