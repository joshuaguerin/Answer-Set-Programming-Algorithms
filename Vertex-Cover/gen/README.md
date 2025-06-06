# Problem: Vertex-Cover Generator

## Description
The generator takes in 2 arguments from the User. Graph size and a connecting factor. The graph size is how many nodes will
appear as part of the graph. The connecting factor controls how interconnected our graph is going to be. It is a number from
0 to 1. 0 will output only a [Minimum Spanning Tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree), or a tree that includes 
all nodes of the graph exactly once. 1 will output a graph where every node is connected to every node. The default is 0.5, 
which will generate half of the maximum number of edges. With smaller graphs, the factor will still only sometimes only output
the minimum spanning tree since there must be n - 1 edges in a minimum spanning tree.

# How it works
The generator first lists all the possible nodes for the solver. Then it generates a minimum spanning tree using 
[Depth-First Search](https://en.wikipedia.org/wiki/Depth-first_search). We use a n x n matrix to represent our graph. At any
given point, if it is a 1, then there is an edge between it's coordinates, otherwise 0. Example if (2,3) is a 1, then there is 
an edge from node 2 to node 3. Since this is an undirected graph, order doesn't matter. However, for the matrix it does. 
So any time we check (X,Y) we also check (Y,X) before making an edge. Once we have placed our spanning tree in the matrix, 
we calculate how many edges we need based on the maximum number of edges possible for the graph, multiplied by our connecting factor.
The spanning tree is our minimum, so we do not remove edges if the number is lesser. If the number is greater, then we begin
adding random edges until our matrix sums to the number. Finally we print out our matrix in the appropriate format.
