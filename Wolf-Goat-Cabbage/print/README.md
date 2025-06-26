# Wolf, Goat, and Cabbage Problem Printer

## Description
The printer takes input from standard input, and can be piped directly in from the program's output in Clingo.

## Arguments
There are no arguments, nor configurations necessary.

## Output

When ran with a parameter of n=7:

```
Time:  0 ['f', 'w', 'g', 'c'] g > []
Time:  1 ['c', 'w'] <   ['g', 'f']
Time:  2 ['c', 'w', 'f'] c > ['g']
Time:  3 ['w'] < g ['c', 'g', 'f']
Time:  4 ['g', 'w', 'f'] w > ['c']
Time:  5 ['g'] <   ['c', 'w', 'f']
Time:  6 ['g', 'f'] g > ['c', 'w']
Time:  7 [] <   ['f', 'w', 'g', 'c']
```
