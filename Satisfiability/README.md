# Problem: Boolean Satisfiability

## Description
The [Boolean Satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem) (SAT) is an NP-Complete problem of deep theoretical importance to the world of Computer Science. The problem takes a Boolean expression (comprised of `and` (&and;), `or` (&or;), and `not` (&not;) operators and variables as input, and seeks to find an assignment to variables that makes the expression evaluate to `True`.

### CNF Satisfiability
One of the most common forms of the SAT problem is CNF satisfiability. In CNF satisfiability a *clause* is a statement comprised of variables and `and` operators. E.g., (&not;a &or; c &or; d).

A full formula, &phi;, in conjunctive normal form (CNF), is a *conjunction* (`and`) of clauses.

E.g., 
	&phi; = (a &or; b) &and; (&not;a &or; c &or; d) &and; (&not;b &or; &not;d)

is a valid expression in CNF form.

Software designed to solve Satisfiability problems are know as [SAT solvers](https://en.wikipedia.org/wiki/SAT_solver).

## Example

Given the formula &phi; above, we can *satisfy* the formula:
* `a = True`, `b = False`, `c = True`, and `d = True`.

This is not the only satisfying assignment to &phi;.

Note that identifying a *satisfying valuation* to &phi; is fairly straight-forward. Due to the nature of the `or` operator, *any* assignment that is included in a clause satisfies the clause, and an assignment that satisfies each individual clause satisfies the entire expression.

## Problem Variants

Satisfiability, logic, and logic programming are active areas of research with many possible problem variations.

### 2-SAT

The [2-Satisfiability problem](https://en.wikipedia.org/wiki/2-satisfiability) is a special case of CNF Satsifiability where clauses are limited to length 2. Unlike more general versions of CNF-SAT, 2-SAT is NL-Complete, and can be solved in Polynomail time.

### 3-SAT

The [3-Satisfiability problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem#3-satisfiability) is a special case of CNF Satisfiabiliyt where clauses are limited to length 3. Unlike 2-SAT, and like unrestricted CNF Satisfiability, 3-SAT is NP-Complete, and the only known algorithms that solve it run in exponential time in the worst case.

### MAX-SAT

The [Maximum Satisfiability problem](https://en.wikipedia.org/wiki/Maximum_satisfiability_problem) (MAX-SAT) is a *generalization* of the CNF Satisfiability problem. MAX-SAT allows unsolved clauses, and instead seeks to *maximize* the number of clauses that evaluate to True. This problem is in NP-Hard, making it more difficult to solve in practice than most other variants named here.

### Other SAT Forms

Many other forms of SAT exist, like [Disjuntive Normal Form](https://en.wikipedia.org/wiki/Disjunctive_normal_form) (DNF-SAT), which switches the roles of `and` and `or` operations.

## Theoretical Significance

While this repository explores many problems of historical and theoretical importance, Boolean Satisfiability serves an important role in the history of theoretical and applied Computer Science.

The [Cook–Levin theorem](https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem) established that Boolean Satisfiability is NP-Complete, the first such problem to be identified in the class. Not long after, Richard Karp used this result to locate the first 21 NP Complete problems (known as [Karp's 21 NP-Complete Problems](https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems)). This list included 3-SAT, which was used to demonstrate that a number of other problems were NP-Complete.

While SAT solvers were an active area of research for decades prior, the late 1990s and early 2000s saw a significant advancement in the state of the art--technology that would later pave the way for modern [Answer Set Programming languages](https://en.wikipedia.org/wiki/Answer_set_programming) such as [Clingo](https://potassco.org/clingo/).
