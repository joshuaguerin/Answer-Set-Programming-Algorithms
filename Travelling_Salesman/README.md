# Problem: Travelling Salesman Problem

## Description
Given a graph, *G=(V, E)* and a start and end vertex, *s* and *e*, a **path** in a graph is a finite sequence of edges from *s* to *e*.

A **path** is **Hamiltonian** if all vertices *V* occur *exactly once* in the path.

A **Hamiltonian Path** is a solution to the **Travelling Salesman** Problem if it is the *smallest* such path.

E.g.,

![Example Graph](images/graph.png)

From: [Wikipedia](https://en.wikipedia.org/wiki/Travelling_salesman_problem#Description)

In the above graph, one of many Hamiltonian paths from *a* to *d* is:
* a -> c -> b -> d, at a path length of 106.

However, only one such path is a solution to the Travelling salesman problem:
* a -> b -> c -> d, with a minimal path length of 62.

Note that due to the similarities between the two algorithms, the implementations may be nearly identical.
* Only an additional minimization constraint is required to go from one to the other.

## Problem Variants
Both the Hamiltonian Path problem and The Travelling Salesman Problem are phrased above in terms of paths, with distinct start and end points, *s* and *e*. Both problems can be phrased as both a *path* or a *cycle*. The latter is reformulated in terms of a single point that servers as *both* start and end. I.e., the cycle formulation starts and ends at the same location.

Because the computational complexity of the problem is the same irrespective of whether it is phrased as a path or cycle, the *path* problem formulation has been selected for consistency in these examples.
