# Problem: Wolf, Goat, and Cabbage

## Description

A farmer starts on the left bank of a river. The farmer can only carry one passenger with him across the river at a time, but there is a catch. If left alone (without the farmer) the:
* wolf will eat the goat
* goat will eat the cabbage.
Neither the goat nor the cabbage are in danger if the farmer is there to supervise.

The farmer must plan a series of trips back and forth across the river to ensure that all three passengers (eventually) arrive safely on the right bank of the river with the farmer. When needed teh farmer can take a trip without a passenger.

## Example

|  Time  | Left Bank  | Boat | Right Bank |
| ------------- | ------------- | ------------- | ------------- |
| 0 | ['f', 'w', 'g', 'c']  | Empty  | []  |
| 1 | ['c', 'g', 'w', 'f']  | g ->  | []  |
| 2 | ['c', 'w'] | <- no passenger |  ['g', 'f'] |
| 3 | ['c', 'w', 'f'] | c -> | ['g'] |
| 4 | ['w'] | <- g | ['c', 'g', 'f'] |
| 5 | ['g', 'w', 'f'] | w -> | ['c'] |
| 6 | ['g'] | <- no passenger | ['c', 'w', 'f'] |
| 7 | ['g', 'f'] | g -> | ['c', 'w'] |

