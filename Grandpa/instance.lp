
%% Known relationships from the song.
% male gender
male(me).
male(father).
male(bouncing_baby_boy).

% female gender
female(widow).
female(widows_daughter).

% initail parents relations
parent(father, me).
parent(widow, widows_daughter).
parent(me, bouncing_baby_boy).
parent(widows_daughter, bouncing_baby_boy).
parent(widows_daughter, son).

% initial marriages
married(me, widow).
married(father, widows_daughter).

