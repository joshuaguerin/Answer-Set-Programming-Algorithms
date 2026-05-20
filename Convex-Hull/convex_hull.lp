% File: convex_hull.lp
% Author: Michael Huelsman
% Created On: 19 May 2026
% Idea: Convex hull through point selection and polygon testing.
% Assumptions:
%   All points are on an integer grid.
% Instances are a seires of point(X,Y) predicates.

% Determine number of points
point_count(N) :- N = {point(X,Y)}.

% Generate polygon selection
3 {polygon(X,Y): point(X,Y)} N :- point_count(N).

% Polygon count
poly_count(N) :- N = {polygon(X,Y)}.

% Order polygon points
1 {polygon(I,X,Y): polygon(X,Y)} 1 :- I = 1..N, poly_count(N).
% Can't put a point in the order twice.
:- polygon(I1, X, Y), polygon(I2, X, Y), I1 != I2.

%Define line segements of the polygon
%Sorts line segements so first polygon point is less in the Y direction.
line_segment(polygon(I1,X1,Y1), polygon(I2,X2,Y2)) :- polygon(I1,X1,Y1), polygon(I2,X2,Y2), I2-I1 = 1.
line_segment(polygon(1,X1,Y1), polygon(N,X2,Y2)) :- polygon(1,X1,Y1), polygon(N,X2,Y2), poly_count(N).

% Simplify line_segement predicate
line_segment(polygon(X1,Y1), polygon(X2,Y2)) :- line_segment(polygon(_,X1,Y1),polygon(_,X2,Y2)).

% Determine if a point is in the polygon (by being on the hull.)
inside(point(X,Y)) :- polygon(X,Y).

% Determine if a point is in the polygon using ray crossing count.
ray_cross(point(X,Y), line_segment(polygon(X1,Y1), polygon(X2,Y2))) :-
  point(X,Y), polygon(X1,Y1), polygon(X2,Y2), not polygon(X,Y),
  line_segment(polygon(X1,Y1), polygon(X2,Y2)),
  X1 < X2, X >= X1, X <= X2,
  Cross_numer=((Y2-Y1) * (X - X1)) - (Y1 * (X2-X1)),
  Cross_denom=(X2-X1),
  Cross_numer <= Y2*Cross_denom,
  Cross_numer >= Y1*Cross_denom.

ray_cross(point(X,Y), line_segment(polygon(X1,Y1), polygon(X2,Y2))) :-
  point(X,Y), polygon(X1,Y1), polygon(X2,Y2), not polygon(X,Y),
  line_segment(polygon(X1,Y1), polygon(X2,Y2)),
  X1 > X2, X <= X1, X >= X2,
  Cross_numer=((Y2-Y1) * (X - X1)) - (Y1 * (X2-X1)),
  Cross_denom=(X2-X1),
  Cross_numer >= Y2*Cross_denom,
  Cross_numer <= Y1*Cross_denom.

% Handle vertical lines
ray_cross(point(X,Y), line_segment(polygon(X,Y1), polygon(X,Y2))) :-
  point(X,Y), polygon(X,Y1), polygon(X,Y2), not polygon(X,Y),
  line_segment(polygon(X1,Y1), polygon(X2,Y2)),
  Y <= Y2.

% Count the number of line segements that the point's ray crosses.
cross_count(N, point(X,Y)) :-
  point(X,Y),
  N = {ray_cross(point(X,Y), line_segment(polygon(X1, Y1), polygon(X2, Y2))): line_segment(polygon(X1, Y1), polygon(X2,Y2))}.

% Determine if the point is inside by whether or not it crosses an even number
% of line segments.
inside(point(X,Y)) :- point(X,Y), cross_count(N, point(X,Y)), N\2=1.

% Ensure all points are inside the polygon.
:- not inside(point(X,Y)), point(X,Y).

% Minimize the number of points in the polygon.
:~ poly_count(N). [N]

#show polygon/2.
