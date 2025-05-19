# Use:
# clingo subset_sum.lp instance.lp -c n=<val> | python3 print/print.py
# to be ran in previous directory where subset_sum.lp and instance.lp are

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
if toks is not None:
    nums = [int(t[4:-1]) for t in toks]

    nums.sort()

    print(str(sum(nums)) + ' = ' + ' + '.join(str(n) for n in nums))

else:
    print("No solution found.")
