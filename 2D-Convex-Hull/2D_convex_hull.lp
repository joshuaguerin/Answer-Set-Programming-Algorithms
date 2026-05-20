
 %*
    * Problem: 2D Convex Hull
    * Author: Esteban Morales : https://esteban-morales.onrender.com
 *%


% two point references are identical if both coordinates match.
same_point(AX, AY, BX, BY) :- point(AX, AY), AX = BX, AY = BY.


% point c lies strictly to the right of directed edge a->b.
right_of(AX, AY, BX, BY, CX, CY) :-
    point(AX, AY), point(BX, BY), point(CX, CY),
    Cross = (BX-AX)*(CY-AY) - (BY-AY)*(CX-AX),
    Cross < 0.


% a directed edge is blocked if any point lies to its right.
blocked(AX, AY, BX, BY) :- right_of(AX, AY, BX, BY, _, _).


% a directed edge a->b is a hull edge if it's between two distinct points
% and no otjher point lies strictly to its right.
hull_edge(AX, AY, BX, BY) :-
    point(AX, AY), point(BX, BY),
    not same_point(AX, AY, BX, BY),
    not blocked(AX, AY, BX, BY).


% a point is on the hull if it's an endpoint of any hull edge.
on_hull(X, Y) :- hull_edge(X, Y, _, _).
on_hull(X, Y) :- hull_edge(_, _, X, Y).


% print output
#show on_hull/2.
