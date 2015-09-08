=============================================================
A minimal UTF-8 text equation database with simple searching.
=============================================================

Example usage:

    python search.py approximation

This is a prototype of a text-based equation storage, processing, and retrieval program.

It is an excruciatingly simplistic implementation in ``python`` with a small textual database of equations.

If you are curious about the motivation of this tool, see here:

<https://github.com/nbeaver/equation-manager-description>

--------------------
Database description
--------------------

The [database](equation-database.txt) is in the [cookie jar format](http://www.catb.org/esr/writings/taoup/html/ch05s02.html#id2902164),
although for simplicity comments after the `%%` delimiters are not permitted.
(Ideally this would be migrated to [YAML](http://en.wikipedia.org/wiki/YAML),
which is a more standard format that also allows multiline block literals with newlines preserved,
so the equations remain readable.
See the [TODO list below](#todo).)

The entire record is matched in the search,
which is case-insensitive.

The first line (after the `%%`) of a record is a textual description of the equations.

After the first line is a unicode pretty-print of the equation,
including symbols like Greek letters,
subscripts and superscripts,
and square root symbols.

Everything after that is optional,
but it is useful to include formats for a variety of human-readable markups,
such as [LaTeX](http://www.latex-project.org/),
[asciimathml](http://www1.chapman.edu/~jipsen/mathml/asciimath.html),
and [troff/eqn](http://troff.org/prog.html#eqn).

Similarly useful are inputs for commonly used scientific programming languages,
like [C](http://www.open-std.org/jtc1/sc22/wg14/),
[Fortran](http://www.nag.co.uk/sc22wg5/),
[Java](http://www.oracle.com/technetwork/java/index.html),
[Julia](http://julialang.org/),
[Mathematica](https://www.wolfram.com/mathematica/),
[Matlab](http://www.mathworks.com/products/matlab/),
[Maxima](http://maxima.sourceforge.net/),
[Octave](https://www.gnu.org/software/octave/),
[Python](http://www.python.org/),
and [Sage](http://www.sagemath.org/).

-----------------
Notes on encoding
-----------------

The textual database uses Unicode
(specifically [UTF-8](http://en.wikipedia.org/wiki/UTF-8))
for many of the math characters.
If these characters don't show up correctly:

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

then you will need to install Unicode (UTF-8) encodings or supporting fonts to view the equations properly.

See [common-unicode-symbols.txt](common-unicode-symbols.txt) for some more examples.

----
TODO
----

Database:
* Change database format into more easily parseable YAML.
* Add MathML equation expressions.
* Add OpenMath equation expressions.
* Add internal cross references.
* Add external references.
* Add dimensions for each variable.
* Add variants for e.g. Gaussian vs. SI units.
* Add RPN versions of equations.

Search tool:
* Add case-sensitive search.
* Search by symbols in equation.
* Search by units.
* Search by dimensions.
* Return equations that have a subexpression matching the query (e.g. `a x^2 + b x + c` matches `c + b x`).
* Return equations that are equivalent given simple substitution of variables (e.g. `a+b^2` matches `x+y^2`).
* Search by algebraically equivalent form (e.g. `a(b+c)` matches `a b + a c`).
