# Use:
# clingo n_queens.lp | python3 ./print/print.py
# to be ran in previous directory where n_queens.lp is


def printGrid(coords, n):
    grid = []
    for i in range(n):
        grid.append([' ']*n)

    for (a, b) in coords:
        # print(a, b)
        grid[a-1][b-1] = 'Q'
        
    for g in grid:
        print(g)

toks = input().split()

while not toks[0].startswith("Answer:"):
    if toks[0] == "UNSATISFIABLE":
        print("UNSATISFIABLE")
        exit()
        
    toks = input().split()

toks = input().split()

bound = 0

solution = []

for t in toks:
    (fst, snd) = t.split(',')
    fst = int(fst[7:])
    snd = int(snd[:-1])
    #print(fst, snd)

    bound = fst if fst>bound else bound
    bound = snd if snd>bound else bound
    
    solution.append((fst, snd))

#print(solution)

printGrid(solution, bound)
