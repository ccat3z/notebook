---
# vi: ft=markdown.pandoc
---

# 无穷级数

## 常数项无穷级数

(常数项)无穷级数
: $\sum_{i = 1}^\infty u_i = u_1 + u_2 + \ldots$

一般项
: $u_n$

部分和
: $s_n = \sum_{i = 1}^n u_i = u_1 + u_2 + \ldots$

收敛
: $\lim_{n -> \infty} s_n = s$, $s$也叫做这级数的**和**

发散
: $\lim_{n -> \infty} s_n$不存在

余项
: $r_n = s - s_n$

### 常见无穷级数

等比级数(几何级数)
: $\sum_{i = 0}^\infty aq^i$

调和级数\label{常见级数:调和级数}
: 调和级数: $\sum_{n = 1}^\infty \frac{1}{n}$

### 性质

::: {.prop latex=true}
在级数中增删改有限项, 不会改变级数的收敛性
:::

::: {.prop latex=true}
$\lim_{n -> \infty}^\infty u_n = 0 \Leftarrow \sum_{n = 1}^\infty u_n \text{收敛}$

反例: \nameref{常见级数:调和级数}
:::


### 柯西审敛原理
$$\text{级数} \sum_{n = 1}^\infty \text{收敛} \Leftrightarrow \forall \varepsilon,\ \exists N, n > N, \forall p,\ |u_{n + 1} + u_{n + 2} + \ldots u_{n + p}| < \varepsilon$$

## 常数项级数的审敛法

### 正项级数的审敛法

正项级数
: 各项都是正数或零的级数

::: {.mthm latex=true}
正项级数$\sum_{n = 1}^\infty u_n$ $\Leftrightarrow$ 它的部分和数列$\{s_n\}$有界
:::

::: {.mthm latex=true args="[比较审敛法]"}
对于正项级数$\sum_{n = 1}^\infty u_n$, $\sum_{n = 1}^\infty u_v$, 且$u_n \leq u_v$, 若$\sum_{n = 1}^\infty u_v$收敛, 则$\sum_{n = 1}^\infty u_n$收敛, 发散同理
:::

::: {.example}
$1 + \frac{1}{2^p} + \frac{1}{3^p} + \ldots (p > 1)$ 收敛性

对于$x (k - 1 \leq x \leq k)$, $\frac{1}{k^p} \leq \frac{1}{x^p}$ $\Rightarrow$

$$\frac{1}{k^p} = \int_{k - 1}^k \frac{1}{k^p} dk \leq \int_{k - 1}^k \frac{1}{x^p} dx (k = 2, 3, \ldots)$$

所以

\begin{align*}
s_n &= 1 + \sum_{k = 2}^n \frac{1}{k^p} \leq 1 + \sum_{k = 2}^n \int_{k - 1}^k \frac{1}{x^p} dx = 1 + \int_1^n \frac{1}{x^p} dx \\
    &= 1 + \frac{1}{p - 1} (1 - \frac{1}{n^{p - 1}}) < 1 + \frac{1}{p - 1} (n = 2, 3, \ldots)
\end{align*}

所以收敛
:::

::: {.mthm latex=true args="[比较审敛法极限形式]"}
对于正项级数$\sum_{n = 1}^\infty u_n$, $\sum_{n = 1}^\infty u_v$

1. 如果$\lim_{n -> \infty} \frac{u_n}{v_n} = l (0 \leq l < + \infty)$, 若$\sum_{n = 1}^\infty u_v$收敛, 则$\sum_{n = 1}^\infty u_n$收敛
1. 如果$\lim_{n -> \infty} \frac{u_n}{v_n} = l (0 < l\ \text{or}\ l = + \infty)$, 若$\sum_{n = 1}^\infty u_v$发散, 则$\sum_{n = 1}^\infty u_n$发散
::: 

::: {.mthm latex=true args="[比值审敛法, 达朗贝尔(d'Alembert)判别法]"}
对于正项级数$\sum_{n = 1}^\infty u_n$, 如果
$$\lim_{n -> \infty} \frac{u_{n + 1}}{u_n} = \rho,
\begin{cases}
\rho < 1 & \text{级数收敛} \\
\rho > 1 & \text{级数发散} \\
\rho = 1 & \text{都有可能}
\end{cases}$$
:::

::: {.mthm latex=true args="[根值判别法, 柯西判别法]"}
对于正项级数$\sum_{n = 1}^\infty u_n$, 如果
$$\lim_{n -> \infty} \sqrt[n]{u_n} = \rho
\begin{cases}
\rho < 1 & \text{级数收敛} \\
\rho > 1 & \text{级数发散} \\
\rho = 1 & \text{都有可能}
\end{cases}$$
:::

::: {.mthm latex=true args="[极限审敛法]"}
对于正项级数$\sum_{n = 1}^\infty u_n$, 如果
$$\begin{cases}
\lim_{n -> \infty} nu_n = l > 0 & \text{级数发散} \\
\exists p > 1, \lim_{n -> \infty} n^pu_n = l, 0 \leq l < +\infty & \text{级数收敛}
\end{cases}$$

即$u_n$与$\frac{1}{n^p}$的比较审敛法极限形式
:::

### 交错级数的审敛法

交错级数
: $\sum_{n = 1}^{\infty} (-1)^{(n - 1)} u_n = u_1 - u_2 + u_3 - u_4 \ldots$

::: {.mthm latex=true args="[莱布尼兹定理]"}
$$\begin{cases}
u_n \geq u_{n + 1} \\
\lim_{n -> \infty} u_n = 0
\end{cases} \Rightarrow \text{级数收敛}, \text{且} s \leq u_1, \text{其余项} r_n \text{的绝对值} |r_n| \leq u_{n + 1}$$
:::

### 绝对收敛与条件收敛

绝对收敛
: $\sum_{n = 1}^\infty |u_n|$收敛

   如果$\sum_{n = 1}^\infty |u_n|$收敛, $\sum_{n = 1}^\infty u_n$收敛

条件收敛
: $\sum_{n = 1}^\infty u_n$收敛, $\sum_{n = 1}^\infty |u_n|$发散
