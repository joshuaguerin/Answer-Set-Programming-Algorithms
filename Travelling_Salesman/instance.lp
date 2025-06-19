% DEFINE
% s=a, e=d should generate a path of length 62.

% Vertex list.
node(a ; b ; c ; d).

% Edge list.
edge(a, b, 20). edge(a, c, 42). edge(a, d, 35).
edge(b, c, 30). edge(b, d, 34).
edge(c, d, 12).
