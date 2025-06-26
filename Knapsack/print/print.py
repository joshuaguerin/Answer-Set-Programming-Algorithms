# Use:
# clingo knapsack.lp instance.lp -c n=<val> | python3 print/print.py
#      where instance.lp contains item predicates.
#
# To be ran in previous directory where knapsack.lp and instance.lp are.

import re


# Reading in clingo output
toks_last = None
toks = None
toks_next = input().split()

while not (toks_next[0].startswith("OPT")):
    toks_last = toks
    toks = toks_next
    toks_next = input().split()

toks = toks_last

# Generating Knapsack
if toks_next[0].startswith("OPT"):
    weight = ''
    value = ''
    count = ''
    contents = []

    valueSize = 0
    weightSize = 0
    
    for t in toks:

        if "knapsack" in t:
            t = re.findall(r'\d+', t)
            contents.append(t)
            
            if len(t[0]) > valueSize:
                valueSize = len(t[0])

            if len(t[1]) > weightSize:
                weightSize = len(t[1])   

        elif "weight" in t:
            weight = t[7:-1]

        elif "value" in t:
            value = t[6:-1]
        
        elif "count" in t:
            count = t[6:-1]

    # Drawing Knapsack
    output = "Knapsack Contents:\n       Value" + (' ' * (valueSize + 1)) + "Weight\n"
            
    output += "        __" + ('_' * valueSize) + "____" + ('_' * weightSize) + "__\n"

    for c in contents:
        output += "        | " + c[0] + "    " + (' ' * (valueSize - len(c[0]))) + c[1] + " |\n"

    output += "        --" + ('-' * valueSize) + "----" + ('-' * weightSize) + "--\n"

    output += "  Totals: " + value + "    " + (' ' * (valueSize - len(c[0]))) + weight + "\n"
    
    print(output)

elif toks_next[0].startswith("UNSAT"):
    print("No solution found.")
