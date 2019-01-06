<!--
  vi: ft=pandoc.markdown
-->


## 自顶向下

FIRST
: 产生的句子的可能的第一个符号

  * $FIRST(\epsilon) = \{\epsilon\}$
  * $FIRST(a\ldots) = \{a\}$
  * $FIRST(A\ldots) = FIRST(A), A \not\rightarrow \epsilon$

FOLLOW
: 符号的下一个可能符号, 末尾为$\#$

  * $FOLLOW(S) = {\#} \cup \ldots$

SELECT
: 读取下一个符号可推导

LL(1)
: 从左到右(Left), 最左推导(Left derivation), 向后读取一个符号

LL(1)判别方式
: $SELECT(A \rightarrow X) \cap SELECT(A \rightarrow Y) = \emptyset$

### 常见非LL(1)

1. 左公因子$A \rightarrow aX | aY$转化为$A \rightarrow aA'$, $A' \rightarrow X | Y$
1. 左递归$A \rightarrow Aa | b | c$转化为右递归$A \rightarrow bA' | cA'$, $A' \rightarrow aA$

### 例题

P93 4.5.2
