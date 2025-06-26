# Perfect Numbers Printer

## Description
The printer takes input from standard input, and can be piped directly in from the program's output in Clingo.

## Arguments
There are no arguments, nor configurations necessary.

## Implementational Details
Distribution of perfect numbers is rather sparse--there are only 4 such numbers in the range [1..10,000] (6, 28, 496, and 8,128). For the sake of simplicity and efficiency, results are hard-coded for the first 9 perfect numbers. While seemingly limiting, this should well exceed what the program is capable of generating in a reasonable amount of time[^1].

[^1]: The nineth number, 2658455991569831744654692615953842176, has nearly 40 digits.
