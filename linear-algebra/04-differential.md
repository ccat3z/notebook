# 向量和矩阵微分

::: {.mthm latex=true}
常见导数

\begin{align*}
(x^\mu)^{\prime} &= \mu x^{\mu - 1} \\
(a^x)^{\prime} &= a^x \ln a \\
(\log_a x)^{\prime} &= \frac{1}{x \ln a} \\
(f \circ g)^{\prime} &= f^{\prime} (g(x)) g^{\prime} (x)
\end{align*}
:::

::: {.mthm latex=true}
行列式对矩阵偏导: $\frac{\partial |X|}{\partial X} = X^{*}$

如果$|X| > 0$, $\frac{\partial |X|}{\partial X} = |X| X^{-T}$
:::

::: {.mthm latex=true}
逆矩阵求导: $\mathrm{d} X^{-1} = - X^{-1} \mathrm{d} X X^{-1}$
:::
