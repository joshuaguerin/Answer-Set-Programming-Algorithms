%*
 * File: set_cover.lp
 * Author: Samuel Ortion
 *
 * Description: Given a universe set S, n subsets of S, S_1, S_2, ..., S_k, find an exact set cover S*
 * Use: clingo set_cover.lp exact_set_cover.lp instance.lp
 *      where instance contains the atoms universe/1. for the elements of the S,
 *       and is_in(Set, Element). atoms for element Element in set Set.
 *%

% In exact set cover, two selected set cannot contain the same element
:- selection(Set1) , selection(Set2) , is_in(Set1, Element) , is_in(Set2, Element) , Set2 != Set1.
