# File: print.py
# Author: Michael Huelsman
# Created On: 04 Jun 2026
# Purpose:
#   A print function for viewing an instance and solution to a sat or max-sat problem
# Use:
# clingo sat.lp instance.lp | python3 print/print.py instance.lp > sat.html
# clingo sat.lp instance.lp | python3 print/print.py instance.lp > sat.html
#      where instance.lp contains clause predicates.
# Notes:

import argparse

def clause_literal_to_html(literal: int) -> str:
    html_str = f'x<sub>{abs(literal)}</sub>'
    if literal < 0:
        html_str = '&not;' + html_str
    return html_str

def main(args):
    # Parse instance
    instance = {}
    literals = set()
    with open(args.instance, 'r') as fin:
        lines = fin.read().split('\n')
        for line in lines:
            line = line.strip()
            if not line.startswith('clause'):
                continue
            clause, literal = line[7:].strip(').').split(',')
            clause = int(clause)
            literal = int(literal)
            if clause not in instance:
                instance[clause] = []
            instance[clause].append(literal)
            literals.add(abs(literal))
    # Parse SAT/MAX-SAT output
    solution = {}
    clingo_out = []
    clingo_out.append(input())
    while not clingo_out[-1].startswith('UNSATISFIABLE') and \
          not clingo_out[-1].startswith('SATISFIABLE') and \
          not clingo_out[-1].startswith('OPTIMUM'):
        clingo_out.append(input().strip())
    if clingo_out[-1].startswith('UNSATISFIABLE'):
        # Unsatisfiable formula
        solution = None
    elif clingo_out[-1].startswith('SATISFIABLE'):
        # SAT solution
        for assign in clingo_out[-2].split():
            if assign.startswith('true'):
                solution[int(assign[5:].strip(')'))] = True
            elif assign.startswith('false'):
                solution[int(assign[6:].strip(')'))] = False
    elif clingo_out[-1].startswith('OPTIMUM'):
        # MAX-SAT solution
        for assign in clingo_out[-3].split():
            if assign.startswith('true'):
                solution[int(assign[5:].strip(')'))] = True
            elif assign.startswith('false'):
                solution[int(assign[6:].strip(')'))] = False

    # HTML Document preamble
    preamble = \
        """
<html>
  <header>
    <style>
        .satisfied {color: red;}
        .unsatisfied {color: black;}
        .sat-highlight {background-color: #99ff99;}
    </style>
  </header>
  <body>
        """
    epilogue = \
        """
  </body>
</html>
        """
    print(preamble)
    # Render and output html for True/False literals
    if solution is None:
        # Unsatisfiable
        print("    <h1> UNSATISFIABLE </h1>")
    else:
        # Satisfiable
        print("    <h1> Truth Assignment </h1>")
        print("    <hr>")
        true_literals = []
        false_literals = []
        for literal in sorted(solution.keys()):
            if solution[literal]:
                true_literals.append(literal)
            else:
                false_literals.append(literal)
        print("    <p>")
        print("    <h3> True Literals </h3>")
        print("    <hr>")
        print("    <ul>")
        for literal in true_literals:
            print(f"    <li> x<sub>{literal}</sub> </li>")
        print("    </ul>")
        print("    <p>")
        print("    <h3> False Literals </h3>")
        print("    <hr>")
        print("    <ul>")
        for literal in false_literals:
            print(f"    <li> x<sub>{literal}</sub> </li>")
        print("    </ul>")

        # Render and output html for boolean formula w/ colored satisfied
        print("    <p><p><h1> Instance CNF Formula </h1>")
        print("    <hr><p>")
        clause_strs = []
        sat_count = 0
        # Render each clause
        for clause in sorted(instance.keys()):
            satisfied = False
            literals = []
            for literal in instance[clause]:
                if (literal > 0 and abs(literal) in true_literals) or \
                   (literal < 0 and abs(literal) in false_literals):
                    satisfied = True
                    lit_str = "<span class=satisfied>" + \
                              clause_literal_to_html(literal) + \
                              "</span>"
                else:
                    lit_str = "<span class=unsatisfied>" + \
                              clause_literal_to_html(literal) + \
                              "</span>"
                literals.append(lit_str)
            clause_str = "(" + " &or; ".join(literals) + ")"
            if satisfied:
                sat_count += 1
                clause_str = "<span class=sat-highlight>" + \
                             clause_str + \
                             "</span>"
            clause_strs.append(clause_str)
        # Render full formula
        print("    ", " &and; ".join(clause_strs))
        print(f"    <p>Clause SAT Count: {sat_count}")

    # HTML Document epilogue
    print(epilogue)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="SAT/MAX-SAT instance and solution generator")
    parser.add_argument('instance', type=str, help="File with the CNF formula instance in logic program form.")
    main(parser.parse_args())
