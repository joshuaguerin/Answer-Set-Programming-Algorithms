# Problem: I'm my own Grandpa

## Description
"[I'm My Own Grandpa](https://en.wikipedia.org/wiki/I%27m_My_Own_Grandpa)" is a song written by [Dwight Latham](https://www.imdb.com/name/nm0490077/) and [Moe Jaffe](https://en.wikipedia.org/wiki/Moe_Jaffe), and has been performed by several artists including [Ray Stevens](https://en.wikipedia.org/wiki/Ray_Stevens), [Willie Nelson](https://en.wikipedia.org/wiki/Willie_Nelson), and [Tom Arnold](https://en.wikipedia.org/wiki/Tom_Arnold_(actor)) (in the 1996 comedy "[The Stupids](https://en.wikipedia.org/wiki/The_Stupids)."). The song is told from the perspective of a(n unnamed) narrator who, along with his father, engage in marriages and producting offspring. Through a somewhat convoluted series of inferences, the narrator concludes that, by definition, he has become his own grandfather.

The notion of encoding a family tree is not new, and actually serves as a somewhat common school assignment in logical models and introducing newcomers to logical languages. Indeed, the "I'm my own Grandpa" lyrics have actually inspired discussion of models for representing relationships in family domains, including a chapter of the text "[How We Reason](https://academic.oup.com/book/11984)" by Philip Johnson-Laird [^1].

[^1]: Johnson-Laird, P. N. (2006). How We Reason. Oxford University Press. ISBN 978-0199551330.

## Relationships
The song lyrics [^2] contains only a handful of preexisting relationships, at which point it switches into inference to discover the eventual grandparent relationship between the narrator and himself. These starting relationships are:
* I (the narrator) am married to a widow.
* The widow had an adult daughter with red hear.
* My father marries the widow's daughter.
* I have a son (with the widow), a "bouncing baby boy."
* The widow has a son.

[^2]: Due to existing copyright, the lyrics are not reproduced on this page outside of an analysis of the relationships. At the time of this writing the song lyrics can be found  online in text, audio, and video formats.

Additional relationships that are inferred over the course of the song:
* My father is my son.
* The widow (by marriage to my father) is my daughter and mother.
* The baby is the brother to my father.
* The baby is my uncle.
* The baby is brother of the widow's daughter.
* The son (of the widow's daughter) is my grandchild.
* My wife (widow) is now my grandmother, and I am her grandchild.
* because I am married to the widow (my grandmother) I am my own grandfather.

The following image illustrates the relationships specified directly and inferred from the song:

![Family relationships inferred from the song logic.](images/relationships.png)
A larger version of the image can be found in the [images](images/relationships.pdf) directory.

## Dependencies
The [print](print/) system generates [graphviz](https://graphviz.org/) files for input, that can be viewed, redirected into a file, or rendered using dot. The latter step can be omitted if graphviz is not present or if graphical output is not desired. 

## Implementational Notes
In order to have the [print](print/) system work correctly all output is currently enabled. Due to the volume of relationships printed, this does not lend itself to easy parsing by the reader, but instead enables a graphical visualization of the output.

If the user wishes to see a binary output based on the problem syntax, the final `#show` can be uncommented, and any other desired print statements can be easily added. 
