%*
 * File: intra_distance_cluster.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given a set of data vectors (2D) and an integer k, find
 * 		k clusters (sets) that minimize overall, intra-cluster
 *		distance.
 * Use: clingo k_intra_cluster.lp instance.lp -c k=<val>
 *%

% There are k clusters.
cluster(1..k).

% Each data vector must be in a cluster
1 {cluster((X, Y), C) : cluster(C)} 1 :- vector(X, Y).

% Manhattan distance between data vectors
distance((X, Y), (X', Y'), |X-X'| + |Y-Y'|) :-
	     vector(X, Y), vector(X', Y'), X<X'.
	     
distance((X, Y), (X', Y'), |X-X'| + |Y-Y'|) :-
	     vector(X, Y), vector(X', Y'), Y<Y'.

% Cluster weight: Sum intra-cluster distances
weight(C, S) :- S = #sum{D, V, V' : distance(V, V', D),
 	      	    cluster(V, C), cluster(V', C)}, cluster(C).

% Minimize total weight of clusters based on intra-cluster distance
#minimize{S, C : weight(C, S)}.

#show weight/2.
#show cluster/2.
%#show distance/3.
