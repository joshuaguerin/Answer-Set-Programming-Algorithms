
%    1---2
%    |\ /|
%    | 3 |
%    |/ \|
%    4---5

node(1..5).

% For a concise representation, edges can be directed in the description.
edge(1, (2 ; 3 ; 4)).
edge(2, (3 ; 5)).
edge(3, (4 ; 5)).
edge(4, 5).
