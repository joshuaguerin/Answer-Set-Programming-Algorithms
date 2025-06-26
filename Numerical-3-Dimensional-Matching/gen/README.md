# Problem: Numerical 3-Dimensional Matching

# Description
The generator takes in 2 arguments: the desired set size (`s`) for each input set and the target value of the sum (`n`).

# Algorithm
For generating the sets, we borrow an approach from combinatorics called the [Stars & Bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)) method.
We make a list with a number of stars equal to the target value and 3 bars (since there are 3 sets to generate). Then we shuffle the list and count how many stars 
we encounter until the next bar. This is partitions the list into 3 portions and guarantees that we always sum to the appropriate value. Then we add one of each 
value to each of the lists. 

Due to the algorithm the solver uses, no set can contain repeat elements. So occainsonally, the sets may be a few shorter than the user 
expects. Generally, larger target values and smaller set sizes produce the desired set size every time.
