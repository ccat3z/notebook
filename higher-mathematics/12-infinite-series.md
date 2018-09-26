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
: $\sum_{i = 0}^\infty aq^i = \frac{a - aq^n}{1 - q} = \frac{a}{1 - q}, (|q| < 1)$

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

::: {.mthm latex=true args="[\underline{比较审敛法}]"}
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

::: {.mthm latex=true args="[\underline{比值审敛法}, 达朗贝尔(d'Alembert)判别法]"}
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

* 级数$\sum_{n = 0}^{\infty} (-1)^{n + 1} \frac{1}{n}$收敛

### 绝对收敛与条件收敛

`重点!交错级数!绝对收敛`{.idx}
`重点!交错级数!条件收敛`{.idx}

绝对收敛
: $\sum_{n = 1}^\infty |u_n|$收敛

   如果$\sum_{n = 1}^\infty |u_n|$收敛, $\sum_{n = 1}^\infty u_n$收敛

条件收敛
: $\sum_{n = 1}^\infty u_n$收敛, $\sum_{n = 1}^\infty |u_n|$发散

## 函数项级数

函数项级数
: 对于函数列${u_n(x)}$, $u_1(x) + u_2(x) + \ldots$为函数项无穷级数

收敛(发散)点
: $x = x_0$时, 函数项级数收敛(发散)

收敛区间
: 不包含边界点的收敛域

收敛(发散)域
: 收敛(发散)点的集合

## 幂级数

`重点!幂级数!收敛半径`{.idx}
`重点!幂级数!收敛区间`{.idx}

幂级数
: $\sum_{n = 0}^{\infty} a_nx^n$

    其中$a_0, a_1, a_2, \ldots, a_n, \ldots$为幂级数的系数

::: {.mthm latex=true args="[阿贝尔(Abel)定理]"}
对于$\sum_{n = 0}^{\infty} a_nx^n$, \
当$x = x_0, x_0 \not= 0$时, 该级数收敛, $|x| < |x_0|$使得该级数收敛 \
当$x = x_0, x_0 \not= 0$时, 该级数发散, $|x| > |x_0|$使得该级数发散
:::

::: {.mthm latex=true args="[阿贝尔(Abel)定理 推论]"}
对于$\sum_{n = 0}^{\infty} a_nx^n$, 若不是仅在$x = 0$或整个数轴上收敛, 那么存在一个**收敛半径$R$**, 使得

* $|x| < R$, 幂级数绝对收敛
* $|x| > R$, 幂级数发散
* $|x| = R$, 幂级数收敛性不确定
:::

::: {.mthm latex=true}
如果$\lim_{n -> \infty} |\frac{a_{n + 1}}{a_n}| = \rho$, 那么

$$R = \begin{cases}
\dfrac{1}{\rho} & \rho \not= 0 \\
+\infty & \rho = 0 \\
0 & \rho = +\infty
\end{cases}$$
:::

**注意** 上述定理对$\sum_{n = 0}^{\infty} a_n x^{2n}$无效

**补充例题P277**

### 幂级数运算

#### 四则运算

$$\sum_{n = 0}^{\infty} a_nx^n\ \text{OP}\ \sum_{n = 0}^{\infty} b_nx^n$$

加减乘
: 收敛半径取较小的

除
: 收敛半径可能比二者小得多

#### 幂级数的和函数性质

`重点!幂级数!和函数`{.idx}

$$s(x) = \sum_{n = 0}^{\infty} a_nx^n$$

::: {.mthm latex=true}
$s(x)$在收敛域上连续
:::

::: {.mthm latex=true}
$s(x)$在收敛域上可积, 积分后收敛半径相同
:::

::: {.mthm latex=true}
$s(x)$在收敛区间$(-R, R)$上可导(有任意阶导数), 求导后收敛半径相同
:::

::: {.example}
求幂级数$\sum_{n = 0}^{\infty} \frac{x^n}{n + 1}$的和函数

1. 先求收敛域

    $$\lim_{n \rightarrow \infty} |\frac{a_{n+1}}{a_n}| = \lim_{n \rightarrow \infty} \frac{n + 1}{n + 2} = 1$$

    收敛半径$R = 1$

1. 收敛域

    $x = -1$时
    : $\sum_{n = 0}^{\infty} \frac{(-1)^n}{n + 1}$收敛

    $x = 1$时
    : $\sum_{n = 0}^{\infty} \frac{1}{n + 1}$发散

    收敛域为$[-1, 1)$

1. 设和函数为$s(x) = \sum_{n = 0}^{\infty} \frac{x^n}{n + 1}$

    \begin{align*}
    x s(x) &= \sum_{n = 0}^{\infty} \frac{x^{n + 1}}{n + 1} \\
    (x s(x))^{'} &= \sum_{n = 0}^{\infty} x^n, x \in [-1, 1) \\
    &= \frac{1}{1 - x} \\
    xs(x) &= \begin{cases}
    \int_0^x \frac{1}{1 - t} dt = -ln(1 - x) & x \in [-1, 0) \cup (0, 1) \\
    1 & x = 0
    \end{cases}
    \end{align*}
:::

::: {.example}
求幂级数$\sum_{n = 1}^{\infty} nx^{n - 1}$的和函数

$$\lim_{n \rightarrow \infty} |\frac{a_{n + 1}}{a_n}| = \lim_{n \rightarrow \infty} |\frac{n + 1}{n}| = 1 \Rightarrow R = 1$$

当$x = -1$时
: $\sum_{n = 0}^{\infty} n (-1)^n$发散

当$x = 1$时
: $\sum_{n = 0}^{\infty} n$发散

因此, 收敛域为$(-1, 1)$

\begin{align*}
s(x) &= \sum_{n = 1}^{\infty} nx^{n - 1} \\
\int_0^x s(x) &= \sum_{n = 1}^{\infty} x \\
\int_0^x s(x) &= \frac{1}{1 - x} - 1 = \frac{x}{1 - x} \\
s(x) &= (\frac{x}{1 - x})^{'} = \frac{1}{(1 - x)^2}, |x| < 1
\end{align*}
:::

## 函数展开称幂级数

`重点!函数展开幂级数`{.idx}

泰勒级数
: $$f(x) = \int_{n = 0}^{\infty} \frac{1}{n!} f^{(n)} (x_0)(x - x_0)^n$$

麦克劳林级数
: $$f(x) = \int_{n = 0}^{\infty} \frac{1}{n!} f^{(n)} (0)(x)^n$$

### 常见泰勒级数

* $e^x = \sum_{n=0}^\infty \frac{x^n}{n!} \Rightarrow a^x = e^{ln\ a^x}= e^{xln\ a} = \sum_{n=0}^\infty \frac{(ln\ a)^x}{n!} x^n$
* $\frac{1}{1 - x} = \sum_{n=0}^\infty x^n (|x| < 1)$
* $\frac{1}{1 + x} = \sum_{n=0}^\infty (-1)^n x^n (|x| < 1)$
* $sin\ x = \sum_{n=0}^\infty \frac{(-1)^n}{(2n + 1)!} x^{2n + 1}$
* $cos\ x = \sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} x^{2n}$
* $ln(1 + x)$
* \ldots 注意简单的微积分

## 函数展开傅里叶级数

`重点!函数展开傅里叶级数`{.idx}

对于周期为$2\pi$的函数$f(x)$

$$f(x) = \frac{a_0}{2} + \sum_{k = 1}^{\infty} (a_k cos\ kx + b_k sin\ kx)$$

其中

$$\begin{cases}
a_n = \dfrac{1}{\pi} \int_{-\pi}^{\pi} f(x) cos\ nx dx & n \in \{0, 1, 2, 3, \ldots\} \\
b_n = \dfrac{1}{\pi} \int_{-\pi}^{\pi} f(x) sin\ nx dx & n \in \{1, 2, 3, \ldots\}
\end{cases}$$
