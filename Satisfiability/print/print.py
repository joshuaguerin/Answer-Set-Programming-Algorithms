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


#def main():

        
if __name__ == '__main__':
    solution = {}
    clingo_out = []
    count = -1
    
    # Retrieve Input
    clingo_out.append(input())
    
    while not clingo_out[-1].startswith('UNSATISFIABLE') and \
          not clingo_out[-1].startswith('SATISFIABLE') and \
          not clingo_out[-1].startswith('OPTIMUM'):
        clingo_out.append(input().strip())


    # Locate any special cases
    if clingo_out[-1].startswith('UNSATISFIABLE'):
        # Unsatisfiable formula
        solution = None
        exit()
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
            elif assign.startswith('sat_clause'):
                current = int(assign[11:].strip(')'))
                count = current if current > count else count

    # Print True and False assigned literals.
    if solution is None:
        # Unsatisfiable
        print("UNSATISFIABLE")
        exit()
    else:
        # Satisfiable
        true_literals = []
        false_literals = []
        for literal in sorted(solution.keys()):
            if solution[literal]:
                true_literals.append(literal)
            else:
                false_literals.append(literal)

        # Print valuation
        print("True  literals: ", end='')
        for literal in true_literals:
            print("x", literal, sep='', end=' ')
        print()

        print("False literals: ", end='')
        for literal in false_literals:
            print("x", literal, sep='', end=' ')
        print()

        if count != -1:
            print("Clauses Satisfied: ", count)
