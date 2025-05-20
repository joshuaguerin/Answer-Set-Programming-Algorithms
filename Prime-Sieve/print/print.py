# Use:
# clingo <prime/composite>.lp -c n=<max> | python3 print/print.py
#
# To be ran in previous directory where prime.lp and composite.lp are.

toks = input().split()

while not toks[0].startswith("Answer:"):
    toks = input().split()

toks = input().split()

if len(toks) == 0:
    print("None found.")

else:
    if toks[0].startswith("prime"):
        print("Primes found: ", end='')
        nums = [int(t[6:-1]) for t in toks]
    else:
        print("Composites found: ", end='')
        i = 10
        nums = [int(t[10:-1]) for t in toks]

    nums.sort()
        
    print(", ".join(str(n) for n in nums))

