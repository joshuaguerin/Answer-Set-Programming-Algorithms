# Use:
# clingo perfect_numbers.lp -c n=<max> | python3 print/print.py
#
# To be ran in previous directory where prime.lp and composite.lp are.


toks = input().split()

while not toks[0].startswith("Answer:"):
    toks = input().split()

toks = input().split()

if len(toks) == 0:
    print("None found.")

else:
    nums = [int(t[8:-1]) for t in toks]
    
    nums.sort()

    print("Perfect Numbers: " + ", ".join(str(n) for n in nums))
