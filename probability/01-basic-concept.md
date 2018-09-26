---
# vi: ft=markdown.pandoc
---

# 基础概念

* 互不相容 (互斥) $A \cap B = \emptyset$
* 逆事件 (对立事件) $A \cup B = S \land A \cap B = \emptyset$
* 德摩根律 $\overline{A \cup B} = \bar{A} \cap \bar{B}$
* 概率
  * $0 \leq P(A) \leq 1$
  * 规范性 $P(S) = 1$ 性质扩展 $P(A) \leq P(S) = 1$
  * 可列可加性质, 有限可加性质
  * $A_1, A_2, \ldots \text{两两互不相容} \Rightarrow f_n(A_1 \cup A_2 \cup \ldots) = f_n(A_1) + f_n(A_2) + \ldots$
  * $P(\emptyset) = 0$
  * $A \subset B \Rightarrow P(B - A) = P(B) - P(A), P(B) > P(A)$
  * $P(\bar{A}) = 1 - P(A)$
  * \underline{加法公式 $P(A \cup B) = P(A) + P(B) - P(AB)$}

组合数
: $r \leq a, C_r^a = \vectornum{a}{r} = \dfrac{a (a - 1) \ldots (a - r + 1)}{r!}$

## 条件概率

条件概率
: $P(B | A) = \dfrac{P(AB)}{P(A)}$

乘法定理
: $P(AB) = P(B \mid A)P(A)$, $P(ABC) = P(C \mid AB)P(B \mid A)P(A)$

全概率公式
: $P(A) = P(A \mid B_1)P(B_1) + P(A \mid B_2)P(B_2) + \cdots + P(A \mid B_n)P(B_n)$

贝叶斯公式
: $P(B_i \mid A) = \frac{P(B_i A)}{P(A)} = \frac{P(A \mid B_i)P(B_i)}{\sum_{j=1}^{n}P(A \mid B_j)P(B_j)}$

## 独立性

$$ P(AB) = P(A)P(B) \Leftrightarrow A, B \text{相互独立}$$

$$A, B \text{独立} \Leftrightarrow A, \bar{B} \text{独立}$$

多事件独立
: 
    $$\left.
            \begin{array}{l}
                P(AB) = P(A)P(B), \\
                P(BC) = P(B)P(C), \\
                P(AC) = P(A)P(C), \\
                P(ABC) = P(A)P(B)P(C).
            \end{array}
        \right\}
        \Leftrightarrow{}
        A, B, C \text{相互独立}
    $$
