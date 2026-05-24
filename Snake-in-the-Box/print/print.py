# Use:
# clingo snake-in-the-box.lp -c n=<n> | python3 print/print.py -n <n> | dot -Tpdf -o snake-in-the-box.pdf
#  Both n in the snake-in-the-box execution and in print.py must be the same.
#  To be ran in previous directory where snake-in-the-box.lp is contained.


# Set up for highlighting the specific path.
path_edges = set()

# Reading in clingo output
clingo_out = []
clingo_out.append(input().split())

while clingo_out[-1][0] != 'OPTIMUM':
    clingo_out.append(input().split())
    if len(clingo_out) > 3:
        clingo_out.pop(0)

dim = -1

for token in clingo_out[0]:
    if token.startswith('path'):
        u, v = map(int, token.removeprefix('path').strip('()').split(','))
        edge = (v, u)
        if u < v:
            edge = (u, v)
        path_edges.add(edge)
    elif token.startswith('dim'):
        dim = int(token.removeprefix('dim').strip('()'))

edges = set()
if dim > 0:
    # Generate base graph
    for i in range(2**dim):
        for j in range(dim):
            u, v = i, i^(1 << j)
            if u < v:
                edges.add((u, v))
            else:
                edges.add((v, u))
    # Output the graph
    output = ['// Graph visualization via dot.', 'graph H {', '\tnode [color=black];', '\tedge [color=black];']
    for edge in sorted(edges):
        if edge not in path_edges:
            output.append(f"\t{edge[0]} -- {edge[1]};")
        else:
            output.append(f"\t{edge[0]} -- {edge[1]} [color=\"red\"];")

    for line in output:
        print(line)
    print('}')
    print(f"// Path length: {len(path_edges)}")
