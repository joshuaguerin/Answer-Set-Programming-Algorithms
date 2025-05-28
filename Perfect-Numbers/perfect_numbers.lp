%*
 * File: perfect.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given an integer n, perfect numbers from 2..n
 *
 * Use: clingo perfect_numbers.lp -c n=<max>
 *      where perfect numbers between 2..max are to be generated.
 *%


num(1..n).

divisor(M, N) :- num(N), num(M), N!=M, N\M==0.

perfect(N) :- num(N), #sum {M : divisor(M, N)} == N.

perfect(M, N) :- perfect(N), divisor(M, N).

#show perfect/1.
#show perfect/2.