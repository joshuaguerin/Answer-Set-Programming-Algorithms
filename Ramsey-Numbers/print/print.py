# Use:
# clingo ramsey.lp -c k=<int> -c r=<int> -c s=<int> | python3 print/print.py | dot -Tpdf -o ramsey.pdf
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

for t in toks:
    if t[0:4] == "edge":
        (fst, snd) = t.split(',')
        fst = int(fst[5:])
        snd = int(snd[0:-1])
        if fst < snd:
            edges.append((fst, snd))
    # clique
    else:
        (fst, snd) = t.split(',')
        fst = int(fst[7:])
        snd = snd[0:-1]
        if snd=="red":
            red.append(fst)
        else:
            blue.append(fst)

# Print to graphviz format.
header = '''
graph {
   rankdir=LR;
'''
print(header)

for b in blue:
    print("   ", b, "[color=\"blue\"];")

for r in red:
    print("   ", r, "[color=\"red\"];")

for(fst, snd) in edges:
    if fst in blue and snd in blue:
        print("   ", fst, "--", snd, "[color=\"blue\"]", sep='')
    elif fst in red and snd in red:
        print("   ", fst, "--", snd, "[color=\"red\"]", sep='')
    else:
        print("   ", fst, "--", snd, "[color=\"black\"]", sep='')

footer= '''
}
'''

print(footer)
            
