#!/usr/bin/env python

"""
latex example environment
e.g.
<div example="true">
Q...

A...
</div>
will becomes
\begin{example}{Q...}
A...
\end{note}
"""

from pandocfilters import toJSONFilter, RawInline, RawBlock
import sys


def latex(x):
    return RawInline('latex', x)


def latex_block(x):
    return RawBlock('latex', x)


def example(key, value, format, meta):
    if key == 'Div':
        [[ident, classes, kvs], contents] = value
        kvs = dict(kvs)
        if 'example' in classes:
            if format == 'latex':
                if ident == '':
                    label = ''
                else:
                    label = '\\label{' + ident + '}'

                contents[0]['c'] = (
                        [latex('\\begin{example}{')]
                        + contents[0]['c']
                        + [latex('}' + label)]
                )

                if contents[1]['t'] == 'Para':
                    contents[0]['c'] += contents[1]['c']
                    del contents[1]

                if contents[-1]['t'] == 'Para':
                    contents[-1]['c'] += [latex('\\end{example}')]
                else:
                    contents += [latex_block('\\end{example}')]

                return contents


if __name__ == "__main__":
    toJSONFilter(example)
