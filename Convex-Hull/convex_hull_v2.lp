
point(0,0 ; 0,4 ; -4,0 ; 5,0 ; 0,-6 ; 1,0).
% Solution: (-4, 0), (5, 0), (0, -6), (0, 4)

3 {polygon(X,Y): point(X,Y)} N :- N = {point(X,Y)}.

subtriangle(polygon(X1,Y1), polygon(X2,Y2), polygon(X3,Y3)) :-
    polygon(X1,Y1), polygon(X2,Y2), polygon(X3,Y3),
    {polygon(X1,Y1);polygon(X2,Y2);polygon(X3,Y3)} = 3.

inside(point(X,Y), subtriangle(polygon(X1,Y1), polygon(X2,Y2), polygon(X3,Y3))) :-
    point(X,Y), subtriangle(polygon(X1,Y1), polygon(X2,Y2), polygon(X3,Y3)),
    S1=((X2-X1)*(Y1-Y))-((X1-X)*(Y2-Y1)),
    S2=((X3-X2)*(Y2-Y))-((X2-X)*(Y3-Y2)),
    S3=((X1-X3)*(Y3-Y))-((X3-X)*(Y1-Y3)),
    S1>=0, S2>=0, S3>=0.

inside(point(X,Y), subtriangle(polygon(X1,Y1), polygon(X2,Y2), polygon(X3,Y3))) :-
    point(X,Y), subtriangle(polygon(X1,Y1), polygon(X2,Y2), polygon(X3,Y3)),
    S1=((X2-X1)*(Y1-Y))-((X1-X)*(Y2-Y1)),
    S2=((X3-X2)*(Y2-Y))-((X2-X)*(Y3-Y2)),
    S3=((X1-X3)*(Y3-Y))-((X3-X)*(Y1-Y3)),
    S1<=0, S2<=0, S3<=0.


inside(X,Y) :- 
    point(X,Y), subtriangle(polygon(X1,Y1), polygon(X2,Y2), polygon(X3,Y3)),
    inside(point(X,Y), subtriangle(polygon(X1,Y1), polygon(X2,Y2), polygon(X3,Y3))).

inside(X,Y) :- polygon(X,Y).

:- point(X,Y), not inside(X,Y).

:~ N = {polygon(X,Y)}. [N]

#show polygon/2.
