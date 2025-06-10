# Problem: Vertex-Cover Generator

## Description
The generator takes in 2 arguments from the User. Graph size and a connectivity factor. The graph size is how many nodes will
appear as part of the graph. The connectivity factor controls how interconnected our graph is going to be. It is a floating-point value in the range
[0, 1.0]. We do ensure minimal connectivity, as an argument of 0 will output a [Minimum Spanning Tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree). On the other extreme, 1 will be fully connected (with the exception of self-loops, which are not generated).

For smaller graphs the user will want a larger connectivity factor (> .5) if connectivity far beyond the minimum spanning tree is desired.

## Algorithm
The data structure representation is a matrix, with connectivity measured by the number of edges generated. First a minimum spanning tree is generated using a recursive, [depth-first search](https://en.wikipedia.org/wiki/Depth-first_search) strategy to ensure a minimal level of connectivity. Additional edges are generated randomly to satisfy the desired connectivity factor.
