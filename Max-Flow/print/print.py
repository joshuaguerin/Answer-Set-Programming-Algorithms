# Use:
# clingo max_flow.lp instance.lp | python3 print/print.py -f f | dot -Tpdf -o max_flow.pdf
#      where instance.lp contains node and edge predicates.
#            f is the optional file that contains a graph's node and edge predicates (default = "instance.lp").
#
# Note:
#  The final pipe and call to dot can be omitted if graphviz is not present.
#  To be ran in previous directory where max_flow.lp, and instance.lp are.


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

while not (toks_next[0].startswith("OPT")):
    toks_last = toks
    toks = toks_next
    toks_next = input().split()

toks = toks_last

# Scripting graph
output = '''// Graph visualization using dot
strict digraph {
    node [color=black]
    edge [color=black,dir=none]

'''

if toks_next[0].startswith("OPT"):

    # Setting up graph
    for line in instance_lines:
        if line.startswith("node"):
            line = re.sub(r"node\(", "    ", line)
            line = re.sub(r"\)\.", "", line)
            output += line + "\n"
            
        elif line.startswith("edge"):
            weight = re.findall(r"\d+", line)[0]

            line = re.sub(r"edge\(", "    ", line)
            line = re.sub(r", \d+\)\.", ";", line)
            line = re.sub(r", ", " -> ", line)
            line = re.sub(r";", " [label=\"" + weight + "\"];", line)
            output += line

    # Adding solution to graph
    output += '''\n
    subgraph cluster_0 {
        style=invis

'''

    for t in toks:
        weight = re.findall(r"\d+\)", t)[0][:-1]
        
        t = re.sub(r"flow\(", "        ", t)
        t = re.sub(r",\d+\)", " [temp]", t)
        t = re.sub(r",", " -> ", t)
        t = re.sub(r"\[temp\]", "[dir=yes,label=\"" + weight + "\"];", t)            

        tempt = t.split(" ")

        output = re.sub("    " + tempt[-2] + " -> " + tempt[-4] + r" \[.*?\];", "", output)

        output += t + "\n"

    output += "\n    }\n"

    print(output + "}\n")

# In case of unsatisfiability
elif toks_next[0].startswith("UNSAT"):
    print("No solution found.")
