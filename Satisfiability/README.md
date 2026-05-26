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
