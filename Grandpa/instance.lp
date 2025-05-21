
%% Known relationships from the song.
% male gender
male(me).
male(dad).
male(bouncing_baby_boy).

% female gender
female(widow).
female(widows_daughter).

% initail parents relations
parent(dad, me).
parent(widow, widows_daughter).
parent(dad, bouncing_baby_boy).
parent(widows_daughter, bouncing_baby_boy).

% initial marriages
married(me, widow).
married(dad, widows_daughter).

