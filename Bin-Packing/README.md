# Problem: Bin Packing

## Description

The **Bin Packing** problem is an optimization problem. Given a set of items, $I$, where each item is associated with a label and a cost, *i<sub>x</sub> = (l, c)* (size, weight, etc.), and a max bin capacity, *c*, find the smallest number of bins that will fit all items without exceeding any bin's capacity.

E.g.,
If we have items *I* = {(1, 2), (2, 1), (3, 3), (5, 5)}, and a capacity *c*=6, we can pack our items optimally in 2 bins with:
* *b*<sub>1</sub> = {2, 5} and *b*<sub>2</sub> = {1, 3}.

In this case neither bin exceeds capacity (*b*<sub>1</sub> is filled 6/6 and *b*<sub>2</sub> is 5/6).

## Related
See also the [knapsack problem](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Knapsack).