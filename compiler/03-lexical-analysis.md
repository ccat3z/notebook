<!--
  vi: ft=pandoc.markdown
-->

# 词法分析

正规式
: $1(0|1)^{*} 0$

NFA
: 不确定的有穷自动机

  \begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=2cm, semithick]
    \tikzstyle{every node}=[circle,scale=0.7]
    \node[initial,state] (A) {$a$};
    \node[state] (B) [right of=A] {$b$};
    \node[state] (C) [right of=B] {$c$};
    \node[state] (D) [right of=C] {$d$};
    \node[state,double] (E) [right of=D] {$e$};
  
    \path (A) edge node {$1$} (B)
          (B) edge node {$\epsilon$} (C)
          (C) edge node {$\epsilon$} (D)
          (B) edge[bend left=100] node {$\epsilon$} (D)
          (C) edge[loop above] node {$0$} (C)
          (C) edge[loop below] node {$1$} (C)
          (D) edge node {$0$} (E);
  \end{tikzpicture}

NFA转DFA
: \

  状态/输入 | 0 | 1
  -- | -- | --
  A {a} | - | B {b, c, d}
  B {b, c, d} | $\epsilon\text{-closue}(c, e)$ = **C** {c, d, **e**} | D {c, d}
  **C** {c, d, **e**} | **C** | D
  D {c, d} | **C** | D

DFA
: 确定的有穷自动机

DFA化简(确定法, 最小化)
: $\{\{A, B, D\}, \{C\}\}$, 若状态任意输入后下一个状态在其他组则独立出来, 最后同组内合并

  状态/输入 | 0 | 1
  -- | -- | --
  A | - | B
  B | **C** | B
  **C** | **C** | B

  \begin{tikzpicture}[->,>=stealth',shorten >=1pt,auto,node distance=2cm, semithick]
    \tikzstyle{every node}=[circle,scale=0.7]
    \node[initial,state] (A) {$A$};
    \node[state] (B) [right of=A] {$B$};
    \node[state,double] (C) [right of=B] {$C$};
  
    \path (A) edge node {$1$} (B)
          (B) edge[bend left] node {$0$} (C)
          (B) edge[loop above] node {$1$} (B)
          (C) edge[loop above] node {$0$} (C)
          (C) edge[bend left] node {$1$} (B);
  \end{tikzpicture}
