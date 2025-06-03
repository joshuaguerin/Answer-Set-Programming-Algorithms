# ASP&#8704;: Answer Set Programming "Algorithms"

## What is ASP&#8704;
Pronounced "Answer Set Programming for all," this repository is designed to serve as a sort of online textbook or Open Educational Repository (OER) for Answer Set Programming, in particular in the [Clingo](https://potassco.org/clingo/) dialect. The universal quantifier, &#8704;, is an important symbol in logic programming, ascribing properties to *everything* of a particular type of atom in logic programming. The upside-down 'A' also serves to reinforce the sort of misnomer of the term "algorithms," as it may or may not apply to languages like Clingo.

In terms of overall design, our expected audiences are those who new to ASP and Clingo, but are looking to improve, and may be useful for those with an intermediate experience level as well. We hope that the overall structure will allow readers to learn ASP patterns "by example," to identify commonalities in program construction.

While the respository is open to anyone who wishes to learn ASP, the goals do not currently include dedicated instruction in the language's features. This is a goal of ours, but we believe it would be better expressed through a different project. So some fluency with logical/declarative languages, or the Clingo semantics is likely useful. There are certainly [existing options](https://teaching.potassco.org/) for learning a bit of the language and solver semantics.

### "Algorithms"
The term "Algorithms" doesn't really apply as the conventional algorithm is a description of a step-by-step process to find a solution to a particular problem. In a declarative language like an answer set language, the *algorithm* is more easily attributed to the solver. The program specified in the language dialect by the end-user is a model or description of the problem domain, including a description of a solution in the domain. In this case "patterns" may be a better description, but are easily conflated with conventional "design patterns" in software.

The inspiration (including the name) for the repository are the myriad of books with titles like "Algorithms in C++" or "Algorithms in Python," where the author's primary goal is to present implementations of conventional algorithms in the target language. We opted for a similar naming scheme in hopes of conveying a similar purpose for the repository as an educational tool, despite the largely non-algorithmic nature of solutions in the language.


## Organization
The repository  is designed around a "flat" organizational structure for ease of navigation, however problems in the repository are easily grouped into categories related to their type. The following table presents one such organizational structure, with problems in each category organized (roughly) by length or conceptual difficulty of the solution.

| Category  | Problems | Complexity |
| ------------- | ------------- | ------------- |
| Number Theory   | [Composite Numbers](Prime-Sieve)  |
|    | [Prime Sieve](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Prime-Sieve)  |
|    | [Perfect Numbers](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Perfect-Numbers)  |
| Numerical Set/Partitioning  | [Subset Sum](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Subset-Sum) | NP-Complete |
|  | [Equal Sum Partition](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Equal-Sum-Partition) | 
|  | [Numerical 3-Dimensional Matching](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Numerical-3-Dimensional-Matching) |
|  Combinatorial Optimization  |  [Knapsack](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Knapsack)  | NP-Complete |
|  | [Bin-Packing](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Bin-Packing) | NP-Complete |
|  Puzzles/Games  | [I'm my own Grandpa!](Grandpa/)  | N/A |
|    | [N-Queens](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/N-Queens) |
|    | [Sudoku](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Sudoku) | 
|  Graphs  | [Graph Coloring](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Graph-Coloring) | NP-Complete |
|    | [Chromatic Numbers](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Graph-Coloring) | NP-Hard |
|    | [Clique](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Clique) | NP-Complete |
|    | [Dominating Set](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Dominating-Set) | NP-Complete&#x2020; |
|    | [Independent Set](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Independent_Set) |
|    | [Vertex Cover](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Vertex-Cover) | 
|  Deterministic Planning  | [Hamiltonian Path](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Travelling_Salesman) | NP-Complete |
|    | [Traveling Salesman](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Travelling_Salesman) | NP-Hard |
| Sequential/Time-Based Planning | [Wolf, Goat, and Cabbage](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Wolf-Goat-Cabbage) | N/A |
|  Network Flow  | [Max-Flow](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Max-Flow) |
|  Data Mining  | [Clustering](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Clustering) |

Note that a directory may contain multiple solutions. E.g., The "standard" problem in NP-Complete and an optimization variant in NP-Hard. Such problems are labeled with a dagger (&#x2020;).

Additionally, some solutions are to purpose-built or contrived, single-purpose domains (e.g., [Grandpa](Grandpa) or [Wolf, Goat, and Cabbage](Wolf-Goat-Cabbage), which do not have a meaningful notion of "input size," (for which we will denote a N/A complexity).

## Structure
Entries are designed with a primary goal of comprehensibility for study. This is not to imply that solutions encountered will necessarily be slow in practice or deliberately inefficient. Instead we have designed solutions to be easy to understand and learn from, as articulating thoughts in a logical language may feel difficult at first.

Each problem entry contains, minimally, a description and example of the problem being solved (in the form of a `README.md` file), a problem instance file (data, usually called `instance.lp`), and a solution file (sharing the name of problem).

Additional resources are typically included on an as-needed basis including:
* Problem variants that are not sufficiently different to warrant separate inclusion (e.g., minimization/maximization variants).
* Generators to construct new instances (`gen` directory).
* Printing software (`print` directory).

Some of these features will be omitted where not applicable. E.g., [Prime-Sieve](Prime-Sieve)'s prime and composite sieves take a single integer, and thus domain/instance generation is not terribly useful to the reader. Unless otherwise stated, generation and printing software are likely written in Python.

Applications are designed under the assumptions of a standard Unix design philosophy of small, single-purpose programs that operate largely over standard input and output. This means that either individual applications can be called as-needed, and invocations can be pipelined using pipes and redirects. Example calls/suggested uses are included in the headers of each file (either `.lp` or `.py`).

## Use

Each implementation may have slight variations [1] on use (e.g., number of command-line arguments), we have maintained a fairly consistent interface throughout each entry. Clingo applications are divided into a separate `instance.lp` and `problem.lp` file, where the former holds the data for a specific problem instance and the latter contains the generalized solution. 

^[1]: Please see the header comment for individual files for more detailed use instructions.

In general, instance and problem files can be passed directly to Clingo:

```console
clingo instance.lp problem.lp
```

Output can be parsed by the reader either directly, or through an included printing script. In most instances, this can be accomplished through pipes:

```console
clingo instance.lp problem.lp | python3 print/print.py
```

When generating a problem instance for testing, the user may find file redirects useful, as they allow easy inspection of generated instances:

```console
python3 gen/generate.py > instance.lp
```



## Notes about implementations
The goal for this repo is to produce a set of original solutions to common/classical problems in Computer Science, however natural similarities are likely to exist between my own sources and those written by others. Of significant influence are the educational materials in the [Potassco](https://potassco.org/) collection, who are also the developers of clingo and other related solvers. Many programming conventions in this repository were learned from their materials and carry over directly.

### Prerequisites/Dependencies
Solution and instance files (`.lp`) are written for the [Clingo](https://potassco.org/clingo/) solver, from the [Potsdam](https://potassco.org/clingo/) Answer Set Solving Collection (Potassco).

Auxiliary software applications (e.g., generation and printing) are usually written in [Python 3](https://www.python.org/downloads/).

Finally, additional utilities may be used where appropriate. While efforts have been taken to ensure that required software packages are somewhat minimal, additional utilities may improve (for example) our ability to represent output.

E.g., Many graph algorithms do not have a natural/human readable means to display as plaintext or *ASCII art*. Thus, for convenience, [graphviz/dot](https://graphviz.org/download/) may be used as an output format by printers. This particular format was selected because it is roughly as comprehensible as any other text-based format, but users also have the option of running these outputs through dot to produce graphical documents (e.g., pdfs) for final output.


## Bugs and other issues
Our goal is to have solutions be well-documented, and fairly robust. While bugs are likely to be present, our hope is that the algorithms largely function under their defined parameters. If users discover bugs or other problems in our code, we welcome the user to submit an [issue](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/issues) that clearly defines the unexpected behavior so it may be fixed or better documented.

## How to Cite
For now, please cite the website by the name *ASP&#8704;: Answer Set Programming "Algorithms"* by "Joshua T. Guerin" with the full URL. You may use whatever citation conventions are most reasonable for the publication.

