---
title: "**A Simple Markdown Document Using Pandoc**"
author: John Doe
date: 2021
geometry: ["left=3.5cm","right=2cm","bottom=3.5cm","top=3cm"]
header-includes:
  - \usepackage{listings}
  - \usepackage{xcolor}
  - \usepackage{amsmath}
---

\noindent\rule{\textwidth}{1pt}

\tableofcontents

\noindent\rule{\textwidth}{1pt}


# Why use markdown?

- Low mental overhead when writing documents.
  - No complicated syntax to remember.
- Maintain the advantages of not using a "what you see is what you get editor", i.e being a plain text file.

## Coolness

Here we can easily embed latex, without the overhead of a big latex doc to keep track of!

\begin{align*}
    \int_a^b cos(x) \,dx &= sin(x) + c \\
    \oint \! \nabla f dt  &= 0
\end{align*}




# Running docinator

- Make it executable and run this command in the shell:
    - `./docinator.sh`

<test>

 ```
  #!/bin/sh
  echo "Running pandoc"
  pandoc -f markdown ./markdown/title.md ./markdown/content/*.md -o markdown.pdf
```

Make sure to have a proper LaTeX install before doing this.
You can use whatever IDE/text editor works best for you.

\noindent\rule{\textwidth}{1pt}
