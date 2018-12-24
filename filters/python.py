#!/usr/bin/env python

"""
exec python script and insert global variable 'output'
as raw latex in the document if 'output' is not None

``` {.python .embed}
output = 'hello'
```
"""

from pandocfilters import toJSONFilter, RawInline, RawBlock


g = {'output': None}


def get_output(script):
    exec(script, g)
    return str(g['output'])


def index(key, value, format, meta):
    if key == 'CodeBlock' or key == 'Code':
        [[ident, classes, kvs], contents] = value
        if 'python' in classes and 'embed' in classes:
            out = get_output(contents)
            if g['output'] is not None:
                return [
                    RawInline('latex', out)
                    if key == 'Code'
                    else RawBlock('latex', out)
                ]
            else:
                return []


if __name__ == "__main__":
    toJSONFilter(index)
