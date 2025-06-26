# Use:
# clingo graph_coloring.lp instance.lp -c n=<val> | python3 print/print.py -f f | dot -Tpdf -o graph_coloring.pdf
# clingo chromatic_number.lp instance.lp | python3 print/print.py -f f | dot -Tpdf -o chromatic_number.pdf
#      where instance.lp contains node and edge predicates.
#            f is the optional file that contains a graph's node and edge predicates (default = "instance.lp").
#
# Note:
#  The number of colors available to use in the graphs are limited to 15 distinct colors, and a number of similar backup colors.
#  Differing shapes are being explored as an option to further distinguish coloring.
#  The final pipe and call to dot can be omitted if graphviz is not present.
#  To be ran in previous directory where graph_coloring.lp, chromatic_number.lp, and instance.lp are.


import re
import argparse
import random


# Colors available
color = ["lightblue1", "tomato2", "lawngreen", "pink", "orange", "lightgoldenrod1", "lightgoldenrod4",
         "purple", "blue1", "darkslategray", "dimgrey", "deeppink1", "palegreen4", "seashell", "red4"]

backupColors = ['aliceblue', 'antiquewhite', 'antiquewhite1', 'antiquewhite2', 'antiquewhite3', 'antiquewhite4', 'aqua', 'aquamarine', 'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure', 'azure1', 'azure2', 'azure3', 'azure4', 'beige', 'bisque', 'bisque1', 'bisque2', 'bisque3', 'bisque4', 'black', 'blanchedalmond', 'blue', 'blue2', 'blue3', 'blue4', 'blueviolet', 'brown', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadetblue', 'cadetblue1', 'cadetblue2', 'cadetblue3', 'cadetblue4', 'chartreuse', 'chartreuse1', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate', 'chocolate1', 'chocolate2', 'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflowerblue', 'cornsilk', 'cornsilk1', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'crimson', 'cyan', 'cyan1', 'cyan2', 'cyan3', 'cyan4', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgoldenrod1', 'darkgoldenrod2', 'darkgoldenrod3', 'darkgoldenrod4', 'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkolivegreen1', 'darkolivegreen2', 'darkolivegreen3', 'darkolivegreen4', 'darkorange', 'darkorange1', 'darkorange2', 'darkorange3', 'darkorange4', 'darkorchid', 'darkorchid1', 'darkorchid2', 'darkorchid3', 'darkorchid4', 'darkred', 'darksalmon', 'darkseagreen', 'darkseagreen1', 'darkseagreen2', 'darkseagreen3', 'darkseagreen4', 'darkslateblue', 'darkslategray1', 'darkslategray2', 'darkslategray3', 'darkslategray4', 'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deeppink2', 'deeppink3', 'deeppink4', 'deepskyblue', 'deepskyblue1', 'deepskyblue2', 'deepskyblue3', 'deepskyblue4', 'dimgray', 'dodgerblue', 'dodgerblue1', 'dodgerblue2', 'dodgerblue3', 'dodgerblue4', 'firebrick', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'gold1', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'green2', 'green3', 'green4', 'greenyellow', 'gray89', 'gray9', 'gray90', 'honeydew3', 'honeydew4', 'hotpink', 'hotpink1', 'hotpink2', 'hotpink3', 'hotpink4', 'indianred', 'indianred1', 'indianred2', 'indianred3', 'indianred4', 'indigo', 'invis', 'ivory', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavenderblush', 'lavenderblush1', 'lavenderblush2', 'lavenderblush3', 'lavenderblush4', 'lemonchiffon', 'lemonchiffon1', 'lemonchiffon2', 'lemonchiffon3', 'lemonchiffon4', 'lightblue', 'lightblue2', 'lightblue3', 'lightblue4', 'lightcoral', 'lightcyan', 'lightcyan1', 'lightcyan2', 'lightcyan3', 'lightcyan4', 'lightgoldenrod', 'lightgoldenrod2', 'lightgoldenrod3', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightpink1', 'lightpink2', 'lightpink3', 'lightpink4', 'lightsalmon', 'lightsalmon1', 'lightsalmon2', 'lightsalmon3', 'lightsalmon4', 'lightseagreen', 'lightskyblue', 'lightskyblue1', 'lightskyblue2', 'lightskyblue3', 'lightskyblue4', 'lightslateblue', 'lightslategray', 'lightslategrey', 'lightsteelblue', 'lightsteelblue1', 'lightsteelblue2', 'lightsteelblue3', 'lightsteelblue4', 'lightyellow', 'lightyellow1', 'lightyellow2', 'lightyellow3', 'lightyellow4', 'lime', 'limegreen', 'linen', 'magenta', 'magenta1', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumorchid1', 'mediumorchid2', 'mediumorchid3', 'mediumorchid4', 'mediumpurple', 'mediumpurple1', 'mediumpurple2', 'mediumpurple3', 'mediumpurple4', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose', 'mistyrose1', 'mistyrose2', 'mistyrose3', 'mistyrose4', 'moccasin', 'navajowhite', 'navajowhite1', 'navajowhite2', 'navajowhite3', 'navajowhite4', 'navy', 'navyblue', 'none', 'oldlace', 'olive', 'olivedrab', 'olivedrab1', 'olivedrab2', 'olivedrab3', 'olivedrab4', 'orange1', 'orange2', 'orange3', 'orange4', 'orangered', 'orangered1', 'orangered2', 'orangered3', 'orangered4', 'orchid', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'palegoldenrod', 'palegreen', 'palegreen1', 'palegreen2', 'palegreen3', 'paleturquoise', 'paleturquoise1', 'paleturquoise2', 'paleturquoise3', 'paleturquoise4', 'palevioletred', 'palevioletred1', 'palevioletred2', 'palevioletred3', 'palevioletred4', 'papayawhip', 'peachpuff', 'peachpuff1', 'peachpuff2', 'peachpuff3', 'peachpuff4', 'peru', 'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 'plum4', 'powderblue', 'purple1', 'purple2', 'purple3', 'purple4', 'rebeccapurple', 'red', 'red1', 'red2', 'red3', 'rosybrown', 'rosybrown1', 'rosybrown2', 'rosybrown3', 'rosybrown4', 'royalblue', 'royalblue1', 'royalblue2', 'royalblue3', 'royalblue4', 'saddlebrown', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandybrown', 'seagreen', 'seagreen1', 'seagreen2', 'seagreen3', 'seagreen4', 'seashell1', 'seashell2', 'seashell3', 'seashell4', 'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'silver', 'skyblue', 'skyblue1', 'skyblue2', 'skyblue3', 'skyblue4', 'slateblue', 'slateblue1', 'slateblue2', 'slateblue3', 'slateblue4', 'slategray', 'slategray1', 'slategray2', 'slategray3', 'slategray4', 'slategrey', 'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'springgreen', 'springgreen1', 'springgreen2', 'springgreen3', 'springgreen4', 'steelblue', 'steelblue1', 'steelblue2', 'steelblue3', 'steelblue4', 'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'teal', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato1', 'tomato3', 'tomato4', 'transparent', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet', 'violetred', 'violetred1', 'violetred2', 'violetred3', 'violetred4', 'webgray', 'webgreen', 'webgrey', 'webmaroon', 'webpurple', 'wheat', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white', 'whitesmoke', 'x11gray', 'x11green', 'x11grey', 'x11maroon', 'x11purple', 'yellow', 'yellow1', 'yellow2', 'yellow3', 'yellow4', 'yellowgreen']

random.shuffle(backupColors)
color += backupColors

# Reading in graph
parser = argparse.ArgumentParser()

parser.add_argument('-f', default = "instance.lp", type = str,
                    help = "File (filename.lp) with the graph's node and edge predicates. (Default = instance.lp)")

args = parser.parse_args()

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
