<!--
  vi: ft=pandoc.markdown
-->

# 中间代码生成

* AST: 抽象语法树
* TAC: 三地址码, 四元式

## 考试用汇编

`JEZ c _ addr`
: 如果c为假跳转到addr, 逆波兰: c(addr)(jez)

`JMP _ _ addr`
: 跳转到addr, 逆波兰: (addr)(jez)

``` {.python}
if c:       # 0x01: JEZ c _ 0x05
    x       # 0x02 - 0x03: x
else        # 0x04: JMP _ _ 0x09
    y       # 0x05 - 0x08: y
            # 0x09:
```

``` {.python}
while c:    # 0x01: JEZ c _ 0x05
    x       # 0x02 - 0x03: x
            # 0x04: JMP _ _ 0x01
            # 0x05
```

<div class="example">
完整例题

``` {.python}
while x + y > 3:
    a = c + 3 * b
    b = a + e - f * e
```

逆波兰
: xy+3> (26)(jez) ac3b*+= bae+fe*-= 1(jmp)

```
01: + x y T1
    > T1 3 T2
    jez T2 _ 12
    * 3 b T3
05: + c T3 T4
    = T4 _ a
    + a e T5
    * f e T6
    - T5 T6 T7
10: = T7 _ b
11: jmp _ _ 1
12:
```
</div>
