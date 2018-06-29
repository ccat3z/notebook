---
# vi: ft=markdown.pandoc
---

# 随机变量及其分布

## 随机变量

<div latex="true" class="define" args="随机变量">
  设随机实验的样本空间为$S = \{\mathit{e}\}$, $X = X(\mathit{e})$是定义在样本空间$S$上的实值单值函数. 称\underline{$X = X(\mathit{e})$}为随机变量
</div>

## 离散型随机变量及其分布律

### 分布律$P$表示形式

* $P\{X = x_k\} = p_k, k = 1, 2, 3, \ldots$
* 
  \begin{tabular}{c|ccc}
      X & $x_1$ & $x_2$ & $x_3$ \\ \hline
      $p_k$ & $p_1$ & $p_2$ & $p_3$
  \end{tabular}

### 重要离散型随机变量

1. $(0 - 1)$分布

    设随机变量只可能取$0$和$1$两个值, 它的分布律为
    $$P\{X = k\} = p^k (1 - p)^{1 - k}, k = 0, 1 (0 < p <1)$$
    表格形式为
    \begin{center}
        \begin{tabular}{c|cc}
            X & $0$ & $1$ \\ \hline
            $p_k$ & $1 - p$ & $p$
        \end{tabular}
    \end{center}

    对于样本空间$S = {e_1, e_2}$都能用$(0 - 1)$分布的随机变量来描述

1. 伯努利试验, 二项分布

    伯努利试验
    : 只有两个可能结果的实验: $A$ 及 $\bar{A}$

       设$P(A) = p\ (0 < p < 1)$, 则$P(\bar{A}) = 1 - p$

    n重伯努利试验
    : 将**伯努力实验**重复$n$次


    二项分布
    : 随机变量$X$表示$n$重伯努利试验中$A$发生的次数, $X$服从参数为$n$, $p$的二项分布, 记作$X \sim b(n, p)$

    $$P\{X = k\} = \vectornum{n}{k} p^k q^{n - k}$$

1. 泊松分布

    设随机变量可能取的值为$0, 1, 2, \ldots$, 而取各个值的概率为

    $$P\{X = k\} = \frac{\lambda^k e^{-\lambda}}{k!}, k = 0, 1, 2, \ldots$$
    
    其中$\lambda > 0$是常数, 则称$X$服从参数为$\lambda$的泊松分布, 记作$X \sim \pi(\lambda)$

#### 泊松分布

::: {.mthm latex="true" args="泊松定理"}
$$\lim_{n -> \infty} \vectornum{n}{k} p^k_n (1 - p_n)^{n - k} = \frac{\lambda^k e^{-\lambda}}{k!}, \lambda = np_n$$
由此可知, $n$很大, $p$很小时， 二项分布可以由此近似
$$\vectornum{n}{k} p^k_n (1 - p_n)^{n - k} \approx \frac{\lambda^k e^{-\lambda}}{k!}, \lambda = np_n$$
:::

## 随机变量的分布函数

分布函数$F$
: 设$X$是一个随机变量, $x$是任意实数, 函数
$$F(x) = P\{X \leq x\}, -\infty < x < \infty$$

## 连续型随机变量及其概率密度

对与随机变量$X$分布函数$F(X)$, 存在非负函数$f(x)$, 使
$$F(x) = \int^x_{-\infty} f(t) dt$$
成了, $X$为**连续性随机变量**, $f(x)$为**概率密度函数**, 简称**概率密度**

### 重要连续型随机变量

1. 均匀分布, $X \sim U(a, b)$

    概率密度为:
    $$f(x) =
    \begin{cases}
        \dfrac{1}{b - a} & a < x < b \\
        0 & \text{其他}
    \end{cases}
    $$

    由此可得分布函数为:
    $$F(x) = 
    \begin{cases}
        0 & x < a \\
        \dfrac{x - a}{b - a} & a \leq x < b \\
        1 & x \geq b
    \end{cases}
    $$

1. 指数分布

    概率密度为:
    $$f(x) =
    \begin{cases}
        \dfrac{1}{\theta} e^{-\frac{x}{\theta}} & x > 0 \\
        0 & \text{其他}
    \end{cases}
    $$

    由此可得分布函数为:
    $$F(x) =
    \begin{cases}
        1 - e^{-\frac{x}{\theta}} & x > 0 \\
        0 & \text{其他}
    \end{cases}
    $$

    无记忆性
