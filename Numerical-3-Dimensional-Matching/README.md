# Problem: Numerical 3-Dimensional Matching

## Description

Assume three sets of integers of equal size: *X*, *Y*, and *Z*, and a parameter *n*. We wish to compute a new set of ordered triples, *T*, where each triplet *t=(x, y, z)* meets the following constraints:
* each of *x*, *y*, and *z* are members of *X*, *Y*, and *Z*, respectively,
* each member of *X*, *Y*, and *Z* occurs *exactly once* in a triplet,
* each triplet must sum to *n*.

E.g.,
Let *X* = {7, 1, 5, 4}, *Y*={0, 2, 1, 3}, and *Z*={5, 8, 0, 4}, with *n*=10. We can compute a solution of 4 triples:
* T = {(5,0,5), (1,1,8), (7,3,0), (4,2,4)}.

## Problem Variants
Intuitively, the additive constraint is only *one* such possibile constraint. Additional variants could be constructed over non-numeric domains (e.g., assigning doctors x patients x rooms for scheduling purposes). The problem could also be phrased as a graph problem where *X*, *Y*, and *Z* contain nodes of a graph, with edges between elements *X* and *Y*, *Y* and *Z*. In this case the problem could be viewed as a selection of edges in the graph that will connect and match distinct elements of *X*, *Y*, and *Z* such that the edges denote the triples.

## Related
See also:
* [subset sum](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Subset-Sum) and
* [equal sum partitionng]{https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Equal-Sum-Partition}.