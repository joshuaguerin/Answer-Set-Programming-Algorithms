# Problem: Knapsack

## Description

The **knapsack** problem  is an optimization problem. Given a set of items *I*, where each item is associated with a value and a weight (cost, etc.), *i<sub>x</sub> = (v, w)* and a knapsack capacity, *c*, find the subset of *I* that maximizes total value without exceeding capacity *c*.

The problem is also known as the **0-1 knapsack problem** due to the inclusion/exclusion of items.

## Example
If we have items *I* = {(1, 2), (2, 1), (3, 3), (5, 5)}, and a capacity *c*=6, we can pack the knapsack with items:
* {(2, 1), (5, 5)}

which meets the knapsack's capacity at total weight of 6, and a total value of 7.

Note that the alternate packing of {(1, 2), (2, 1), (3, 3)} would also meet the capacity of 6, however it would result in a sub-optimal total value of 6.

## Related
See also the [bin-packing](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Bin-Packing) problem.
