%*
 * File: perfect.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given an integer n, compute primes from 2..n
 * Use: clingo prime.lp -c n=max
 *      where composites between 2..max are to be generated.
 *%


num(1..n).

divisor(M, N) :- num(N), num(M), N!=M, N\M==0.

perfect(N) :- num(N), #sum {M : divisor(M, N)} == N.

#show perfect/1.