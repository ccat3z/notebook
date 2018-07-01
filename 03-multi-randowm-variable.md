---
# vi: ft=pandoc.markdown
---

# 多维随机变量

联合分布函数`联合分布函数`{.idx}
: $F(x, y)$

边缘分布函数`边缘分布函数`{.idx}
: $F_X(x, y) = F_X(x, \infty)$

边缘分布概率`边缘分布概率`{.idx}
: $f_X(x) = \int_{\infty}^{\infty} f(x, y) dy$

边缘分布律`边缘分布律`{.idx}
: $p_{i \cdot} = \sum_{j = 0}^{\infty} p_{ij}$

条件分布律`条件分布律`{.idx}
: $P\{X = x_i \mid Y = y_i\} = \frac{p_{ij}}{p_{\cdot j}}$

条件概率密度`条件概率密度`{.idx}
: $P_{X \mid Y} (x \mid y) = \frac{f(x, y)}{f_Y(y)}$

::: {.example}
设数$X$在区间$(0, 1)$上随机地取值, 当观察到$X = x (0< x < 1)$时, 数$Y$在区间$(x, 1)$上随机地取值, 求$Y$的概率密度函数$f_Y(y)$

\begin{align*}
f_X(x) &= \begin{cases}
1, & 0 < x < 1 \\
0, & \text{其他}
\end{cases} \\
f_{Y \mid X}(y \mid x) &= \begin{cases}
\frac{1}{1 - x}, & x < y < 1 \\
0, & \text{其他}
\end{cases} \\
f(x, y) &= f_{Y \mid X}(y \mid x)f_X(x) = \begin{cases}
\frac{1}{1 - x}, & x < y < 1 \\
0, & \text{其他}
\end{cases} \\
f_Y(y) &= \int_{-\infty}^{\infty} f(x, y) dx \\
&= \begin{cases}
\int_0^y \frac{1}{1 - x} \frac{1}{1 - x} dx = -ln(1 - y), & 0 < y < 1 \\
0, & \text{其他}
\end{cases}
\end{align*}
:::

## 两个随机变量相互独立

\begin{align*}
P\{X \leq x, Y \leq y\} &= P\{X \leq x\}P\{Y \leq y\} \\
F(x, y) &= F_X(x) F_Y(y)
\end{align*}

## 两个随机变量的函数的分布

1. $Z = X + Y$

   \begin{align*}
   f_{X + Y}(z) &= \int_{-\infty}^{\infty} f(z - y, y) dy \\
   &= \int_{-\infty}^{\infty} f(x, z - x) dx
   \end{align*}

1. $Z = \frac{Y}{X}$

   $$f_{Y/X}(z) = \int_{-\infty}^{\infty} |x| f(x, xz) dx$$

1. $Z = XY$

   $$f_{XY}(z) = \int_{-\infty}^{\infty} \frac{1}{|x|} f(x, \frac{z}{x}) dx$$

1. $max\{X, Y\}, min\{X, Y\}$

   当$X$, $Y$独立时:

   $$F_{max}(z) = F_{X}(z)F_{Y}(z)$$

   $$F_{min}(z) = 1 - [1 - F_{X}(z)][1 - F_{Y}(z)]$$

*补充? 例题P87*
