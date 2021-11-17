#!/usr/bin/env python

"""
`索引`{.idx} -> \index{suo3 yin3@索引}
`a@索引`{.idx} -> \index{a@索引}
`#索引` -> \index{suo3 yin3@索引}索引
`#索引`{.not-idx} -> `#索引`
"""

from pandocfilters import toJSONFilter, RawInline, Str
from pypinyin import lazy_pinyin, Style
import re
import sys


def latex_in_line(x):
    return RawInline('latex', x)

def latex_index(contents):
    if '@' not in re.sub('"@', '', contents):
        real_indexs = re.sub('"!', '', contents).split('!')
        contents = '!'.join(list(map(lambda x: '{}@{}'.format(
            ' '.join(lazy_pinyin(x, style=Style.TONE3)),
            x
        ), real_indexs)))
    return latex_in_line('\\index{{{}}}'.format(contents))

def index(key, value, format, meta):
    if key == 'Code':
        [[ident, classes, kvs], contents] = value
        if 'idx' in classes:
            return [latex_index(contents)]

        if contents.startswith('#') and 'not-idx' not in classes:
            contents = contents[1:]
            return [latex_index(contents), Str(contents)]


if __name__ == "__main__":
    toJSONFilter(index)
