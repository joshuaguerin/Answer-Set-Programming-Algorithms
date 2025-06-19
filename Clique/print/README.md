# K-Clique & Max-Clique Printer

## Description
The printer takes input from standard input, and can be piped directly in from the program's output in Clingo.

## Arguments
There are no arguments, nor configurations necessary.

## Sample Output
Output prior to interpretation by graphviz is a `dot` file structure:

```
// Graph visualization using dot
strict graph {
    node [color=black]
    edge [color=black]

    1
    2
    3
    4
    5
    1 -- {2 3}
    2 -- {3 4 5}
    3 -- {4 5}
    4 -- 5

    subgraph cluster_0 {
        style=invis

        2 -- 5 [color=red]
        3 -- 5 [color=red]
        4 -- 3 [color=red]
        4 -- 2 [color=red]
        3 -- 2 [color=red]
        5 -- 4 [color=red]
        4 [color=red]
        2 [color=red]
        3 [color=red]
        5 [color=red]
    }
}
```

And the same graph when processed by `dot`:

![Provided Instance Output](images/6n-graf-clique.svg.png)
