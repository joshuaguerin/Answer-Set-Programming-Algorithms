# Problem: Subset Sum

## Description
The [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) problem is a standard NP-Hard problem in computing and number theory. Given a set of integers, *S*, and a target value *n*, is there a subset of *S* that sums to exactly *S*.

E.g.,
Let *S* = {1, 2, 3, 4, 10, 11, 12, 14, 18, 20}, and a query of *n*=26.
* This would be satisfied by the subset: {2, 3, 10, 11}, as 2+3+10+11=26.


There are several variants of this problem that are NP-Hard. Some assumptions in this encoding are:
* A [set](https://en.wikipedia.org/wiki/Set_(mathematics)) of values is encoded (vs. a [multiset](https://en.wikipedia.org/wiki/Multiset)) because the encoding of values is a single predicate.
* Generating software is over positive integers (an arbitrary decision that should be easy to modify).

