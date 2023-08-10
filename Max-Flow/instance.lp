
% Example from CLRS
node(s ; t ; a ; b ; c ; d).

start(s).
terminal(t).

% edge(start, end, capacity)
edge(s, a, 11). edge(s, c, 12).
edge(a, b, 12).
edge(c, a, 1). edge(c, d, 11).
edge(b, t, 19).
edge(d, b, 7). edge(d, t, 4).