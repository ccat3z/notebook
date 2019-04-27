#!/usr/bin/env python

"""
``` {.plantuml .embed}
@startuml

[*] --> State1
State1 --> [*]
State1 : this is a string
State1 : this is another string

State1 -> State2
State2 --> [*]

@enduml
```
"""

from pandocfilters import toJSONFilter, Image, get_caption, Para, get_filename4code
import subprocess


g = {'output': None}


def get_image(src):
    outfilename = str(get_filename4code('temp-plantuml', src, 'svg'))
    file = open(outfilename, 'w')
    p = subprocess.Popen(['plantuml', '-p', '-tsvg'], stdin=subprocess.PIPE, stdout=file)
    p.stdin.write(src.encode('UTF-8'))
    p.communicate()
    p.stdin.close()
    return outfilename


def index(key, value, format, meta):
    if key == 'CodeBlock':
        [[ident, classes, kvs], contents] = value
        caption, typef, kvs = get_caption(kvs)
        if 'plantuml' in classes and 'embed' in classes:
            return Para([
                Image(
                    [ident, [], kvs],
                    caption,
                    [get_image(contents), typef]
                )
            ])


if __name__ == "__main__":
    toJSONFilter(index)
