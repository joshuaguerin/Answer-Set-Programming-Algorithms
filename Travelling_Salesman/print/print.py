# Use:
# clingo hamiltonian_path.lp instance.lp -c s=<val> -c e=<val> | python3 print/print.py -f f | dot -Tpdf -o hamiltonian_path.pdf
# clingo travelling_salesman.lp instance.lp -c s=<val> -c e=<val> | python3 print/print.py -f f | dot -Tpdf -o hamiltonian_path.pdf
#      where instance.lp contains node and edge predicates.
#            f is the optional file that contains a graph's node and edge predicates (default = "instance.lp").
#
# Note:
#  The final pipe and call to dot can be omitted if graphviz is not present.
#  To be ran in previous directory where hamiltonian_path.lp, travelling_salesman.lp, and instance.lp are.


import re
import argparse
import math


parser = argparse.ArgumentParser()

parser.add_argument('-f', default = "instance.lp", type = str,
                    help = "File (filename.lp) with the graph's node and edge predicates. (Default = instance.lp)")

args = parser.parse_args()

# Reading in graph
instance = open(args.f, "r")
instance_lines = instance.readlines()
instance.close()

# Reading in clingo output
toks_last = None
toks = None
toks_next = input().split()

while not (toks_next[0].startswith("SAT") or toks_next[0].startswith("UNSAT") or toks_next[0].startswith("OPT")):
    toks_last = toks
    toks = toks_next
    toks_next = input().split()

# Scripting graph
output = '''// Graph visualization using dot
strict digraph {
    node [color=black]
    edge [color=black,dir=none]

'''
    
if toks_next[0].startswith("SAT") or toks_next[0].startswith("OPT"):

    # Setting up graph
    for line in instance_lines:
        if line.startswith("node"):
            line = re.sub(r"node\(", "    ", line)
            line = re.sub(r"\)\.", "", line)
    
        elif line.startswith("edge"):
            weight = re.findall(r"\d+", line)[0]
            
            line = re.sub(r"edge\(", "    ", line)
            line = re.sub(r", \d+\)\.", ";", line)
            line = re.sub(r", ", " -> ", line)

            if toks_next[0].startswith("OPT"):
                line = re.sub(r";", " [label=\"" + weight + "\"];", line)
                
        output += line

    # Adding solution to graph
    output += '''
    subgraph cluster_0 {
        style=invis

'''

    if toks_next[0].startswith("OPT"):
        toks = toks_last
        
    for t in toks:
        weight = re.findall(r"\d+", t)[0]
        
        t = re.sub(r"path\(", "        ", t)
        t = re.sub(r",\d+\)", " [temp]", t)
        t = re.sub(r",", " -> ", t)

        if toks_next[0].startswith("OPT"):
            t = re.sub(r"\[temp\]", "[color=red,dir=yes,label=\"" + weight + "\"];", t)            
            tempt = t.split(" ")
            output = re.sub("    " + tempt[-2] + " -> " + tempt[-4] + r" \[.*?\];", "", output)

        else:
            t = re.sub(r"\[temp\]", "[color=red,dir=yes];", t)
            tempt = t.split(" ")
            output = re.sub("    " + tempt[-2] + " -> " + tempt[-4] + ";", "", output)
        
        output += t + "\n"
            
    output += "\n    }\n"
                
    print(output + "}\n")

# In case of unsatisfiability
elif toks_next[0].startswith("UNSAT"):
    print("No solution found.")
