%*
 * File: set_cover.lp
 * Author: Samuel Ortion
 *
 * Description: Given a universe set S, n subsets of S, S_1, S_2, ..., S_n, find an exact set cover S*
 * Use: clingo set_cover.lp instance.lp
 *      where instance contains the atoms universe/1. for the elements of the S,
 *       and is_in(Set, Element). atoms for element Element in set Set.
 *%

set(Set) :- is_in(Set, _).

% the solution is a selection of the sets
{ selection(Set) : set(Set) }.

% Element is covered if it belongs to a set of the selection
covered(Element) :- selection(Set) , is_in(Set, Element).

% All elements should be covered
:- universe(Element) , not covered(Element).

#show selection/1.
