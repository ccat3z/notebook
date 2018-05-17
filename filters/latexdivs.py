#!/usr/bin/env python

"""
Pandoc filter to convert divs with latex="true" to LaTeX
environments in LaTeX output. The first class
will be regarded as the name of the latex environment
e.g.
<div latex="true" class="note abc" args="a b c">...</div>
will becomes
\begin{note}[a][b][c]...\end{note}
"""

from pandocfilters import toJSONFilter, RawBlock, Div
import sys


def latex(x):
    return RawBlock('latex', x)


def latexdivs(key, value, format, meta):
    if key == 'Div':
        [[ident, classes, kvs], contents] = value
        kvs = dict(kvs)
        if ('latex', 'true') in kvs.items():
            if format == 'latex':
                if ident == '':
                    label = ''
                else:
                    label = '\\label{' + ident + '}'

                if 'args' in kvs.keys():
                    args = kvs['args']
                else:
                    args = ''

                return ([latex('\\begin{' + classes[0] + '}' + args + label)]
                        + contents
                        + [latex('\\end{' + classes[0] + '}')])


if __name__ == "__main__":
    toJSONFilter(latexdivs)
