# Problem: Traveling Salesman Problem

## Description
The generator takes in 3 arguments from the user: Size of the graph (`n`), Connectivity Factor (`f`), and Maximum Weight (`w`). The graph size is how many nodes will appear in the graph. The connectivity factor controls how interconnected our graph will be.
It is a floating-point value in the range [0, 1.0]. We ensure minimum connectivity using [Dirac's Theorem on Hamiltonian Cycles](https://en.wikipedia.org/wiki/Dirac%27s_theorem), as an argument of 0 is going to be minimum connectivity. It states that a graph is guaranteed to have a hamiltonian path, if each vertex
has a degree $\geqslant$ $\frac{n}{2}$. Our generator outputs nearly this minimum, with an occaisonal additional edge or 2. On the other extreme, an argument of 1 will output a fully connected graph (with the exception of self-loops, which are not generated).

For smaller graphs, the user will want a larger connectivity factor if connectivity beyond the minimum is desired.

## Algorithm
The data structure representation is a matrix, with connectivity measured by the number of edges generated. First, we calculate the minimum number from [Dirac's Theorem](https://en.wikipedia.org/wiki/Dirac%27s_theorem) to ensure minimum connectivity for a path to form.
Additional edges are generated randomly to satisfy the desired connectivity factor.
