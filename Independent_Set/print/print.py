# Use:
# clingo independent_set.lp instance.lp | python3 print/print.py -f f | dot -Tpdf -o independent_set.pdf
#      where instance.lp contains node and edge predicates.
#            f is the optional file that contains a graph's node and edge predicates (default = "instance.lp").
#
# Note:
#  The final pipe and call to dot can be omitted if graphviz is not present.
#  To be ran in previous directory where independent_set.lp and instance.lp are.


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

while not (toks_next and toks_next[0].startswith("OPT")):
    toks_last = toks
    toks = toks_next
    toks_next = input().split()

toks = toks_last

# Scripting graph
output = '''// Graph visualization using dot
strict graph {
    node [color=black]
    edge [color=black]

'''

if toks_next[0].startswith("OPT"):

    # Setting up graph
    for line in instance_lines:
        if line.startswith("node"):
            line = re.sub(r"node\(", "    ", line)
            line = re.sub(r"\)\.", "", line)

            output += line + "\n"
            
        elif line.startswith("edge"):
            line = re.sub(r"edge\(", "    ", line)
            line = re.sub(r"\)\.", ";", line)
            line = re.sub(r", ", " -- ", line)
            line = re.sub(r"\(", "{", line)
            line = re.sub(r"\)", "}", line)
            
            output += line

    # Adding solution to graph
    output += "\n"
    
    for t in toks:
        t = re.sub(r"set\(", "    ", t)
        t = re.sub(r"\)", " [style=filled,fillcolor=lightblue];", t)

        output += t + "\n"

    #output += "\n    }\n"

    print(output + "}\n")

# In case of unsatisfiability
elif toks_next[0].startswith("UNSAT"):
    print("No solution found.")
