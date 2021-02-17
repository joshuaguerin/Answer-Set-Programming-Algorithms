%*
 * File: subset_sum.lp
 * Author: Joshua T. Guerin
 *
 * Description: Implementation of the subset-sum problem.
 * Use: clingo subset_sum.lp values.lp -c n=<val>
 *      where values.lp contains domain predicates.
 *%


% DEFINE
% Values are candidates to be included in the sum.
{sum(X) : value(X)}.

%% TEST
% Values in sum/1 must sum to n.
:- #sum {X : sum(X)} != n.

% DISPLAY
#show sum/1.
