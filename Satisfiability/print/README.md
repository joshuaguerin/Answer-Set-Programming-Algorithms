# SAT Printer

## Description
The printer takes input from standard input, and can be piped directly in from the program's output in Clingo. This printer outputs (to stdout) HTML describing the solution, if one exists.

## Arguments
Takes a single argument which is the instance file of the CNF formula that is given to Clingo. This program assumes that the instance file only contains clause predicates.

## Output Format
The HTML that is produced has three sections:

1. True Literals: List of literals assigned True
2. False Literals: List of literals assigned False
3. Instance CNF Formula: A rendering of the CNF formula the literals are associated with. Satisfied literals are highlighted in red, satisfied clauses are highlighted in green.

If the instance is not satisfied the HTML contains only the text UNSATISFIABLE.

If output is put into a file then it can be opened in any browser to see the results.

## Sample Usage
Assuming we have a proper instance in a file `instance.lp` and wish to put our output into a file called `sat.html` we would run the following line:

```
clingo sat.lp instance.lp | python3 print/print.py instance.lp > sat.html
```

For MAX-SAT the process is the same, except `max-sat.lp` is used instead of `sat.lp`

## Sample Output
In this section we explore output generated when MAX-SAT is ran using the provided `instance.lp` file.

Output:

```
<html>
  <header>
    <style>
        .satisfied {color: red;}
        .unsatisfied {color: black;}
        .sat-highlight {background-color: #99ff99;}
    </style>
  </header>
  <body>

    <h1> Truth Assignment </h1>
    <hr>
    <p>
    <h3> True Literals </h3>
    <hr>
    <ul>
    </ul>
    <p>
    <h3> False Literals </h3>
    <hr>
    <ul>
    <li> x<sub>1</sub> </li>
    <li> x<sub>2</sub> </li>
    </ul>
    <p><p><h1> Instance CNF Formula </h1>
    <hr><p>
     (<span class=unsatisfied>x<sub>1</sub></span> &or; <span class=unsatisfied>x<sub>2</sub></span>) &and; <span class=sat-highlight>(<span class=satisfied>&not;x<sub>1</sub></span> &or; <span class=unsatisfied>x<sub>2</sub></span>)</span> &and; <span class=sat-highlight>(<span class=unsatisfied>x<sub>1</sub></span> &or; <span class=satisfied>&not;x<sub>2</sub></span>)</span> &and; <span class=sat-highlight>(<span class=satisfied>&not;x<sub>1</sub></span> &or; <span class=satisfied>&not;x<sub>2</sub></span>)</span>
    <p>Clause SAT Count: 3
  </body>
</html>
```
