# Use:
# clingo k_clique.lp instance.lp -c n=<val> | python3 print/print.py | dot -Tpdf -o clique.pdf
# clingo max_clique.lp instance.lp | python3 print/print.py | dot -Tpdf -o clique.pdf
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
        nums = re.findall(r'\d+', line)

        for n in nums:
            output += "    " + n + "\n"
    
    elif line.startswith("edge"):
        nums = re.findall(r'\d+', line)

        if len(nums) == 2:
            output += "    " + nums[0] + " -- " + nums[1] + "\n"

        else:
            output += "    " + nums[0] + " -- {" + " ".join(nums[1:]) + "}\n"

instance.close()

# Reading in clingo output
toks_last = None
toks = None
toks_next = input().split()

while not (toks_next[0].startswith("SAT") or toks_next[0].startswith("UNSAT") or toks_next[0].startswith("OPT")):
    toks_last = toks
    toks = toks_next
    toks_next = input().split()

if toks_next[0].startswith("OPT"):
    toks = toks_last
    toks.pop() # This erases the number from "count(n)"

if toks_next[0].startswith("UNSAT"):
    print("No solution found.")
    
else:
    output += '''
    subgraph cluster_0 {
        style=invis

'''
    
    for t in toks:
        nums = re.findall(r'\d+', t)

        if len(nums) == 1:
            output += "        " + nums[0] + " [color=red]\n"

        elif len(nums) == 2:
            output += "        " + nums[0] + " -- " + nums[1] + " [color=red]\n"

    print(output + "    }\n}\n")
