

% Passenger list may include nothing (x).
passenger(w ; g ; c ; x).


% Initial configuration:
% at(who, side, timestep).
% All passengers must start at the left.
at(f, l, 0).
at(w, l, 0).
at(g, l, 0).
at(c, l, 0).
at(x, l, 0).
at(x, r, 0).