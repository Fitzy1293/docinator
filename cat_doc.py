'''
- This is for combining markdown files into one markdown file.
    - Then it gets compiled with pandoc in docinator.sh

TODO:
    - Build a proper CLI
'''

import os
from pprint import pprint

#********************************************************************************
                                                                                #
outFile = 'out.md'                                                              #
cwd = os.getcwd()                                                               #
sortedFiles = sorted([file for file in os.listdir(cwd)])                        #
                                                                                #
#********************************************************************************

# ------------------------------------------------------------------------------------------------------------------------------------------

'''
List of lines in new "out.md" markdown file.
Gets all .md files in cwd (except the output .md) and concatenates them.
'''

def markdownLineList():
    markdownFiles = []
    for file in sortedFiles:
        if file.endswith('.md') and not file == outFile:
            with open(file, 'r') as f:
                markdownDoc = [line for line in f.read().splitlines()]
                for line in markdownDoc:
                    markdownFiles.append(line)

        markdownFiles.append('')

    return markdownFiles

# ------------------------------------------------------------------------------------------------------------------------------------------

def main():
    markdownList = markdownLineList()
    outputMarkdownStr = '\n'.join(markdownList)
    with open(outFile, 'w+') as f:
        f.write(outputMarkdownStr)

# ------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()
