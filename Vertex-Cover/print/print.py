# Use:
# clingo k_vertex_cover.lp instance.lp -c n=<val> | python3 print/print.py | dot -Tpdf -o images/vertex_cover.pdf
# clingo min_vertex_cover.lp instance.lp | python3 print/print.py | dot -Tpdf -o images/vertex_cover.pdf
#      where instance.lp contains node and edge predicates.
#
# Note:
#  The final pipe and call to dot can be omitted if graphviz is not present.
#  To be ran in previous directory where instance.lp, k_clique.lp, and max_clique.lp are.


import re


output = '''// Graph visualization using dot
strict graph {
    node [color=black]
    edge [color=black]

'''

# Reading in graph
instance = open("instance.lp", "r")
instance_lines = instance.readlines()

for line in instance_lines:
    if line.startswith("node"):
        
        line = re.sub(r"node\(", "    ", line)
        line = re.sub(r" ; ", " ", line)
        line = re.sub(r"\).", "\n", line)

        output += line
    
    elif line.startswith("edge"):
        
        line = re.sub(r"edge\(", "    ", line)
        line = re.sub(r", ", " -- ", line)
        
        if " (" in line:
            line = re.sub(r" \(", " {", line)
            line = re.sub(r"\)\).", "}", line)

        else:
            line = re.sub(r"\).", "", line)

        output += line
        
instance.close()

# Reading in clingo output
toks_last = None
toks = None
toks_next = input().split()

while not (toks_next[0].startswith("SAT") or toks_next[0].startswith("UNSAT") or toks_next[0].startswith("OPT")):
    toks_last = toks
    toks = toks_next
    toks_next = input().split()

if toks_next[0].startswith("SAT") or toks_next[0].startswith("OPT"):
    if toks_next[0].startswith("OPT"):
        toks = toks_last

    output += '''
    subgraph cluster_0 {
        style=invis

'''
    
    for t in toks:
        output += "        " + t[6:-1] + " [color=red,shape=doubleoctagon]\n"

    output += "\n    }\n"
                
    print(output + "}\n")

elif toks_next[0].startswith("UNSAT"):
    print("No solution found.")
