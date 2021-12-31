# 子模函数及其应用

## 子模函数

``` {=latex}
\begin{align*}
&\ f(S) + f(T) \ge f(S \cup T) + f(S \cap T) \\
\Leftrightarrow&\ 
f(S \cup \{v\}]) - f(S) \ge f(T \cup \{v\}) - f(T),
S \subseteq T \subseteq V, v \in V \backslash T \\
\Leftrightarrow&\ 
f(S \cup C) - f(S) \ge f(T \cup C) - f(T),
S \subseteq T \subseteq V, C \subseteq V \backslash T \\
\end{align*}
```

## 例题


\begin{problem}{232}{12}
假设全集$U = \{1,2,3,4,5\}$和子集族

\[
    S = \{
        \{1, 2\},
        \{1, 2, 4\},
        \{2, 3\},
        \{4, 5\},
        \{3\},
        \{1, 5\},
    \}
\]

当$k = 2$时，运用爬山算法求解最大覆盖问题，可能的解有哪些？
\end{problem}
\begin{solution}{解}
第1次迭代，显然$S_2$的边界覆盖最大，为3。$S = \{1, 2, 3\}$, $f(S) = 3$。

第2次迭代，可选子集为$S_3, S_4, S_5, S_6$, 边界贡献均为$1$。

\begin{table}[H]
    \centering
    \begin{tabular}{|c|c|c|c|}
        \hline
        子集 & $f(S)$ & $f(S \cup S_i)$ & $\delta(S_i)$ \\ \hline
        $S_1$ & 3 & 3 & 0 \\ \hline
        $S_3$ & 3 & 4 & 1 \\ \hline
        $S_4$ & 3 & 4 & 1 \\ \hline
        $S_5$ & 3 & 4 & 1 \\ \hline
        $S_6$ & 3 & 4 & 1 \\ \hline
    \end{tabular}
\caption{第二轮迭代}
\end{table}

综上，可能的解有
$\{S_2, S_3\}, \{S_2, S_4\}, \{S_2, S_5\}, \{S_2, S_6\}$。
\end{solution}


\begin{problem}{232}{2}
给定下面的全集和子集族, 当$k = 3$时, 使用爬山算法求解最大覆盖问题.

\begin{align*}
    \text{全集}: &\ \{a, b, c, d, e, f, g, h, i, j, k, l\} \\
    \text{子集族}: &\ A_1 = \{b, c, d\}, A_2 = \{e, f, g\}, A_3 = \{i, j, k, l\} \\
                   &\ A_4 = \{a, e, i\}, A_5 = \{i, b, g\}, A_6 = \{c, d, g, h, k, l\} \\
                   &\ A_7 = \{a, l\}, A_8 = \{a, e, i\}
\end{align*}
\end{problem}
\begin{solution}{解}
    第1轮迭代, 显然$A_6$的边际覆盖最大, 为$6$. $S = \{c, d, g, h, k, l\}$, $f(S) = 6$.

    第2轮迭代, $A_4$和$A_8$的边际贡献最大.
    选择$A_4$, $S = \{a, c, d, e, g, h, i, k, l\}$, $f(S) = 9$.

    \begin{table}[H]
    \centering
    \begin{tabular}{|c|c|c|c|}
    \hline
    子集 & $f(S)$ & $f(S \cup A_i)$ & $\Delta(A_i)$ \\ \hline
    $A_1$ & 6 & 7 & 1 \\ \hline
    $A_2$ & 6 & 8 & 2 \\ \hline
    $A_3$ & 6 & 8 & 2 \\ \hline
    $A_4$ & 6 & 9 & 3 \\ \hline
    $A_5$ & 6 & 8 & 2 \\ \hline
    $A_7$ & 6 & 7 & 1 \\ \hline
    $A_8$ & 6 & 9 & 3 \\ \hline
    \end{tabular}
    \end{table}

    第3轮迭代, $A_1$, $A_2$, $A_3$, $A_5$的边际贡献最大.
    选择$A_1$, $S = \{a, b, c, d, e, g, h, i, k, l\}$, $f(S) = 10$.

    \begin{table}[H]
    \centering
    \begin{tabular}{|c|c|c|c|}
    \hline
    子集 & $f(S)$ & $f(S \cup A_i)$ & $\Delta(A_i)$ \\ \hline
    $A_1$ & 9 & 10 & 1 \\ \hline
    $A_2$ & 9 & 10 & 1 \\ \hline
    $A_3$ & 9 & 10 & 1 \\ \hline
    $A_5$ & 9 & 10 & 1 \\ \hline
    $A_7$ & 9 &  9 & 0 \\ \hline
    $A_8$ & 9 &  9 & 0 \\ \hline
    \end{tabular}
    \end{table}

    最终输出为$A_6$, $A_4$, $A_1$.
\end{solution}

\begin{problem}{232}{6}
    令$F = \{1, \ldots, n \}$和$D = \{1, \ldots, m\}$分别表示$n$个设备和$m$个客服组成的集合.
    设备$i$提供服务价值$v_{ij}$给客服$j$. 假定$S \subset F$, 验证

    \begin{equation}
        f(S) = \sum_{j \in D} \max_{i \in S} v_{ij}
        \label{tgt}
    \end{equation}

    是一个子模函数.
\end{problem}

\begin{solution}{证}
令$\forall S \subseteq T \subseteq F$, $\forall w \in F \backslash T$.

\begin{align*}
    f(S) &= \sum_{j \in D} \max_{i \in S} v_{ij} \\
    f(S \cup \{w\}) &= \sum_{j \in D} \max_{i \in S \cup \{w\}} v_{ij} \\
    f(S \cup \{w\}) - f(S) &=
    \sum_{j \in D} \begin{cases}
        v_{wj} - \max_{i \in S} v_{ij} & v_{wj} > \max_{i \in S} v_{ij} \\
        0                              & else
    \end{cases}
\end{align*}

$f(T \cup \{w\})$类似, 由上式可得:

\begin{multline}
    (f(S \cup \{w\}) - f(S)) - (f(T \cup \{w\}) - f(T))
    = \\
    \sum_{j \in D}
    \left(
    \begin{cases}
        v_{wj} - \max_{i \in S} v_{ij} & v_{wj} > \max_{i \in S} v_{ij} \\
        0                              & else
    \end{cases}
    -
    \begin{cases}
        v_{wj} - \max_{i \in T} v_{ij} & v_{wj} > \max_{i \in T} v_{ij} \\
        0                              & else
    \end{cases}
    \right)
    \label{eq1}
\end{multline}

对于$\forall j \in D$:

由假设可得:

\begin{equation}
\max_{i \in S} v_{ij} \le \max_{i \in T} v_{ij}
\label{eq2}
\end{equation}

当$v_{wj} > \max_{i \in S} v_{ij}$, $v_{wj} > \max_{i \in T} v_{ij}$时:
$(v_{wj} - \max_{i \in S} v_{ij}) - (v_{wj} - \max_{i \in T} v_{ij}) \ge 0$.

当$v_{wj} > \max_{i \in S} v_{ij}$, $v_{wj} \le \max_{i \in T} v_{ij}$时:
$(v_{wj} - \max_{i \in S} v_{ij}) - 0 > 0$.

当$v_{wj} \le \max_{i \in S} v_{ij}$, $v_{wj} > \max_{i \in T} v_{ij}$时:
与\ref{eq2}冲突.

当$v_{wj} \le \max_{i \in S} v_{ij}$, $v_{wj} \le \max_{i \in T} v_{ij}$时:
$0 - 0 = 0$

综上所述, 式\ref{eq1}总是大于等于$0$.
即$f(S \cup \{w\}) - f(S) \ge f(T \cup \{w\}) - f(T)$

因此, 式\ref{tgt}是一个子模函数.
\end{solution}

\begin{problem}{233}{10}
    设$f_i(A)$为子模函数, 而且对$i = 1, 2, \ldots, n$都有$a_i \ge 0$,
    试证明$\sum_{i=1}^{n} a_i f_i (A)$也是一个子模函数.
\end{problem}

\begin{solution}{证}
令$g(A) = \sum_{i=1}^{n} a_i f_i (A)$.

\begin{align*}
    g(S) + g(T) &= \sum_{i=1}^{n} a_i (f_i (S) + f_i (T)) \\
    g(S \cup T) + g(S \cap T) &= \sum_{i=1}^{n} a_i (f_i (S \cup T) + f_i (S \cap T))
\end{align*}

对任意$i = 1, 2, \ldots, n$, $f_i (S) + f_i (T) \ge f_i (S \cup T) + f_i (S \cap T)$成立,
并且$a_i \ge 0$.
所以$a_i (f_i (S) + f_i (T)) \ge a_i (f_i (S \cup T) + f_i (S \cap T))$.

因此$g(S) + g(T) \ge g(S \cup T) + g(S \cap T)$,
$g(A)$, 即$\sum_{i=1}^{n} a_i f_i (A)$是一个子模函数.
\end{solution}