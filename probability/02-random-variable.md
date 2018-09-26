---
# vi: ft=markdown.pandoc
---

# 随机变量及其分布

`分布函数`{.idx}

分布函数$F$
: 设$X$是一个随机变量, $x$是任意实数, 函数$F(x) = P\{X \leq x\}, -\infty < x < \infty$

## 离散型随机变量

`离散性随机变量!(0 - 1)分布`{.idx}

1. $(0 - 1)$分布

   随机变量只可能取$0$和$1$两个值, 

   `分布律`{.idx}
 
   分布律
   : $P\{X = k\} = p^k (1 - p)^{1 - k}, k = 0, 1 (0 < p <1)$

   `分布律表格`{.idx}

   分布律表格
   : 

      \begin{tabular}{c|cc}
          X & $0$ & $1$ \\ \hline
          $p_k$ & $1 - p$ & $p$
      \end{tabular}

1. 伯努利试验, 二项分布: $X \sim b(n, p)$

   `离散性随机变量!二项分布`{.idx} `伯努力试验`{.idx} `n重伯努力试验`{.idx}

   伯努利试验
   : 只有两个可能结果的实验: $A$ 及 $\bar{A}$

      设$P(A) = p\ (0 < p < 1)$, 则$P(\bar{A}) = 1 - p$

   n重伯努利试验
   : 将**伯努力实验**重复$n$次

   二项分布
   : 随机变量$X$表示$n$重伯努利试验中$A$发生的次数, $X$服从参数为$n$, $p$的二项分布

   分布律
   : $P\{X = k\} = \vectornum{n}{k} p^k q^{n - k}$

   数学期望
   : $E(X) = p$

   方差
   : $D(X) = p(1 - p)$

1. 泊松分布: $X \sim \pi(\lambda)$

   `离散性随机变量!泊松分布`{.idx}

   随机变量可能取的值为$0, 1, 2, \ldots$

   分布律
   : $P\{X = k\} = \frac{\lambda^k e^{-\lambda}}{k!}, k = 0, 1, 2, \ldots$

   数学期望
   : $E(X) = \lambda$

   方差
   : $D(X) = E(X^2) - [E(X)]^2 = [E(X(X - 1)) + E(X)] - \lambda^2 = \sum_{k = 0}^{\infty} k(k - 1) \frac{\lambda^k e^{-\lambda}}{k!} + \lambda - \lambda^2 = \lambda^2 + \lambda - \lambda^2 = \lambda$

   其中$\lambda > 0$是常数, 则称$X$服从参数为$\lambda$的泊松分布

   `泊松定理`{.idx}

   ::: {.mthm latex="true" args="泊松定理"}
   $$\lim_{n -> \infty} \vectornum{n}{k} p^k_n (1 - p_n)^{n - k} = \frac{\lambda^k e^{-\lambda}}{k!}, \lambda = np_n$$
   由此可知, $n$很大, $p$很小时， 二项分布可以由此近似
   $$\vectornum{n}{k} p^k_n (1 - p_n)^{n - k} \approx \frac{\lambda^k e^{-\lambda}}{k!}, \lambda = np_n$$
   :::

   `重点!泊松定理证明`{.idx}

   ::: {.example}
   证明泊松定理

   由$p_n = \frac{\lambda}{n}$可得:

   \begin{align*}
   \vectornum{n}{k} p_n^k (1 - p_n)^{n - k} &= \frac{n (n - 1) \ldots (n - k + 1)}{k!} (\frac{\lambda}{n})^k (1 - \frac{\lambda}{n})^{n - k} \\
   &= \frac{\lambda^k}{k!} [1 \cdot \frac{n - 1}{n} \ldots \frac{n - k + 1}{n}] (1 - \frac{\lambda}{n})^{n - k} \\
   \end{align*}

   当$n \rightarrow \infty$时: $[1 \cdot \frac{n - 1}{n} \ldots \frac{n - k + 1}{n}] \rightarrow 1$, $(1 - \frac{\lambda}{n})^{n - k} \rightarrow e^{-\lambda}$

   即$\lim_{n \rightarrow \infty} \vectornum{n}{k} p_n^k (1 - p_n)^{n - k} = \frac{\lambda^k e^{-\lambda}}{k!}$
   :::

## 连续型随机变量

`概率密度函数`{.idx}

对与随机变量$X$分布函数$F(X)$, 存在非负函数$f(x)$, 使
$$F(x) = \int^x_{-\infty} f(t) dt$$
成了, $X$为**连续性随机变量**, $f(x)$为**概率密度函数**, 简称**概率密度**, 概率密度函数可以大于1

1. 均匀分布: $X \sim U(a, b)$

   `连续性随机变量!均匀分布`{.idx}

   概率密度
   : $f(x) = \begin{cases} \dfrac{1}{b - a} & a < x < b \\ 0 & \text{其他} \end{cases}$

   分布函数
   : $F(x) = \begin{cases} 0 & x < a \\ \dfrac{x - a}{b - a} & a \leq x < b \\ 1 & x \geq b \end{cases}$

   数学期望
   : $E(X) = \frac{a + b}{2}$

   方差
   : $D(X) = E(X^2) - [E(X)]^2 = \int_{a}^{b} x^2 \frac{1}{b - a} dx - (\frac{a + b}{2})^2 = \frac{(b - a)^2}{12}$

1. 指数分布

   `连续性随机变量!指数分布`{.idx}

   概率密度
   : $f(x) = \begin{cases} \dfrac{1}{\theta} e^{-\frac{x}{\theta}} & x > 0 \\ 0 & \text{其他} \end{cases}$

   分布函数
   : $F(x) = \begin{cases} 1 - e^{-\frac{x}{\theta}} & x > 0 \\ 0 & \text{其他} \end{cases}$

   无记忆性
   : $P\{X > s + t \mid X > s\} = P\{X > t\}$

1. 正态分布: $X \sim N(\mu, \sigma^2)$

   `连续性随机变量!正态分布`{.idx}

   概率密度
   : $f(x) = \frac{1}{\sqrt{2\pi} \sigma} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$

   分布函数
   : $F(x) = \frac{1}{\sqrt{2\pi} \sigma} \int_{-\infty}^{x} e^{-\frac{(x - \mu)^2}{2\sigma^2}} dt$

   数学期望
   : $\mu$

   方差
   : $\sigma^2$

1. 标准正态分布: $X \sim N(0, 1^2)$

   `连续性随机变量!标准正态分布`{.idx}

   概率密度
   : $\varphi(x) = \frac{1}{\sqrt{2\pi}} e^{\frac{-x^2}{2}}$

   分布函数
   : $\Phi(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{t^2}{2}} dt$

       $1 - \Phi(x) = \Phi(-x)$

   转化为标准正态分布
   : 若$X \sim N(\mu, \sigma^2)$, $Z = \frac{X - \mu}{\sigma} \sim N(0, 1)$

       ::: {.example}
       $X \sim N(90, 0.5^2)$, 求$P\{X < 89\}$

       \begin{align*}
       P\{X < 89\} &= P\{\frac{X - 90}{0.5} < \frac{89 - 90}{05}\} \\
       &= \Phi(\frac{89 -90}{0.5}) \\
       &= 0.0228
       \end{align*}
       :::

   上$\alpha$分位点
   : $P\{X > z_{\alpha}\} = \alpha, 0 < \alpha < 1$

## 随机变量的函数的分布

::: {.example}
随机变量$X$具有概率密度$f_X(x), -\infty < x < \infty$, 求$Y = X^2$的概率密度

\begin{align*}
F_Y(y) &= P\{Y \leq y\} = P\{X^2 \leq y\} \\
&= P\{-\sqrt{y} \leq X \leq \sqrt{Y}\} \\
&= F_X(\sqrt{y}) - F_X(-\sqrt{y})
\end{align*}

$$f_Y(y) = \begin{cases}
\frac{1}{2\sqrt{y}} [f_X(\sqrt{y}) + f_X(-\sqrt{y})], & y > 0 \\
0, & y \leq 0
\end{cases}$$
:::
