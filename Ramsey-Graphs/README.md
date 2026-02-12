# Problem: Ramsey Graphs


## Description

A **graph**, *G = (V, E)*, is comprised of a set of **vertices** and connections called **edges**.

A complete graph on *n* vertices, *K<sub>n</sub>* is a graph where all vertices are connected by an edge.

Given a graph, *G*, as input, a **clique** is a subgraph that is complete.

While searching for a [clique](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Clique) in a given graph is a common phrasing of the clique problem, Ramsey graphs are related to [Ramsey's theorem](https://en.wikipedia.org/wiki/Ramsey%27s_theorem):

Given a complete graph on and two colors, **r**ed and **b**lue, there exists a least positive integer *R(r, b)* for which every coloring contains either a *red* clique of size **r** or a blue clique of size **s**.





A **complete** graph is a graph where every vertex is connected by an edge.


* **K-Clique** - Given *G* and an integer *k*, find a clique with *k* vertices.
* **Max Clique** - Given *G*, locate the *largest* clique in the graph.

## Example
See the following example for a *3-clique* in a graph of 6 vertices:

![Graph with a 3-clique](images/6n-graf-clique.svg.png)

From [Wikipedia](https://en.wikipedia.org/wiki/Clique_problem#Definitions)

## Dependencies
The [print](print/) system generates [graphviz](https://graphviz.org/) files for input, that can be viewed, redirected into a file, or rendered using dot. The latter step can be omitted if graphviz is not present or if graphical output is not desired. 

## Related
See also:
* [clique](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Clique) 
