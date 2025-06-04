# Use:
# clingo equal_sum_partition.lp instance.lp | python3 print/print.py
#
# To be ran in previous directory where equal_sum_partition.lp and instance.lp are.


def get_input():
    toks = input().split()

    while not toks[0].startswith("Answer:"):
        if toks[0].startswith("UNSATISFIABLE"):
            return None
        toks = input().split()

    toks = input().split()
    return toks

toks = get_input()

# output
if toks is None:
    print("No solution found.")
    
else:
    total = ''
    a = []
    b = []
    
    for t in toks:
        if t[0] == 'a':
            a.append(t[2:-1])

        elif t[0] == 'b':
            b.append(t[2:-1])
        
        elif total == '':
            total = t[8:-1]

    print("\nEqual Sums Found!\n\n" +
          "Full set:\nS = {" + ', '.join(list(map(str, sorted(set(map(int, a + b)))))) + "}\n\n" +
          "Set A: {" + ', '.join(a) + "}\n" +
          total + " = " + ' + '.join(a) + "\n\n"
          "Set B: {" + ', '.join(b) + "}\n" +
          total + " = " + ' + '.join(b))
