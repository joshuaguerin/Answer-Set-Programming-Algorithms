# Use:
# clingo instance.lp wolf_goat_cabbage.lp -c n=7 | python3 ./validate/print.py
# to be ran in previous directory where instance.lp is

toks = input().split()

while not toks[0].startswith("Answer:"):
    toks = input().split()

toks = input().split()

left = []
right = []
boat = []

# Process predicates
for t in toks:
    # put elements left and right
    if t[0:2] == "at":
        (fst, snd, thd) = t.split(',')
        fst = fst[3:]
        thd = int(thd[:-1])

        while thd+1 > len(left) or thd+1 > len(right) or thd+1 > len(boat):
            left.append([])
            right.append([])
            boat.append(' ')
            #print(len(left), len(right))

        if snd == 'l' and fst != 'x':
            left[thd].append(fst)
        elif snd == 'r' and fst != 'x':
            right[thd].append(fst)
            
        #print(fst, snd, thd)
    # store bot information
    elif t[0:2] == "bo":
        (fst, snd) = t.split(',')
        fst = fst[5:]
        snd = int(snd[:-1])
        boat[snd] = fst
        

# Print state at each timestep
for i in range(len(left)):
    print("Time: ", i, left[i], end=' ')
    
    if 'f' in right[i]:
        print("<", boat[i], right[i])
    else:
        print(boat[i], ">", right[i])

