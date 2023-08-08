# Use:
# clingo instance.lp | python3 ./validate/print.py
# to be ran in previous directory where instance.lp is


def printGrid(grid):
    count=1
    for s in solution:
        for i in range(0, 9, 3):
            print('[', end='')
            print(s[i], s[i+1], s[i+2], sep=' ', end='] ')

        if count%3==0 and count != 9:
            print()
            
        count += 1
        print()

toks = input().split()

while not toks[0].startswith("Answer:"):
    toks = input().split()

toks = input().split()

solution = []
for i in range(9):
    solution.append([0]*9)

for t in toks:
    (fst, snd, thd) = t.split(',')
    fst = int(fst[6:])
    snd = int(snd)
    thd = int(thd[:-1])
    #print(fst, snd, thd)
    
    solution[fst-1][snd-1] = thd

    #print(solution)

printGrid(solution)



