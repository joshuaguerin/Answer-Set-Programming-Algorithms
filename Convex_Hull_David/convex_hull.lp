%*
 * File: convex_hull.lp
 * Author: Joshua T. Guerin, David J Gonzalez, (Jackson Madsen)
 *
 * Description: Given a set of points in the plane, find the convex hull of the points.
 *
 * Use: clingo convex_hull.lp instance.lp
 *          where instance.lp contains point information.
 *%


% Toy domain
point(0,0 ; 0,4 ; -4,0 ; 5,0 ; 0,-6 ; 1,0).
% Solution: (-4, 0), (5, 0), (0, -6), (0, 4)


%% Use cross product method to determine triangle inclusion.

% Identify all possible triangles.
triangle((U, V), (W, X), (Y, Z)) :- point(U, V), point(W, X), point(Y, Z).


% Cross product method.
internal(A, B) :- triangle((U, V), (W, X), (Y, Z)),
        (A - U)*(X - V) - (W - U)*(B - V) > 0,
		(A - W)*(Z - X) - (Y - W)*(B - X) > 0,
		(A - Y)*(V - Z) - (U - Y)*(B - Z) > 0,
		point(A, B).
% internal(A, B) :- triangle((U, V), (W, X), (Y, Z)),
%         (A - U)*(X - V) - (W - U)*(B - V) < 0,
% 		(A - W)*(Z - X) - (Y - W)*(B - X) < 0,
% 		(A - Y)*(V - Z) - (U - Y)*(B - Z) < 0,
% 		point(A, B).
% { internal(A, B, N, M, P) } 1 :- triangle((U, V), (W, X), (Y, Z)),
%         N = (A - U)*(X - V) - (W - U)*(B - V),
% 		M = (A - W)*(Z - X) - (Y - W)*(B - X),
% 		P = (A - Y)*(V - Z) - (U - Y)*(B - Z),
% 		point(A, B).
% #show internal/5.
% { internal(A, B, N, M, P) } 1 :- point(A, B).

% { internal(A, B) } 1 :- point(A, B).
% { hull(A, B) } 1 :- point(A, B).

% #minimize { 1, A, B : hull(A, B) }.

% A point inside a triangle is internal (and hence not in the hull).
hull(X, Y) :- point(X, Y), not internal(X, Y).

#show internal/2.
#show hull/2.

