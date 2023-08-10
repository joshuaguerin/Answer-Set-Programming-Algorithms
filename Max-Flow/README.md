# Problem: Max Flow

## Description

Let *G=(V, E)* be a directed graph. **Network  flow** problems annotate edges with maximum capacities: *e = (s, e, c)*, where the capacity, *c*, defines the maximum amount of "flow" over *e*. (Think: moving water or electricity, packages in transit, railways, etc.)

The **Max Flow* problem is a network flow optimization problem where the following restrictions must be met:
* there are dedicated start and terminal nodes,
* flow over an edge may not exceed its capacity,
* for any internal (not start or terminal) node, total incoming flow must equal total outgoing flow,
* and we wish to *maximize* flow through the network from the start to the terminal node.