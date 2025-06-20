# Use:
# clingo min_dominating_set.lp instance.lp | python3 print/print.py -f f | dot -Tpdf -o min_dominating_set.pdf
# clingo k_dominating_set.lp instance.lp -c n=<val> | python3 print/print.py -f f | dot -Tpdf -o k_dominating_set.pdf
#      where instance.lp contains node and edge predicates.
#            f is the optional file that contains a graph's node and edge predicates (default = "instance.lp").
#
# Note:
#  The final pipe and call to dot can be omitted if graphviz is not present.
#  To be ran in previous directory where min_dominating_set.lp, k_dominating_set, and instance.lp are.


import re
import argparse
import math


# Colors available
color = ["lightblue1", "tomato2", "lightgreen", "pink", "orange", "lightgoldenrod1", "lightgoldenrod4",
         "purple1", "lightgoldenrodyellow"]

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

while not (toks_next and toks_next[0].startswith("OPT") or toks_next[0].startswith("SAT") or toks_next[0].startswith("UNSAT")):
    toks_last = toks
    toks = toks_next
    toks_next = input().split()

# Scripting graph
output = '''// Graph visualization using dot
strict graph {
    node [color=black]
    edge [color=black]

'''

if toks_next[0].startswith("OPT") or toks_next[0].startswith("SAT"):
    if toks_next[0].startswith("OPT"):
        toks = toks_last
    
    # Setting up graph
    for line in instance_lines:
        if line.startswith("node"):
            line = re.sub(r"node\(", "    ", line)
            line = re.sub(r"\)\.", "", line)

            if ".." in line:
                constraints = re.findall(r"\d+", line)
                replacement = " ; ".join(str(i) for i in range(int(constraints[0]), int(constraints[1]) + 1))
                line = re.sub(r"\d+..\d+", replacement, line)
                
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

    nodeColoring = {}
    
    for t in toks:
        if t.startswith("num"):
            pass

        elif t.startswith("color"):
            data = re.findall(r"\d+", t)
            
            if data[1] in nodeColoring:
                nodeColoring[data[1]].append(data[0])

            else:
                nodeColoring[data[1]] = [data[0]]
    
    colorIndex = 0

    for coloring in nodeColoring:
        for node in nodeColoring[coloring]:

            output += "    " + node + " [style=filled,fillcolor=" + color[colorIndex] + "];\n"
            
        colorIndex = (colorIndex + 1) % len(color)

    output += "\n} // Coloring Number: " + str(len(nodeColoring))
    
    print(output + "\n")

# In case of unsatisfiability
elif toks_next[0].startswith("UNSAT"):
    print("No solution found.")
