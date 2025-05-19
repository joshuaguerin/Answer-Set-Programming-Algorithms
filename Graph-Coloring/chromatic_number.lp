%*
 * File: graph_coloring.lp
 * Author: David Gonzalez, Joshua T. Guerin
 *
 * Description: Given a graph, find the minimal set of colors s.t. no
                adjacent veritices share a color.
 * Use: clingo chromatic_number.lp instance.lp
 *%

% Count the number of nodes/max colors.
count(N) :- N = #count{X : node(X)}.

% Set of available colors (max=number of nodes).
color(1..N) :- count(N).

% Edges are symmetric.
% Assumes potentially directed description of an undirected graph.
edge(M, N) :- edge(N, M).

% Each vertex is assigned a single color.
1 { color(N, C) : color(C) } 1 :- node(N).

% No two adjecent vertices can have the same color.
:- edge(N, M), color(N, C), color(M, C).

% Count the number of colors.
number(X) :- X = #count{ C : color(N, C) }.

% Minimize the number of colors used.
#minimize { X : number(X) }.

% PRINT
% Optional--display of color information is likely useful.
#show color/2.

% The chromatic number.
#show number/1.
