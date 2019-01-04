#!/usr/bin/env python

"""
latex center environment
e.g.
<div example="center">
...
</div>
will becomes
\begin{center}
...
\end{center}
"""

from pandocfilters import toJSONFilter, RawBlock


def latex_block(x):
    return RawBlock('latex', x)


def center(key, value, format, meta):
    if key == 'Div':
        [[ident, classes, kvs], contents] = value
        kvs = dict(kvs)
        if 'center' in classes:
            if format == 'latex':
                return (
                    [latex_block('\\begin{center}')]
                    + contents
                    + [latex_block('\\end{center}')]
                )


if __name__ == "__main__":
    toJSONFilter(center)
