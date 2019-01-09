<!--
  vi: ft=pandoc.markdown:nowrap
-->

# 语法分析

## 文法

\noindent
**终结字符**, **非终结字符** `终结字符`{.idx} `非终结字符`{.idx}

规则`规则`{.idx}, 重写规则`重写规则`{.idx}, 产生式`产生式`{.idx}, 生成式`生成式`{.idx}
: $\alpha \rightarrow \beta$, $\alpha ::= \beta$

文法 `文法`{.idx}
: $G=(V_N, V_T, P, S)$,
$V_N$: 非终结符, $V_T$: 终结符, $P$: 规则集合, $S$: 识别符, 开始符, 一种文法的开始


推导, 归约 `推导`{.idx} `归约`{.idx}
: 对于$a \rightarrow b \rightarrow c$, $a$直接推导$b$, $b$直接归约到$a$ ($a \Rightarrow b$), $a$推导$c$, $c$归约到$a$ ($a \xRightarrow{*/+} b$)

句型, 句子 `句型`{.idx} `句子`{.idx}
: $S \xRightarrow{*} x$, $x$为**句型**, 若x为终结符组成称为**句子**

<div class="example">
已知语言$L(G) = {a^n b^m c^m | n \ge 1, m \ge 0}$, 求$G[S]$

$S \rightarrow AB$

$A \rightarrow aA | a$

$B \rightarrow bBc | \epsilon$

**注意: $S$写最前面**
</div>

### 文法类型

* 0型文法: 全都是
* 1型(上下文有关)文法: $aBc \rightarrow aDcc, |aBc| \le |aDcc|\ or\ A \rightarrow \epsilon$, ($|a| \rightarrow length\ a$)
* 2型(上下文无关)文法: $a \rightarrow bCd$, 其中$a$为单个终结符
* 3型(正规)文法: $A \rightarrow \epsilon | a | aB$

### 句型分析

最右推导(规范推导)
: 优先展开最右非终结符, 推出的句型称为**右(规范)句型**

对于右句型$(Sd(T)db)$,
\begin{tikzpicture}[]
  \node {$S_0$}
    child { node {$(_1$} }
    child { node {$T_1$}
        child { node { $T_2$ }
        child { node { $T_3$ } child { node {$S_1$} } }
            child { node { $d_1$ } }
            child { node { $S_2$ }
                child { node {$(_2$} }
                child { node {$T_3$} }
                child { node {$)_2$} }
            }
        }
        child { node { $d_2$ } }
        child { node { $S_3$ } child { node {$b$} } }
    }
    child { node {$)_1$} };
\end{tikzpicture}

短语
: $S_1$, $(_2 T_3 )_2$, $S_1 d_1 (_2 T_3 )_2$, $b$, $S_1 d_1 (_2 T_3 )_2 d_2 b$, $(_1 S_1 d_1 (_2 T_3 )_2 d_2 b )_1$

直接短语, 简单短语
: $S_1$, $(_2 T_3 )_2$, $b$

句柄(最左直接短语, 仅在右句型中适用)
: $S_1$
