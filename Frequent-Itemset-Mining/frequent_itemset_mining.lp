item(I) :- transaction(_, I).

count(C) :- C = #count{I : item(I)}.

% Create a graph from each transaction.
associate(N, I, J) :- transaction(N, I), transaction(N, J), I!=J.

% Each transaction graph has potential associated subgraphs.
%{ subgraph(N, I, J) } :- associate(N, I, J).

% Compute the intersections of each pair of graphs.
overlap(N, M, I, J) :- associate(N, I, J), associate(M, I, J), I<J, N<M.


% Each item gets a number.
%1 { item(I, 1..X) : count(X) } 1 :- item(I).

% Numbers are unique
%:- item(I, X), item(J, X), I!=J.

% 1 { in(I, 1..7)} 1 :- I=1..C, count(C).

#show overlap/4.
