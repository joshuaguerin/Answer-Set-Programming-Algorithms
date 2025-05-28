# Use:
# clingo perfect_numbers.lp -c n=<max> | python3 print/print.py
#
# To be ran in previous directory where perfect_numbers.lp is.


import collections
import re


toks = input().split()

while not toks[0].startswith("Answer:"):
    toks = input().split()

toks = input().split()

if len(toks) == 0:
    print("None found.")

else:
    num_dict = collections.defaultdict(list)
    
    for t in toks:
        n = re.findall(r'\d+', t)

        if len(n) == 2:
            num_dict[int(n[1])].append(int(n[0]))

    nums = sorted(num_dict.items())

    print("Perfect Numbers:")

    spacing = '                 '
    for item in nums:
        print('%20d = %s' % (item[0], ' + '.join(str(i) for i in item[1])))
    
