# Problem: Max Flow

## Description
The generator takes in up to 5 arguments from the user: the number of Nodes in the graph (`n`), a connectivity factor (`f`),
the maximum weight/capacity of an edge (`w`), the maximum number of layers in the graph(`l`), and an optional flag allowing 
for cycles (`--cyclic`). The connectivity factor (`f`) controls how interconnected the graph will be. It is a floating-point 
value in the range [0,1.0]. We ensure minimum connectivity, as an argument of 0 will output minimum linkage in the network 
to get from the starting node to the end node. On the other extreme, an argument of 1 will be fully connected (with the 
exception of self-loops, which are not generated). (`l`) represents the number of layers between the starting and ending 
nodes. Some of these layers may be empty depending on the number of nodes included in the graph.

If the user wants larger layer, they will need to include either more nodes, or less layers.
Caution should be used when pairing a high connectivity factor and the cyclic flag as this can make very complex graphs
that can make it difficult to verify solutions by hand.

## Algorithm
The generator first connects the starting node to all nodes in the first layer, then it makes edges somewhat at random at
each additional layer, making sure there is still a trace back to the starting node. Finally, at the layer just before the 
ending node, it connects all the nodes to the terminal node. Throughout this process, it is also randomly choosing nodes 
within the same layer to connect to each other (avoiding self-loops, which are not generated).
