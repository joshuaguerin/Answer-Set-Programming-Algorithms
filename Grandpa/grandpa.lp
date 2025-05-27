%*
 * File: grandpa.lp
 * Author: Jackson Madsen, Joshua T. Guerin
 *
 * Description: Encoding the lyrics of "I am my own grandpa" to verify
 * 		the relation grandpa(me, me).
 *
 * Use: clingo grandpa.lp instance.lp
 *      where instance.lp contains node and edge predicates.
 *
 * Attributions: Written by Dwight Latham and Moe Jaffe
 * 		 Inspired by "Very Closely Related" in "Wit and Humor" by
 *		 Mark Twain.
 *		 Performed by Ray Stevens, Willie Nelson, Tom Arnold, and
 *		 others.
 *
 * Note: For the sake of simplicity, "step" relations are not encoded
 * 	 separately (e.g., a stepparent is simply a parent), and non-gendered
 *	 relations are preferred (parent to mother and father).
*%


% Marriage is a symmetric relation.
married(Bride, Groom) :- married(Groom, Bride),
	       	         Bride != Groom.

% Siblings are related by shring parent.
sibling(Child1, Child2) :- parent(Parent, Child1),
			   parent(Parent, Child2),
			   Child1 != Child2.

% Stepparents are also Parents.
parent(Stepparent, Child) :- parent(Parent, Child),
		             married(Parent, Stepparent).

% Uncles are male siblings of parents.
% Note: Gendered verions of aunt/uncle are the most prevelant in English.
uncle(Uncle, Child) :- sibling(Parent, Uncle),
	     	       parent(Parent, Child),
		       male(Uncle).

% Grandparents are the parents of the parents.
grandparent(Grandparent, Child) :- parent(Grandparent, Parent),
		 	   	   parent(Parent, Child).

% Self-Grandpa, a unary, reflexive relation.
grandpa(Person) :- grandparent(Person, Person),
		   male(Person).

%% PRINT
% Can be enabled by uncommenting for a binary yes/no.
% Full output is currently displayed for the graphical printing system.
%#show grandpa/1.