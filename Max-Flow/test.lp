% Individual Nodes for the graph
node(0 ; 1 ; 2 ; 3 ; 4 ).

% Start stop for the graph
start(2).
terminal(3).

% edge(start, end, capacity)
edge(2, 4, 1).
edge(4, 0, 5).
edge(4, 1, 3).
edge(0, 3, 7).
edge(1, 3, 10).

