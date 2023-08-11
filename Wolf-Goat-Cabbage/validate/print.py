# Use:
# clingo instance.lp | python3 ./validate/print.py
# to be ran in previous directory where instance.lp is




toks = input().split()

while not toks[0].startswith("Answer:"):
    toks = input().split()

toks = input().split()

left = []
right = []
boat = []

for t in toks:
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
    elif t[0:2] == "bo":
        (fst, snd) = t.split(',')
        fst = fst[5:]
        snd = int(snd[:-1])
        boat[snd] = fst
        
    #(fst, snd, thd) = t.split(',')
    
    # fst = int(fst[7:])
    # snd = int(snd)
    # thd = int(thd[:-1])
    #print(fst, snd, thd)

    #print(solution)

#printGrid(solution)

# for i in range(len(left)):
#     if 'x' in left[i]:
#         left[i].pop('x')
#     if 'x' in right[i]:
#         right[i].pop('x')

for i in range(len(left)):
    print("Time: ", i, left[i], end=' ')
    # print("Time: ", i, " left:", left[i], end=' ')
    
    if 'f' in right[i]:
        print("<", boat[i], right[i])
    else:
        print(boat[i], ">", right[i])

        
    # if 'f' in right[i]:
    #     print("<", boat[i], "right:", right[i])
    # else:
    #     print(boat[i], ">", "right:", right[i])
