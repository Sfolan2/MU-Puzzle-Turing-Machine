# MU-Puzzle-Turing-Machine

Building a Turing Machine to decide whether or not a given input is a theorem
of Hofstader's MU-Puzzle proposed in Godel-Escher-Bach. We are given a strarting
axiom __MI__ and that we can make new theorems by using any of the 4 following
rules on any string we already know is a theorem.

## MU Puzzle
- Rule I: If you possess a string whose last letter is __I__, you can add a 
__U__ at the end
- Rule II: Suppose you have __Mx__, then you may add __Mxx__ to your collection
- Rule III: If __III__ occurs in one of the strings in your collection, you may make
a new string with __U__ in place of __III__
- Rule IV: If __UU__ occurs in one of your strings, you can drop it