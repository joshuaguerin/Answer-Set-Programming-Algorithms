# ASP&#8704;: Answer Set Programming "Algorithms"

ASP&#8704; is a repository of solutions to common problems in Computer Science implemented in the logical/declarative [Answer Set Programming](https://en.wikipedia.org/wiki/Answer_set_programming) (ASP) paradigm in the [Clingo](https://potassco.org/clingo/) dialect. In particular, we focus on computationally difficult problems, including well-known problems in [NP-Complete](https://en.wikipedia.org/wiki/NP-completeness) and [NP-Hard](https://en.wikipedia.org/wiki/NP-hardness). These problems have no known efficient solutions, highlighting the expressive power and efficiency of the solvers in this language family.

We hope that this repository serves as a means for educators and learners alike to be inspired and grow their appreciation for the logic programming paradigm.

## What is ASP&#8704;?
Pronounced "Answer Set Programming for all," this repository is designed to serve as an Open Educational Repository (OER) for Answer Set Programming, in particular in the [Clingo](https://potassco.org/clingo/) dialect. The [universal quantifier](https://en.wikipedia.org/wiki/Universal_quantification), &#8704;, is an important symbol in logic (programming), ascribing properties to *everything* of a particular type or set (hence, "for all") of atom in logic programming. The upside-down 'A' also serves to reinforce the sort of misapplication of the term "algorithms," as it may or may not apply to languages like the language of Clingo.

In terms of overall design, our expected audiences are those who new to ASP and Clingo, but are looking to start or improve learning, and may be useful for those with an intermediate experience level as well. We hope that the overall structure will allow readers to learn ASP patterns "by example," to identify commonalities in program construction.

While the respository is open to anyone who wishes to learn ASP, the goals do not currently include dedicated instruction in the language or paradigm's primitives or basic features. This is a goal of ours, but we believe it would be better expressed through a different project. Some fluency with logical/declarative languages, or the Clingo semantics is likely useful prior to getting started. There are certainly [existing options](https://teaching.potassco.org/) for learning a bit of the language and solver semantics.

### "Algorithms"
The term "Algorithm" arguably doesn't apply directly to implementations as the conventional algorithm is a description of a step-by-step process to find a solution to a particular problem. In a declarative language like an answer set language, the *algorithm* is more easily attributed to the solver. The program specified in the language dialect by the end-user is a model or description of the problem domain, including a description of a solution in the domain. In this case "patterns" may be a better description, but are easily conflated with conventional "design patterns" in software.

The inspiration (including the name) for the repository are the myriad of books with titles like "Algorithms in C++" or "Algorithms in Python," where the author's primary goal is to present implementations of conventional algorithms in the target language. We opted for a similar naming scheme in hopes of conveying a similar purpose for the repository as an educational tool, despite the largely non-algorithmic nature of solutions in the language.

### Guiding Philosophies

This repository is an expression of enjoyment of logic programming by those who value high-quality educational materials. At the time of the repository's construction, there are several great texts in logic programming (including answer set programming), however few available texts address the particular "Algorithms in" niche. As our goals are primarily educational, software examples are constructed under the following assumptions:

* Simple, well-organized/documented examples.
* Inclusion of a wide-variety of well-studied problems.
* Problem documentation, with examples.
* Additional utilities (where needed) to support understanding.

While efficiency of our solutions isn't a primary guiding concern, we encourage the user to push the limits of our implementations--you may be surprised regarding what some of them may accomplish in (in many instances) 2-5 lines of code! Keep in mind that, due to the largely $NP-Complete$ and $NP-Hard$ complexity classes most examples occupy, the fastest (known) algorithms for many of these problems are exponential or worse. At the most extreme end, some of our implementations may be usable for dozens/hundreds/thousands of inputs. 

The inclusion of additional software is multi-purpose. First, this allows us to provide solutions to problems that are encoded fairly strictly in the logical/ASP paradigm, with non-declarative (sometimes called "impure") notions such as input parsing and output generation moved to different portions of the toolchain. [^2] Additionally, we hope that these additional utilities will help the user in their journey of understanding how to program in the ASP paradigm. The seapration of functionalities with ASP languages can be rather extreme (s.t. input parsing and output formatting aren't even a part of the base language). Because purley predicate-based output (e.g., `attribute(atom)`) can prove difficult to parse for many problems--especially with larger instances.

By providing an end-to-end toolchain, from problem generation to solving to presentation, we hope that we have created a toolset that is flexible, comprehensible, and easy to modify and apply to new domains.

[^2]: These elements could be incorporated more directly using [built-in support for](https://potassco.org/clingo/python-api/5.4/) for languages like Python, however we have opted (for the simplicity) for small toolchains over larger, monolithic applications that aggregate multiple languages/paradigms.


## Organization
The repository  is designed around a "flat" organizational structure for ease of navigation, however problems in the repository are easily grouped into categories related to their type. The following table presents one such organizational structure, with problems in each category organized (roughly) by length or conceptual difficulty of the solution.

| Category  | Problems |
| ------------- | ------------- |
| Number Theory   | [Composite Numbers](Prime-Sieve)  |
|    | [Prime Sieve](Prime-Sieve)  |
|    | [Perfect Numbers](Perfect-Numbers)  |
| Numerical Set/Partitioning  | [Subset Sum](Subset-Sum) |
|  | [Equal Sum Partition](Equal-Sum-Partition) | 
|  | [Numerical 3-Dimensional Matching](Numerical-3-Dimensional-Matching) |
|  Combinatorial Optimization  |  [Knapsack](Knapsack)  |
|  | [Bin-Packing](Bin-Packing) |
|  Puzzles/Games  | [I'm my own Grandpa!](Grandpa)  |
|    | [N-Queens](N-Queens) |
|    | [Sudoku](Sudoku) | 
|  Graphs  | [Graph Coloring](Graph-Coloring) |
|    | [Bipartite Graph Partitioning](Graph-Coloring#problem-variants) |
|    | [Chromatic Numbers](Graph-Coloring) |
|    | [Clique](Clique) |
|    | [Max Clique](Clique) |
|    | [Dominating Set](Dominating-Set) |
|    | [Minimum Dominating Set](Dominating-Set) |
|    | [Independent Set](Independent_Set) |
|    | [Vertex Cover](Vertex-Cover) | 
|    | [Minimum Vertex Cover](Vertex-Cover) | 
|  Deterministic Planning  | [Hamiltonian Path](Travelling_Salesman) |
|    | [Traveling Salesman](Travelling_Salesman) |
| Sequential/Time-Based Planning | [Wolf, Goat, and Cabbage](Wolf-Goat-Cabbage) |
|  Network Flow  | [Max-Flow](Max-Flow) |

Regarding this structure, the reader will note that entries in the list do not necessarily correspond to unique directories. This is a delibereate attempt to simplify overall structure, while still fully enumerating the problems that are addressed.

In several instances we seek to consolodate similar functionalities into the same location. This is selected based on interrelationships between problems and similarities in the constructed solutions. I.e., Where [Hamiltonian Path](Travelling_Salesman) and [Traveling Salesman](Travelling_Salesman) are indeed different problems, from the perspective of the ASP solution there is remarkably little change to arrive at one from the other[^2]--the addition of weights, where appropriate, and a minimization statement. In a few instances, dissimilarly named problems are actually equivalent (e.g., [Bipartite Graph Partitioning](Graph-Coloring#problem-variants) vs. [2-Colorability](Graph-Coloring)), and hence do not even require additional implementation. In such instances we have crafted a narrative flow in our problem descriptions to highlight the similarities between the problems, and identify differences (if any) in their solutions.

[^2]: This highlights an interesting property of ASP solutions to computational problems. Being *descriptive* in nature, the similarities in solutions is most closely related to similarities in problem structure. In other paradigms, algorithmic approaches may differ significantly.

## Structure
Entries are designed with a primary goal of being correct/complete, but comprehensible for study. This is not to imply that solutions encountered will necessarily be slow in practice or deliberately inefficient. Instead we have designed solutions to be easy to understand and learn from, as articulating thoughts in a logical language may feel difficult (or foreign) at first. Solutions are designed around reasoning that is easily expressed in human-readable thoughts, and these expressions are used to document the narrative flow of each program. Indeed, most examples were developed around the expression of problem constraints in plain English, with lines of code engineered to make those thoughts salient.

Each problem entry contains, minimally, a description and example of the problem being solved (in the form of a `README.md` file), a problem instance file (data, usually called `instance.lp`), and a solution file (reflecting the name of problem with an `.lp` extension).

Additional resources are typically included on an as-needed basis including:
* Problem variants that are not sufficiently different to warrant separate directories (e.g., minimization/maximization variants may take no more than a single line).
* Generators to construct random instances for testing (`gen/`).
* Printing software (`print/`).

Some of these features will be omitted where not applicable. E.g., [Prime-Sieve](Prime-Sieve)'s prime and composite sieves take a single integer, and thus domain/instance generation is not terribly useful to the reader. Unless otherwise stated, generation and printing software are written in Python.

Applications are designed under the assumptions of a standard Unix design philosophy of small, single-purpose programs that operate largely over standard input and output. This means that either individual applications can be called as-needed, and invocations can be pipelined using pipes and redirects. Example calls/suggested uses are included in the headers of each file (either `.lp` or `.py`).

## Use

While each implementation may have slight variations [^1] on use (e.g., number and form of command-line arguments), we have sought to maintain a fairly consistent interface throughout each entry. Clingo applications are divided into a separate `instance.lp` and `problem.lp` file, where the former holds the data for an example problem instance and the latter contains the generalized solution. Problem instances supplied are designed as "toy" instances, so that the user can draw examples out by hand and verify results without the support of a computer.

[^1]: Please see the header comment for individual files for more detailed use instructions, including any necessary command-line arguments.

In general, instance and problem files can be passed directly to Clingo:

```console
clingo instance.lp problem.lp
```

Output can be parsed by the user either directly/visually, or through an included printing script. In most instances, this can be accomplished through pipes:

```console
clingo instance.lp problem.lp | python3 print/print.py
```

When generating a problem instance for testing, the user may find file redirects useful, as they allow easy inspection of generated instances:

```console
python3 gen/generate.py > instance.lp
```

## Notes about implementations
The goal for this repository is to produce a set of original solutions to common/classical problems in Computer Science, however natural similarities are likely to exist between my own sources and those written by others. Of significant influence are the educational materials in the [Potassco](https://potassco.org/) collection, who are also the developers of clingo and other related utilities. Many programming conventions in this repository were learned from their materials and carry over directly.

### Prerequisites/Dependencies

#### Clingo
Solution and instance files (`.lp`) are written for the [Clingo](https://potassco.org/clingo/) solver, from the [Potsdam](https://potassco.org/clingo/) Answer Set Solving Collection (Potassco). The binary is rather small, and can easily be installed in the cloned repository directory or a system binary directory.

#### Python
Auxiliary software applications (e.g., generation and printing) are usually written in [Python 3](https://www.python.org/downloads/).

#### Graphviz
Finally, additional utilities may be used where appropriate. While efforts have been taken to ensure that required software packages are somewhat minimal, additional utilities may improve (for example) our ability to represent output. In the case of many implementations we have opted for text-based representations of output figures.

This adds a small complication for graph problems, as graphical models lack a convenient, text-based form for display of results. Thus, for convenience, [graphviz/dot](https://graphviz.org/download/) may be used as an output format by printers. This particular format was selected because it is roughly as comprehensible as any other text-based format, but users also have the option of running these outputs through dot to produce graphical documents (e.g., pdfs) for final output.


## Bugs and other issues
We wish to present solutions that are correct, well-documented, and fairly robust (not to mention efficient, where possible!). We hope is that the solutions presented function under their defined parameters, however with a project of this size unintended behaviors are naturally going to be discovered. If any such problems, bugs, or or areas that require further documentation are discovered we welcome the reader to submit [issue](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/issues) that clearly defines the unexpected behavior so it may be fixed or better documented. Where possible please try to provide inputs, outputs, and any relevant source to expedite our ability to review any suggestions.

## How to Cite
For now, please cite the website by the name *ASP&#8704;: Answer Set Programming "Algorithms"* by "Joshua T. Guerin" with the full URL. You may use whatever citation conventions are most reasonable for the publication.

