# Problem: Numerical 3-Dimensional Matching

# Description
The generator takes in 2 arguments from the user. How large the sets should be (this can also be seen as how many triples to produce) and the target value.
For generating the sets, we borrow an approach from combinatorics called the [Stars & Bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)) method.
We make a list with a number of stars equal to the target value and 3 bars (since there are 3 sets to generate). Then we shuffle the list and count how many stars 
we encounter until the next bar. This is partitions the list into 3 portions and guarantees that we always sum to the appropriate value. Then we add one of each 
value to each of the lists. When we have reached the requested amount of values, we print the lists in the proper format.
