# Description: Creates dot code visualizable using graphviz.
#              Second line in 'Use' will create a pdf with the created graph.
#
# Use: clingo grandpa.lp instance.lp | python3 print/print.py | dot -Tpdf -o grandpa.pdf
#
# To be ran in previous directory where grandpa.lp and instance.lp are.


import re


toks = input().split()

while not toks[0].startswith("Answer:"):
    toks = input().split()

toks = input().split()

output = '''// Graph visualization using dot
digraph {
    node [color=black]
    edge [color=black,decorate=true]
    //splines=polyline

    ranksep=2
    { rank=min ; widow ; father; }
    //{ rank=same ; widows_daughter ; me }
    { rank=max ; bouncing_baby_boy ; son }

'''

for t in toks:
    ex_text = re.search(r"\(.*\)", t).group()[1:-1]

    if re.search(',', ex_text):
        nodes = ex_text.split(',')
    else:
        node = ex_text
    
    if t.startswith("married"):
        string1 = nodes[0] + ' -> ' + nodes[1] + ' [dir=both,label="Married",color=blue]\n'
        string2 = nodes[1] + ' -> ' + nodes[0] + ' [dir=both,label="Married",color=blue]\n'
        duplicate_check1 = re.search(re.escape(string1), output)
        duplicate_check2 = re.search(re.escape(string2), output)

        if not duplicate_check1 and not duplicate_check2:
            output += '    ' + nodes[0] + ' -> ' + nodes[1] + ' [dir=both,label="Married",color=blue]\n'
            
    elif t.startswith("parent"):
        string1 = nodes[0] + ' -> ' + nodes[1] + ' [label="Parent",color=darkgreen]\n'
        string2 = nodes[1] + ' -> ' + nodes[0] + ' [label="Parent",color=darkgreen]\n'
        duplicate_check1 = re.search(re.escape(string1), output)
        duplicate_check2 = re.search(re.escape(string2), output)

        if duplicate_check1:
            output = re.sub(re.escape(string1), nodes[0] + ' -> ' + nodes[1] + ' [dir=both,label="Parent",color=darkgreen]\n', output)

        elif duplicate_check2:
            output = re.sub(re.escape(string2), nodes[1] + ' -> ' + nodes[0] + ' [dir=both,label="Parent",color=darkgreen]\n', output)

        else:
            output += '    ' + nodes[0] + ' -> ' + nodes[1] + ' [label="Parent",color=darkgreen]\n'

    elif t.startswith("sibling"):
        string1 = nodes[0] + ' -> ' + nodes[1] + ' [dir=both,label="Siblings",color=green]\n'
        string2 = nodes[1] + ' -> ' + nodes[0] + ' [dir=both,label="Siblings",color=green]\n'
        duplicate_check1 = re.search(re.escape(string1), output)
        duplicate_check2 = re.search(re.escape(string2), output)

        if not duplicate_check1 and not duplicate_check2:
            output += '    ' + nodes[0] + ' -> ' + nodes[1] + ' [dir=both,label="Siblings",color=green]\n'

    elif t.startswith("uncle"):
        string1 = nodes[0] + ' -> ' + nodes[1] + ' [label="Uncle",color=orange]\n'
        string2 = nodes[1] + ' -> ' + nodes[0] + ' [label="Uncle",color=orange]\n'
        duplicate_check1 = re.search(re.escape(string1), output)
        duplicate_check2 = re.search(re.escape(string2), output)

        if duplicate_check1:
            output = re.sub(re.escape(string1), nodes[0] + ' -> ' + nodes[1] + ' [dir=both,label="Uncle",color=orange]\n', output)

        elif duplicate_check2:
            output = re.sub(re.escape(string2), nodes[1] + ' -> ' + nodes[0] + ' [dir=both,label="Uncle",color=orange]\n', output)

        else:
            output += '    ' + nodes[0] + ' -> ' + nodes[1] + ' [label="Uncle",color=orange]\n'

    elif t.startswith("grandparent"):
        output += '    ' + nodes[0] + ' -> ' + nodes[1] + ' [label="Grandparent",color=purple]\n'

    elif t.startswith("male"):
        # blue?
        output += '    ' + node + ' [shape=box,style=filled,fillcolor=lightblue]\n'

    elif t.startswith("female"):
        # pink?
        output += '    ' + node + ' [shape=ellipse,style=filled,fillcolor=pink]\n'

    elif t.startswith("grandpa"):
        output += '    ' + node + ' -> ' + node + ' [dir=both,taillabel="GRANDPA",labeldistance=8,labelangle=1,style=bold,color=red]\n'

print(output + '}')
