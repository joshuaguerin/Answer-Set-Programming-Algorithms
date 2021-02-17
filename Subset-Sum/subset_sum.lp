%*
 * File: subset_sum.lp
 * Author: Joshua T. Guerin
 *
 * Description: Implementation of the subset-sum problem.
 * Use: clingo subset_sum.lp values.lp -c n=<val>
 *      where values.lp contains domain predicates.
 *%


% Define
% Values are candidates to be included in the sum.
{sum(X) : value(X)}.

%% Test
% Values in sum/1 must sum to n.
:- #sum {X : sum(X)} != n.

#show sum/1.
