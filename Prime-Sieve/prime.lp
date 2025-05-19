%*
 * File: prime.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given an integer n, compute primes from 2..n
 * Use: clingo prime.lp -c n=<max>
 *      where primes between 2..max are to be generated.
 *%

num(2..n).

composite(X) :- num(X), num(Y), X\Y==0, X!=Y.

prime(N) :- num(N), not composite(N).

#show prime/1.
