%*
 * File: graph_coloring.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph and a set of colors, find an assignment of
 *              colors to vertices s.t. no two adjacent vertices share a color.
 * Use: clingo graph_coloring.lp instance.lp -c n=<val>
 *  where $n$ is the number of available colors.
 *%

% Set of available colors.
color(1..n).

% Edges are symmetric.
% Assumes potentially directed description of an undirected graph.
edge(M, N) :- edge(N, M).

% Each vertex is assigned a single color.
1 { color(N, C) : color(C) } 1 :- node(N).

% No two adjacent vertices can have the same color.
:- edge(N, M), color(N, C), color(M, C).

% Output color information.
#show color/2.