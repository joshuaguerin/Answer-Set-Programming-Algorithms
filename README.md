# ASP&#8704;: Answer Set Programming "Algorithms"

ASP&#8704; is a repository of solutions to common problems in Computer Science implemented in the logical/declarative [Answer Set Programming](https://en.wikipedia.org/wiki/Answer_set_programming) (ASP) paradigm in the [Clingo](https://potassco.org/clingo/) dialect. In particular, we focus on computationally difficult problems, including well-known problems in [NP-Complete](https://en.wikipedia.org/wiki/NP-completeness) and [NP-Hard](https://en.wikipedia.org/wiki/NP-hardness). These problems have no known efficient solutions, highlighting the expressive power and efficiency of the solvers in this language family.

We hope that this repository serves as a means for educators and learners alike to be inspired and grow their appreciation for the logic programming paradigm.

## What is ASP&#8704;?
Pronounced "Answer Set Programming for all," this repository is designed to serve as a sort of online textbook or Open Educational Repository (OER) for Answer Set Programming, in particular in the [Clingo](https://potassco.org/clingo/) dialect. The [universal quantifier](https://en.wikipedia.org/wiki/Universal_quantification), &#8704;, is an important symbol in logic (programming), ascribing properties to *everything* of a particular type or set (hence, "for all") of atom in logic programming. The upside-down 'A' also serves to reinforce the sort of misnomer of the term "algorithms," as it may or may not apply to languages like the language of Clingo.

In terms of overall design, our expected audiences are those who new to ASP and Clingo, but are looking to improve, and may be useful for those with an intermediate experience level as well. We hope that the overall structure will allow readers to learn ASP patterns "by example," to identify commonalities in program construction.

While the respository is open to anyone who wishes to learn ASP, the goals do not currently include dedicated instruction in the language or paradigm's primitives or basic features. This is a goal of ours, but we believe it would be better expressed through a different project. So some fluency with logical/declarative languages, or the Clingo semantics is likely useful. There are certainly [existing options](https://teaching.potassco.org/) for learning a bit of the language and solver semantics.

### "Algorithms"
The term "Algorithm" arguably doesn't apply directly to implementations as the conventional algorithm is a description of a step-by-step process to find a solution to a particular problem. In a declarative language like an answer set language, the *algorithm* is more easily attributed to the solver. The program specified in the language dialect by the end-user is a model or description of the problem domain, including a description of a solution in the domain. In this case "patterns" may be a better description, but are easily conflated with conventional "design patterns" in software.

The inspiration (including the name) for the repository are the myriad of books with titles like "Algorithms in C++" or "Algorithms in Python," where the author's primary goal is to present implementations of conventional algorithms in the target language. We opted for a similar naming scheme in hopes of conveying a similar purpose for the repository as an educational tool, despite the largely non-algorithmic nature of solutions in the language.

### Guiding Philosophies

This repository is an expression of enjoyment of logic programming by those who value high-quality educational materials. At the time of the repository's construction, there are several high-quality texts in logic programming (including answer set programming), however few available texts address the particular "Algorithms in" niche. As our goals are primarily educational, software examples are constructed under the following assumptions:

* Simple, well-organized/documented examples.
* Inclusion of a wide-variety of well-studied problems.
* Problem documentation, with examples.
* Additional utilities (where needed) to support understanding.

While efficiency of our solutions isn't a primary guiding concern, we encourage the user to push the limits of our implementations--you may be surprised regarding what some of them may accomplish in (in many instances) 2-5 lines of code! Keep in mind that, due to the largely $NP-Complete$ and $NP-Hard$ complexity classes most examples occupy, the fastest (known) algorithms for many of these problems are exponential or worse. At the most extreme end, some of our implementations may be usable for dozens/hundreds/thousands of inputs. 

The inclusion of additional software is multi-purpose. First, this allows us to provide solutions to problems that are encoded fairly strictly in the logical/ASP paradigm, with non-declarative (sometimes called "impure") notions such as input parsing and output generation moved to different portions of the toolchain. [^2]

[^2]: These elements could be incorporated more directly using [built-in support for](https://potassco.org/clingo/python-api/5.4/) for languages like Python, however we have opted for the simplicity of small toolchains over multi-language aggregate programs.

## Organization
The repository  is designed around a "flat" organizational structure for ease of navigation, however problems in the repository are easily grouped into categories related to their type. The following table presents one such organizational structure, with problems in each category organized (roughly) by length or conceptual difficulty of the solution.

| Category  | Problems |
| ------------- | ------------- |
| Number Theory   | [Composite Numbers](Prime-Sieve)  |
|    | [Prime Sieve](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Prime-Sieve)  |
|    | [Perfect Numbers](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Perfect-Numbers)  |
| Numerical Set/Partitioning  | [Subset Sum](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Subset-Sum) |
|  | [Equal Sum Partition](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Equal-Sum-Partition) | 
|  | [Numerical 3-Dimensional Matching](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Numerical-3-Dimensional-Matching) |
|  Combinatorial Optimization  |  [Knapsack](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Knapsack)  |
|  | [Bin-Packing](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Bin-Packing) |
|  Puzzles/Games  | [I'm my own Grandpa!](Grandpa/)  |
|    | [N-Queens](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/N-Queens) |
|    | [Sudoku](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Sudoku) | 
|  Graphs  | [Graph Coloring](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Graph-Coloring) |
|    | [Chromatic Numbers](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Graph-Coloring) |
|    | [Clique](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Clique) |
|    | [Max Clique](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Clique) |
|    | [Dominating Set](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Dominating-Set) |
|    | [Minimum Dominating Set](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Dominating-Set) |
|    | [Independent Set](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Independent_Set) |
|    | [Vertex Cover](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Vertex-Cover) | 
|    | [Minimum Vertex Cover](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Vertex-Cover) | 
|  Deterministic Planning  | [Hamiltonian Path](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Travelling_Salesman) |
|    | [Traveling Salesman](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Travelling_Salesman) |
| Sequential/Time-Based Planning | [Wolf, Goat, and Cabbage](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Wolf-Goat-Cabbage) |
|  Network Flow  | [Max-Flow](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Max-Flow) |


## Structure
Entries are designed with a primary goal of comprehensibility for study. This is not to imply that solutions encountered will necessarily be slow in practice or deliberately inefficient. Instead we have designed solutions to be easy to understand and learn from, as articulating thoughts in a logical language may feel difficult at first.

Each problem entry contains, minimally, a description and example of the problem being solved (in the form of a `README.md` file), a problem instance file (data, usually called `instance.lp`), and a solution file (sharing the name of problem).

Additional resources are typically included on an as-needed basis including:
* Problem variants that are not sufficiently different to warrant separate inclusion (e.g., minimization/maximization variants).
* Generators to construct new instances (`gen` directory).
* Printing software (`print` directory).

Some of these features will be omitted where not applicable. E.g., [Prime-Sieve](Prime-Sieve)'s prime and composite sieves take a single integer, and thus domain/instance generation is not terribly useful to the reader. Unless otherwise stated, generation and printing software are written in Python.

Applications are designed under the assumptions of a standard Unix design philosophy of small, single-purpose programs that operate largely over standard input and output. This means that either individual applications can be called as-needed, and invocations can be pipelined using pipes and redirects. Example calls/suggested uses are included in the headers of each file (either `.lp` or `.py`).

## Use

Each implementation may have slight variations [^1] on use (e.g., number of command-line arguments), we have maintained a fairly consistent interface throughout each entry. Clingo applications are divided into a separate `instance.lp` and `problem.lp` file, where the former holds the data for a specific problem instance and the latter contains the generalized solution. 

[^1]: Please see the header comment for individual files for more detailed use instructions, including any necessary command-line arguments.

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

