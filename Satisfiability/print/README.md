# SAT Printer

## Description
The printer takes input from standard input, and can be piped directly in from the program's output in Clingo. This printer outputs (to stdout) a text description the solution, if one exists.

## Arguments
There are no arguments, nor configurations necessary.

## Output Format
Using the provided `instance.lp` we have

`sat.lp`:
```
True  literals: x2 
False literals: x1 x3 x4 
```

`max-sat.lp`:

```
True  literals: x1 x4 
False literals: x2 x3 
Clauses Satisfied:  3
```

If the instance is not satisfied the HTML contains only the text UNSATISFIABLE.

## Sample Usage
Assuming we have a proper instance in a file `instance.lp` and wish to put our output into a file called `sat.html` we would run one of the following lines:

```
clingo sat.lp instance.lp | python3 print/print.py
clingo max-sat.lp instance.lp | python3 print/print.py
```
