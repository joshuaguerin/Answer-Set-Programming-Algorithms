#Problem: K-Clique & Max-Clique

##Generator Description
The generator takes in 2 user arguments, the number of nodes in the graph and the specific size of a clique in the graph.
The program then picks a set of the nodes equal to the clique size. From here, the program starts connecting the nodes to
from the set to each other. Each time a connection is made, the program randomly decides how many additional nodes to connect
to that are not part of the clique. This makes a complex graph to navigate, obscuring the clique. It also allows for other
cliques to be made. The user then can save this to a file via redirects or have the output to the terminal.
