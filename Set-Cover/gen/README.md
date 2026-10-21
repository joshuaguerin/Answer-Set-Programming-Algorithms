# Set Cover & Exact Set Cover Generators


## Generator Description

1. The generator takes in 2 (optional) command-line arguments, the number of elements in the universe (n) and the number of subsets (k).
2. The program generates a universe of elements (the first n integer numbers) and sample (k-1) subsets of the universe.
3. The program complete the subsets with the k-th subset with the elements that where not found in any of the previous samples, to avoid degenerate case where the union of all subsets does not cover the universe.
