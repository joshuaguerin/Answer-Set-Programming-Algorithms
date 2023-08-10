%*
 * File: max_flow.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a graph 
 * Use: clingo max_flow.lp instance.lp
 *      where instance.lp contains node and edge predicates.
 *%

% Assign possible values for flow over all edges
flow_vals(0..T) :- T = #max{C : edge(X, Y, C)}.

% Each edge must have a flow value as output
1 { flow(S, E, V) : flow_vals(V) } 1 :- edge(S, E, _).

% Flow on any edge does not exceed capacity.
:- flow(S, E, V), edge(S, E, C), C < V.

% Measure incoming, outgoing flow for each node.
incoming(V, I) :- I = #sum{C : flow(S, V, C)}, node(V).
outgoing(V, O) :- O = #sum{C : flow(V, E, C)}, node(V).

% For every internal node, incoming and outgoing flow are equal. 
:- node(V), not start(V), not terminal(V), incoming(V, I),
   outgoing(V, O), I!=O.

% Maximize overall flow through the network.
#maximize{I : incoming(T, I), terminal(T)}.

% Show the flow
#show flow/3.

% Note: Optimization level reflects network flow.
