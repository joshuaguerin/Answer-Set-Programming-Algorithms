# Problem: Vertex-Cover Generator

## Description
The generator takes in 2 arguments from the User. Graph size and a connectivity factor. The graph size is how many nodes will
appear as part of the graph. The connectivity factor controls how interconnected our graph is going to be. It is a floating-point value in the range
[0, 1.0]. We do ensure minimal connectivity, as an argument of 0 will output a [Minimum Spanning Tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree). On the other extreme, 1 will be fully connected (with the exception of self-loops, which are not generated).

For smaller graphs the user will want a larger connectivity factor (> .5) if connectivity far beyond the minimum spanning tree is desired.

## Algorithm
The generator first lists all the possible nodes for the solver. Then it generates a minimum spanning tree using 
[Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search). We use a n x n matrix to represent our graph. At any
given point, if it is a 1, then there is an edge between it's coordinates, otherwise 0. Example if (2,3) is a 1, then there is 
an edge from node 2 to node 3. Since this is an undirected graph, order doesn't matter. However, for the matrix it does. 
So any time we check (X,Y) we also check (Y,X) before making an edge. Once we have placed our spanning tree in the matrix, 
we calculate how many edges we need based on the maximum number of edges possible for the graph, multiplied by our connecting factor.
The spanning tree is our minimum, so we do not remove edges if the number is lesser. If the number is greater, then we begin
adding random edges until our matrix sums to the number. Finally we print out our matrix in the appropriate format.
