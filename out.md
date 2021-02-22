# This is a Simple Markdown Document Using Pandoc

----  

## Why use markdown?

- Low mental overhead when writing documents.
  - No complicated syntax to remember.
- Maintain the advantages of not using a "what you see is what you get editor", i.e being a plain text file.

## Coolness

Here we can easily embed latex, without the overhead of a big latex doc to keep track of!

- $\int_{a}^{b} cos(x) \,dx = sin(x) + c$

**We compile the document like so:**

  - `pandoc test.md -o test.pdf`

Make sure to have a proper \LaTeX{} install before doing this. You can use whatever IDE/text editor works best for you.

----

## Second document

*This is to test concatenating two .md files and compiling them with Pandoc.*

- $x^2$

I am trying to build a program where you run something like:

- `docinator init homework`

----

## This is my 3rd document YAY

*Can it combine three documents,* **let's find out.**


