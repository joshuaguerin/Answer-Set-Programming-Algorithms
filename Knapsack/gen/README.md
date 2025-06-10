# Problem: Knapsack Generator

## Description
The generator allows for the user to describe the number of items in the set,
the maximum value that can appear in the set, as well as the maximum weight that can
appear in the set.

The program borrows an approach from combinatorics called the [Stars & Bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)) 
method to partition out how many items of each value we will have. 


It first makes a list containing a number of stars equal to the number of items and a number 
of bars equal to the maximum value that can appear in the set. Then we shuffle the list. Once
shuffled, we can count how many stars appear before we reach a bar. This count is how many items
of that value we will have available. We record these values into a list.

Finally, we go through the new list and randomly generate weights for the items of each value. If there 
are no items of the specific value, then we move on. We start counting at a value of 1, since items of 
value 0 defeat the purpose of the problem.

