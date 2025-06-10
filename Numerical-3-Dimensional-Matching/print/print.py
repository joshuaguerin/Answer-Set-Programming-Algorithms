# Use:
# clingo numerical_3_dimensional_matching.lp instance.lp -c n=<val> | python3 print/print.py
#      where instance.lp contains predicates enumerating x, y, and z.
#
# To be ran in previous directory where numerical_3_dimensional_matching.lp and instance.lp are.


import re


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
    print("Triples found:")
    
    for t in toks:
        nums = re.findall(r'\d+', t)
        print(sum(int(n) for n in nums), '= ' + ' + '.join(nums))
