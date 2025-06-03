# Problem: Vertex-Cover Generator

## Description
The solver only has one input variable which is the number of nodes. We elected to not guarantee certain covers
to be possible in the spirit of keeping the generation simpler for the user to understand.

The generator first lists all the possible nodes. It keeps track of which nodes are connected to each other by referencing
backwards (or forwards) to see if this node has already been connected by an edge. With small instances, this does lead to
more connected graphs, but when we get larger graphs, the graphs become less connected
