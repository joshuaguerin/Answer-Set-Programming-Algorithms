# Use:
# clingo bin_packing.lp instance.lp -c n=<val> | python3 print/print.py
#      where instance.lp contains item predicates.
#
# To be ran in previous directory where bin_packing.lp and instance.lp are.

import re


def draw_bin(contents, weight, itemSize):
    # Drawing Bin
    #output = "        Items\n"
    output = ""
    
    output += "        __" + ('_' * itemSize) + "__\n"

    for c in contents:
        output += "        | " + c + " |\n"

    output += "        --" + ('-' * itemSize) + "--\n"

    output += "     Weight: " + weight + "\n"

    return output

# Reading in clingo output
toks_last = None
toks = None
toks_next = input().split()

while not (toks_next[0].startswith("OPT") or toks_next[0].startswith("UNSAT")):
    toks_last = toks
    toks = toks_next
    toks_next = input().split()

toks = toks_last

# Generating Knapsack
if toks_next[0].startswith("OPT"):
    weights = {}
    bins = {}
    itemSizes = {}

    for t in toks:

        if "bin" in t:
            t = t[4:-1].split(',')

            try:
                bins[t[0]].append(t[1])

            except:
                bins[t[0]] = [t[1]]

            try:
                if len(t[0]) > itemSizes[t[0]]:
                    itemSizes[t[0]] = len(t[1])

            except:
                itemSizes[t[0]] = len(t[1])

        elif "weight" in t:
            t = t[7:-1].split(',')
            weights[t[0]] = t[1]

    binStrings = []
    for b in bins:
        binStrings.append(draw_bin(bins[b], weights[b], itemSizes[b]))

    output = "Bin Contents:\n"
    for b in binStrings:
        output += b + "\n"
        
    print(output)

elif toks_next[0].startswith("UNSAT"):
    print("No solution found.")
