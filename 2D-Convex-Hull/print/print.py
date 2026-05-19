#!/usr/bin/env python3

import argparse
import re
import sys

parser = argparse.ArgumentParser()



parser.add_argument(
    '-f',
    type=str,
    help="file (filename.lp) with the clingo output. (default = instance.lp)")


args = parser.parse_args()
doRead = True



if args.f == None:
    instance_lines = sys.stdin.read().splitlines()
    doRead = False
try:
    if doRead:
        with open(args.f, "r") as f:
            instance_lines = [line.strip() for line in f.readlines()]
    else:
        assert instance_lines != None

except FileNotFoundError:
    print(f"error: could not open file {args.f}")
    sys.exit(1)



# check for satisfiability
isSAT = "SATISFIABLE" in instance_lines
if not isSAT:
    print("no solution found (UNSATISFIABLE or incomplete log).")
    sys.exit(0)



sol_str = ""
for i, line in enumerate(instance_lines):
    if line == "SATISFIABLE" and i > 0:
        idx = i - 1
        while idx >= 0:
            if "on_hull" in instance_lines[idx] or "point" in instance_lines[idx]:
                sol_str = instance_lines[idx]
                break
            idx -= 1
        break
if not sol_str:
    print("could not find the answer predicates in the file.")
    sys.exit(1)


# graph visualization using graphviz (render with: neato -n2 -Tpng input.dot -o output.png)
output = '''// 
strict graph {
    layout=neato
    node [shape=circle, style=filled, fillcolor="#45475A", color="#BAC2DE", fontcolor="#CDD6F4", fontname="JetBrains Mono"]
    edge [color="#6C7086"]
'''
# Track hull nodes to process styling


hull_points = set()
all_points = set()
for chunk in sol_str.split(" "):
    chunk = chunk.strip()
    
    if not chunk:
        continue
    
    hull_match = re.match(r"on_hull\((\d+),(\d+)\)", chunk)
    
    if hull_match:
        x, y = hull_match.group(1), hull_match.group(2)
        node_id = f"p_{x}_{y}"
        hull_points.add((node_id, x, y))
        continue
    point_match = re.match(r"point\((\d+),(\d+)\)", chunk)
    
    if point_match:
        x, y = point_match.group(1), point_match.group(2)
        node_id = f"p_{x}_{y}"
        all_points.add((node_id, x, y))


for node_id, x, y in all_points:
    label = f"({x},{y})"
    output += f'    {node_id} [label="{label}", pos="{float(x)/2.0},{float(y)/2.0}!"];\n'

output += "\n    // Convex Hull highlights\n"



for node_id, x, y in hull_points:
    output += f'    {node_id} [fillcolor="#F38BA8", color="#F38BA8", fontcolor="#1E1E2E"];\n'


output += "}\n"
print(output)


