# ASP&#8704;: Answer Set Programming "Algorithms"

## What is ASP&#8704;
Pronounced "ASP for all," this repository is designed to serve as a sort of online textbook or Open Educational Repository (OER) for Answer Set Programming, in particular in the [Clingo](https://potassco.org/clingo/) dialect. The universal quantifier, &#8704;, is an important symbol in logic programming, ascribing properties to *everything* of a particular type of atom in logic programming. The upside-down 'A' also serves to reinforce the sort of misnomer of the term "algorithms," as it may or may not apply to languages like Clingo.

In terms of overall design, our expected audiences are those who new to ASP and Clingo, but are looking to improve, and may be useful for those with an intermediate experience level as well. We hope that the overall structure will allow readers to learn ASP patterns "by example," to identify commonalities in program construction.

While the respository is open to anyone who wishes to learn ASP, the goals do not currently include dedicated instruction in the language's features. This is a goal of ours, but we believe it would be better expressed through a different project. So some fluency with logical/declarative languages, or the Clingo semantics is likely useful. There are certainly [existing options](https://teaching.potassco.org/) for learning a bit of the language and solver semantics.

### "Algorithms"
You are absolutely correct! The term really doesn't apply based on the definition of an algorithm in Computer Science. "Patterns" or "implementations" may be better, but don't really have a solid sound to them. I needed *something* to call the repo, and I'm modeling the idea off the myriad of books out there with titles like "Algorithms in C++" or "Algorithms in Python." What I'm going for is essentially similar to the purposes of those books--just in a language that isn't inherently algorithmic.

## Organization
While I am opting for a flat directory organization at the moment for ease of navigation, one possible organization of the problems for the reader could be:

| Category  | Problems | Complexity |
| ------------- | ------------- | ------------- |
| Number Theory   | [Composite Numbers](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Prime-Sieve)  |
|    | [Prime Sieve](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Prime-Sieve)  |
|    | [Perfect Numbers](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Perfect-Numbers)  |
| Numerical Set/Partitioning  | [Subset Sum](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Subset-Sum) |
|  | [Equal Sum Partition](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Equal-Sum-Partition) |
|  | [Numerical 3-Dimensional Matching](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Numerical-3-Dimensional-Matching) |
|  Combinatorial Optimization  |  [Knapsack](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Knapsack)  |
|  | [Bin-Packing](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Bin-Packing) |
|  Puzzles/Games  | [I'm my own Grandpa!](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/grandpa/Grandpa) |
|    | [N-Queens](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/N-Queens) |
|    | [Sudoku](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Sudoku) |
|  Graphs  | [Graph Coloring](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Graph-Coloring)
|    | [Chromatic Numbers](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Graph-Coloring)
|    | [Clique](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Clique) |
|    | [Dominating Set](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Dominating-Set) |
|    | [Independent Set](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Independent_Set) |
|    | [Vertex Cover](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Vertex-Cover) |
|  Deterministic Planning  | [Hamiltonian Path](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Travelling_Salesman) |
|    | [Traveling Salesman](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Travelling_Salesman) |
| Sequential/Time-Based Planning | [Wolf, Goat, and Cabbage](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Wolf-Goat-Cabbage) |
|  Network Flow  | [Max-Flow](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Max-Flow) |
|  Data Mining  | [Clustering](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/tree/master/Clustering) |

The organization of this table is design to roughly correspond with relative difficulty level of each problem/implementation.

## Note about implementations
The goal for this repo is to produce a set of original solutions to common/classical problems in Computer Science, however natural similarities are likely to exist between my own sources and those written by others. I've been influenced greatly over the course of my own studies by the educational resources provided by the good folks over at [Potassco](https://potassco.org/). Many of the conventions in my coding carry over from theirs, and similar authors. Additionally, ASP solutions tend to be much smaller than other conventional programming languages. Many NP-Complete or NP-Hard problems can be solved in <10 lines (often <5) of actual code. Variations are likely to exist, however it is entirely likely to have two authors describe the same basic ideas/constraints in their code.

## Bugs and other issues
Oh, yea, there will be bugs. It's going to be a while before I'm comforatble enough to label anything as being "done." Assume that everything here is experimental--prone to incorrectness or breakage. Having said that, I'm trying to upload mostly correct code even before I get to thorough testing ;) With that in mind, I would be thrilled if anyone found benefit in reading the examples I've produced here.

I will be using the [Issues](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/issues) page to keep organized in terms of progress, bugs, and future ideas for the page.

If you find a bug or want to chat feel free to hit us up! If you discover any untracked bugs, discussion points, or want to request a solution to a problem please feel free to add or comment on an [Issue](https://github.com/joshuaguerin/Answer-Set-Programming-Algorithms/issues).

## Future updates
We would like to consider this repository something of a "living document," continuing to add content in the form of new problems/solutions, utilities, and other information that the user may find useful. The frequency of updates is TBD, but we wish for this to be useful as an OER for ASP going into the future.

## How to Cite
For now, please cite the website by the name *ASP&#8704;: Answer Set Programming "Algorithms"* by "Guerin, Joshua" with the full URL. You may use whatever citation conventions are most reasonable for the publication.

