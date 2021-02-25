'''
- This is for combining markdown files into one markdown file.
    - Then it gets compiled with pandoc in docinator.sh

- Get the file order from the file name.
- Keep it simple man.

TODO:
    - Build a proper CLI
'''

import os, sys
from subprocess import Popen, PIPE
from pprint import pprint
from time import time

# ******************************************************************************
outFile = 'out.md'
cwd = os.getcwd()
titleMdPath = os.path.join('markdown', 'title.md')
mdContentsDir = os.path.join('markdown', 'content')
sortedFiles = sorted([os.path.join(mdContentsDir, file) for file in os.listdir(mdContentsDir)])

mdFiles = [titleMdPath] + sortedFiles
mdFilesPrintStr = "\n\t".join(mdFiles)
print(f'.md files:\n\t{mdFilesPrintStr}')

# ******************************************************************************


# ------------------------------------------------------------------------------------------------------------------------------------------

'''
List of lines in new "out.md" markdown file.
Gets all .md files in cwd (except the output .md) and concatenates them.
'''

def createMarkdownStr():
    markdownFiles = []
    pageBreakLatexStr = '\n\n\\newpage{}\n\n'
    mdExt = '.md'

    for file in mdFiles:
        with open(file, 'r') as f:
            fileStr = f.read()
            markdownFiles.append(fileStr)

    return pageBreakLatexStr.join(markdownFiles)

# ------------------------------------------------------------------------------------------------------------------------------------------

def main():
    startTime = time()

    combinedMdStr = createMarkdownStr()
    p = Popen(['pandoc', '-t', 'pdf', '-o', 'test.pdf'], stdin=PIPE)
    p.communicate(input=str.encode(combinedMdStr))

    endTime = time()

    print(f'Run time: {round(endTime - startTime, 2)} (s)')


# ------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
