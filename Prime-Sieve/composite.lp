%*
 * File: composite.lp
 * Author: Joshua T. Guerin
 *
 * Description: Given an integer n, compute composites from 2..n
 * Use: clingo composite.lp -c n=max
 *      where composites between 2..max are to be generated.
 *%

num(2..n).

composite(X) :- num(X), num(Y), X\Y==0, X!=Y.

#show composite/1.
