# Problem: CNF Boolean Satisfiability

## Description
Given a logical formula &phi; in conjunctive normal form (CNF), AND of ORs, find an assignment to the literals in &phi; such that &phi; evaluates to true under that assignment.

Problems related to boolean satisfiability:

- SAT - Find a satisfying assignment.
- 3-SAT - SAT which limits clause size to 3 literals OR'd together.
- Max-SAT - Find an assignment which maximizes the number of satisfied clauses.

## Example

Given the formulas &phi; = (x1 OR x2) AND (-x1 OR x3 OR x4) AND (-x2 OR -x4), a satisfying assignment is to set x1 = True, x2 = False, x3 = True, and x4 = True. This is not the only satisfying assignment to &phi;
