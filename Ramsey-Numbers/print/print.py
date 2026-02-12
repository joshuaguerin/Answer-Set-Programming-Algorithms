# Use:
# clingo search.lp -c k=<int> -c r=<int> -c s=<int> | python3 print/print.py | dot -Tpdf -o search.pdf
# Note:
#  The final pipe and call to dot can be omitted if graphviz is not present.
#  To be ran in previous directory where instance.lp, k_clique.lp, and max_clique.lp are.


import sys

raw = []

# Make a copy of stdin
for line in sys.stdin:
    raw.append(line)

# No solution
if "UNSATISFIABLE\n" in raw:
    print("UNSAT", file=sys.stderr)
    exit()

# First solution located.
index = raw.index("Answer: 1\n")+1
toks = raw[index].split()

# Parse the output
edges = []
red = []
blue = []
clique = []

# Collect relevant data.
for t in toks:
    if t[0:4] == "colo" and ',' in t:
        # Edge color
            (fst, snd, color) = t.split(',')

            fst = int(fst[6:])
            snd = int(snd)
            color = color[0:-1]

            if fst < snd:
                edges.append((fst, snd, color))

    elif t[0:3] == "red":
        t = int(t[4:-1])
        red.append(t)
        
    elif t[0:4] == "blue":
        t = int(t[5:-1])
        blue.append(t)
                
    
# Print to graphviz format.
header = '''
graph {
   rankdir=LR;
'''
print(header)

# Print node properties
for b in blue:
    if not b in red:
        print("   ", b, "[color=\"dodgerblue3\", fontcolor=\"white\", style=\"filled\"];")
    else:
        print("   ", b, "[color=\"dodgerblue3:firebrick3\", fontcolor=\"white\", style=\"filled\"];")

for r in red:
    if not r in blue:
        print("   ", r, "[color=\"red\", fontcolor=\"white\", style=\"filled\"];")

# Print edges, with associated properties
for(fst, snd, color) in edges:
    if color == "blue":
        color = "dodgerblue3"
    else:
        color = "firebrick3"
        
    if fst in blue and snd in blue or fst in red and snd in red:
        print("   ", fst, "--", snd, "[color=\"", color, "\", penwidth=3]", sep='')
    else:
        print("   ", fst, "--", snd, "[color=\"", color, "\"]", sep='')
    

# Finishing up
footer= '''
}
'''

print(footer)
            
