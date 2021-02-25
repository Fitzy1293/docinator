---
title: "A Simple Markdown Document Using Pandoc"
author: John Doe
date: 2021
#geometry: "left=3cm,right=3cm,top=2cm,bottom=2cm"
output: pdf_document
header-includes:
  \usepackage{blindtext}
---

\tableofcontents

----  

# Why use markdown?

- Low mental overhead when writing documents.
  - No complicated syntax to remember.
- Maintain the advantages of not using a "what you see is what you get editor", i.e being a plain text file.

## Coolness

Here we can easily embed latex, without the overhead of a big latex doc to keep track of!

- $\int_{a}^{b} cos(x) \,dx = sin(x) + c$

# Running docinator

**We compile the document like so:**

  - `pandoc test.md -o test.pdf`

Make sure to have a proper \LaTeX{} install before doing this.
You can use whatever IDE/text editor works best for you.
