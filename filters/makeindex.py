#!/usr/bin/env python

"""
`索引`{.idx} -> \index{suo3 yin3@索引}
`a@索引`{.idx} -> \index{a@索引}
"""

from pandocfilters import toJSONFilter, RawInline
from pypinyin import lazy_pinyin, Style
import re
import sys


def latex_in_line(x):
    return RawInline('latex', x)


def index(key, value, format, meta):
    if key == 'Code':
        [[ident, classes, kvs], contents] = value
        if 'idx' in classes:
            if '@' not in re.sub('"@', '', contents):
                real_indexs = re.sub('"!', '', contents).split('!')
                contents = '!'.join(list(map(lambda x: '{}@{}'.format(
                    ' '.join(lazy_pinyin(x, style=Style.TONE3)),
                    x
                ), real_indexs)))
            return [latex_in_line('\\index{{{}}}'.format(contents))]


if __name__ == "__main__":
    toJSONFilter(index)
