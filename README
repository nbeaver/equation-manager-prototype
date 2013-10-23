Example usage:

    python search.py approximation

This is a prototype of a text-based equation storage, processing, and retrieval program.

It is an excruciatingly simplistic implementation in python with a small textual database of equations.

The [database](equation-database.txt) is in the [cookie jar format](http://www.catb.org/esr/writings/taoup/html/ch05s02.html#id2902164), although for simplicity comments after the `%%` delimiters are not permitted.

The first line of a record is a textual description of the equations. This is what gets matched in a search.

After the first line is a unicode pretty-print, including symbols like Greek letters, subscripts and superscripts, and square root symbols.

Everything after that is optional, but it is useful to include formats for a variety of human-readable markups, such as [LaTeX](http://www.latex-project.org/), [asciimathml](http://www1.chapman.edu/~jipsen/mathml/asciimath.html), and [troff/eqn](http://troff.org/prog.html#eqn). Similarly useful are inputs for commonly used scientific programming languages like [C](http://www.open-std.org/jtc1/sc22/wg14/), [Fortran](http://www.nag.co.uk/sc22wg5/), [Java](http://www.oracle.com/technetwork/java/index.html), [Julia](http://julialang.org/), [Mathematica](https://www.wolfram.com/mathematica/), [Matlab](http://www.mathworks.com/products/matlab/), [Maxima](http://maxima.sourceforge.net/), [Octave](https://www.gnu.org/software/octave/), [Python](http://www.python.org/), and [Sage](http://www.sagemath.org/).

The textual database uses Unicode (specifically UTF-8) for many of the math characters. If these characters don't show up correctly:

→ (right arrow)

± (plus-or-minus symbol)

√ (square root symbol)

∞ (infinity symbol)

∂ (partial differential)

∫ (integral)

γ (Greek lowercase gamma)

ℏ (h-bar)

ⁿ (superscript n)

₀ (subscript 0)

then you will need to install Unicode (UTF-8) encodings to view the equations properly.
