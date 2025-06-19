% Individual Nodes for the graph
node(0 ; 1 ; 2 ; 3 ; 4 ).

% Start stop for the graph
start(4).
terminal(1).

% edge(start, end, capacity)
edge(4, 0, 7).
edge(4, 2, 4).
edge(0, 3, 6).
edge(2, 4, 7).
edge(3, 1, 9).

