# Problem: Wolf, Goat, and Cabbage

## Description

A farmer starts on the left bank of a river. The farmer can only carry one passenger with him across the river at a time, but there is a catch. If left alone (without the farmer) the:
* wolf will eat the goat
* goat will eat the cabbage.
Neither the goat nor the cabbage are in danger if the farmer is there to supervise.

The farmer must plan a series of trips back and forth across the river to ensure that all three passengers (eventually) arrive safely on the right bank of the river with the farmer. When needed the farmer can take a trip without a passenger. In *any instance* the farmer is required to move the boat.

This is an example of a puzzle that requires some implicit/explicit notion of *time*--proper sequencing of actions is required, as each action affets the *state* of the puzzle.

![Wolf, Goat, and Cabbage Manuscript](Illuminated_illustration_of_the_wolf,_goat_and_cabbage_problem_in_the_Ormesby_Psalter.jpg)

Illustration from [Wikipedia](https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem).

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

In this example, time 0 has everyone on the left. The first move at time 1 has the farmer taking the goat across, and at time 2 the farmer returns passengerless. At time 3 the farmer takes the cabbage, only to return with the goat at time 4. At time 5 the farmer takes the wolf, and returns passengerless at time 6. Finally, the farmer is safe to take the goat across at time 7, completing the puzzle.