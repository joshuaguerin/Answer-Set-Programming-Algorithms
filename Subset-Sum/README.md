# Problem: Subset Sum

## Description
The [Subset Sum](https://en.wikipedia.org/wiki/Subset_sum_problem) problem is a classical NP-Complete problem in computing and number theory. Given a set of integers, *S*, and a target value *n*, is there a subset of *S* that sums to exactly *S*.

## Example
Let *S* = {1, 2, 3, 4, 10, 11, 12, 14, 18, 20}, and a query of *n*=26.
* This would be satisfied by the subset: {2, 3, 10, 11}, as 2+3+10+11=26.

## Implementational Details
Note that the declaration of value(k ; k). in an instance.lp file will result in a *single* instance of k having property value. For simplicity this implementation was designed where *S* is a *set*, allowing inclusion, but not duplicates. For a multi-set-based implementation (see below), modification would be necessary.

## Problem Variants
There are several variants of this problem that are NP-Complete. Some assumptions in this encoding are:
* A [set](https://en.wikipedia.org/wiki/Set_(mathematics)) of values is encoded (vs. a [multiset](https://en.wikipedia.org/wiki/Multiset)) because the encoding of values is a single predicate.
* Generating software is over positive integers (an arbitrary decision that should be easy to modify).

## Related
See also:
* [equal sum partitioning](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Numerical-3-Dimensional-Matching) and
* [numerical 3-dimensional matching](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Numerical-3-Dimensional-Matching).
