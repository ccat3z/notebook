---
# vi: ft=markdown.pandoc
---

# 基础概念

## 基础

* 随机实验 $E: \{\text{样本点}, \ldots\}$
* 样本空间 $S \subseteq E$
  * 必然事件
  * 随机事件
  * 不可能事件 $\emptyset$
* 事件间关系及其运算
  * 包含 $\subset$, $\subseteq$
  * 等于 $=$
  * 和事件 $A \cup B$，$\bigcup_{k=1}^n A_k$, $\bigcup_{k=1}^\infty A_k$
  * 积事件 $A \cap B$, $\bigcap_{k=1}^n A_k$, $\bigcap_{k=1}^\infty A_k$
  * 差事件 $A - B$
  * 互不相容 (互斥) $A \cap B = \emptyset$
  * 逆事件 (对立事件) $A \cup B = S \land A \cap B = \emptyset$
  * 交换律
  * 结合律
  * 分配律
  * 德摩根律 $\overline{A \cup B} = \bar{A} \cap \bar{B}$
  * 差事件 $A - B$
* 频率

* 频数 $n_A$: n次试验中A发生的次数
* 频率 $f_n(A) = n_A / n$
  * $0 \leq f_n(A) \leq 1$
  * $f_n(S) = 1$
  * $A_1, A_2, \ldots, A_k \text{两两互不相容} \Rightarrow f_n(A_1 \cup A_2 \cup \ldots \cup A_k) = f_n(A_1) + f_n(A_2) + \ldots f_n(A_k)$
  * $n \rightarrow \infty \Rightarrow f_n(A) \rightarrow P(A)$
* 概率
  * 非负数 $P(A) \geq 0$
  * 规范性 $P(S) = 1$ 性质扩展 $P(A) \leq P(S) = 1$
  * 可列可加性质, 有限可加性质
  * $A_1, A_2, \ldots \text{两两互不相容} \Rightarrow f_n(A_1 \cup A_2 \cup \ldots) = f_n(A_1) + f_n(A_2) + \ldots$
  * $P(\emptyset) = 0$
  * $A \subset B \Rightarrow P(B - A) = P(B) - P(A), P(B) > P(A)$
  * $P(\bar{A}) = 1 - P(A)$
  * \underline{加法公式 $P(A \cup B) = P(A) + P(B) - P(AB)$}

## 等可能概型(古典模型)

* 样本空间包含有限个元素
* 每个事件的可能性相同

\begin{define}[组合数]\label{组合数}
    \[r \leq a, C_r^a = \vectornum{a}{r} = \dfrac{a (a - 1) \ldots (a - r + 1)}{r!}\]
\end{define}

## 条件概率

* 条件概率
\begin{mthm}[条件概率]\label{条件概率}
    A事件发生当条件下B发生当条件概率
    \[P(B | A) = \dfrac{P(AB)}{P(A)}\]
\end{mthm}
* \uwave{乘法定理}
\begin{mthm}[乘法定理]\label{乘法定理}\label{乘法公式}
    \[P(AB) = P(B \mid A)P(A)\]
\end{mthm}
由乘法公式~\ref{乘法公式}推导可得: $$P(ABC) = P(C \mid AB)P(B \mid A)P(A)$$
* \uwave{全概率公式}
\begin{define}[划分]\label{划分}
    $S$为$E$的样本空间, $B_1, B_2, \ldots, B_n$ 为$E$的一组事件,
    满足 $B_i B_j = \emptyset, i \not= j, i, j = 1, 2, \ldots, n \land B_1 \cup B_2 \cup \ldots \cup B_n = S$,
    则称 $B_1, B_2, \ldots, B_n$ 为$E$的一个划分
\end{define}
\begin{mthm}[全概率公式]\label{全概率公式}
    $B_1, B_2, \ldots, B_n$ 为S当一个划分~\ref{划分}
    \[P(A) = P(A \mid B_1)P(B_1) + P(A \mid B_2)P(B_2) + \cdots + P(A \mid B_n)P(B_n)\]
\end{mthm}
* \uwave{贝叶斯公式}
\begin{mthm}[贝叶斯公式]\label{贝叶斯公式}
    $B_1, B_2, \ldots, B_n$为$S$的一个划分~\ref{划分},
    由条件概率~\ref{条件概率}及全概率公式~\ref{全概率公式}推得
    \[P(B_i \mid A) = \frac{P(B_i A)}{P(A)} = \frac{P(A \mid B_i)P(B_i)}{\sum_{j=1}^{n}P(A \mid B_j)P(B_j)}\]
\end{mthm}

## 独立性

\begin{define}[独立]\label{独立}\label{相互独立}
    对于$A, B$两事件
    \[ P(AB) = P(A)P(B) \Leftrightarrow A, B \text{相互独立}, \text{简称} A, B \text{独立} \]
\end{define}
\begin{mthm}
    \[ A, B \text{独立} \Leftrightarrow A, \bar{B} \text{独立} \]
\end{mthm}
\begin{define}[多事件独立]
    \[
        \left.
            \begin{array}{l}
                P(AB) = P(A)P(B), \\
                P(BC) = P(B)P(C), \\
                P(AC) = P(A)P(C), \\
                P(ABC) = P(A)P(B)P(C).
            \end{array}
        \right\}
        \Leftrightarrow{}
        A, B, C \text{相互独立}
    \]
\end{define}
