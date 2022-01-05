# 尾概率不等式

## Markov不等式

::: {.mthm latex=true}
非负随机变量$X$, $a > 0$

$$
P(X \ge a) \le \frac{E(X)}{a}
$$
:::

## Chebyshev不等式

::: {.mthm latex=true}
随机变量$X$, $r > 0$

$$
P(|X - E(X)| \ge r) \le \frac{Var(X)}{r^2}
$$
:::

\begin{problem}{45}{2}
    令$X_i (i = 1, 2, \ldots, n)$为一组独立同分布的随机变量,
    期望$\mu = E(X_i)$和方差$\delta^2 = E[(X_i - \mu)^2]$.
    如果定义$\overline{X} = \dfrac{1}{n} \sum\limits_{i=1}^{n}{X_i}$,
    证明

    \[P[|\overline{X} - \mu|\geq \epsilon|] \leq \frac{\delta^2}{n\epsilon^2}\]
\end{problem}
\begin{solution}{证明}
    $\overline{X}$的期望和方差为:
    \[
        E(\overline{X}) = \frac{1}{n}\sum_{i=1}^n{E(X)} = E(X) = \mu
    \]
    \[
        Var(\overline{X}) = \frac{1}{n^2} n Var(X_i) = \frac{Var(X_i)}{n}
        = \frac{\delta^2}{n}
    \]

    根据Chebyshev不等式,

    \begin{align*}
        P[|\overline{X} - E(\overline{X})| \geq \epsilon]
        & \leq \frac{Var(\overline{X})}{\epsilon^2} \\
        P[|\overline{X} - \mu| \geq \epsilon]
        & \leq \left.\frac{\delta^2}{n}\middle/{\epsilon^2}\right. \\
        & = \frac{\delta^2}{n\epsilon^2}
    \end{align*}
\end{solution}

## Chernoff不等式

::: {.mthm latex=true}
$X$二项分布

\begin{align*}
P(X < (1 - \delta) \mu) &< \left(\frac{e^{-\delta}}{(1-\delta)^{(1-\delta)}}\right)^u \\
P(X < (1 - \delta) \mu) &< \exp\left(\frac{-\mu\delta^2}{2}\right) \\
P(X > (1 + \delta) \mu) &< \left(\frac{e^{\delta}}{(1+\delta)^{(1+\delta)}}\right)^u \\
P(X > (1 + \delta) \mu) &< \exp\left(\frac{-\mu\delta^2}{4}\right)
\end{align*}
:::

\begin{problem}{45}{4}
    假设${X_i}$独立随机变量满足$P(X_i = 1) = p_i$和$P(X_i = 0) = 1 - p_i$,
    令$\mu = \sum\limits_{i=1}^n{p_i}$,
    定义随机变量$X = \sum\limits_{i=1}^n{X_i}$.
    证明以下结论:

    \begin{enumerate}[label= (\arabic*)]
        \item $P(X > (1 + \delta)\mu) < \left(\dfrac{e^\delta}{(1+\delta)^{(1+\delta)}}\right)^\mu$
        \item $P(X > (1 + \delta)\mu) < \exp(-\mu\delta^2 / 3)$
    \end{enumerate}
\end{problem}
\begin{solution}{证明}
    \begin{enumerate}[label= (\arabic*)]
        \item
        对 $t > 0$,
        \begin{align*}
            P(X > (1+\delta)\mu) &= P\big(\exp(tX) > \exp(t(1+\delta)\mu)\big) \\
                                   &< \frac{\prod\limits_{i=1}^n E(\exp(tX_i))}{\exp(t(1+\delta)\mu)}
        \end{align*}

        因为$1 - x < e^{-x}$, 所以
        \begin{align*}
            E(\exp(tX_i)) &= p_i e^t + (1 - p_i) = 1 - p_i (1 - e^{t}) \\
                           &< \exp(p_i(e^{t} - 1)) \\
            \prod_{i=1}^n E(\exp(t X_i)) &< \prod_{i=1}^n \exp(p_i (e^t - 1)) \\
                                          &= \exp(\mu(e^t - 1)) \\
            P(X > (1 + \delta \mu)) &< \frac{\exp(\mu(e^t - 1))}{\exp(t(1+\delta)\mu)} \\
                                    &= \exp(\mu (e^t - t - t\delta - 1))
        \end{align*}

        对$\mu (e^t - t - t\delta - 1)$关于$t$求导, 并令其为$0$.
        当$t = \ln(1 + \delta)$时, $\mu (e^t - t - t\delta - 1)$为最小值.
        所以
        \[
            P(X > (1 + \delta)\mu) < \left(\frac{e^{\delta}}{(1+\delta)^{(1+\delta)}}\right)^\mu
        \]

        \item
        \begin{align*}
            (1+\delta) \ln(1+\delta) &= (1+\delta)\left(\sum_{i=1}^\infty (-1)^{i - 1} \frac{\delta^i}{i}\right) \\
                                     &> \delta + \frac{\delta^2}{3} - \frac{\delta^2}{6} \\
            (1+\delta)^{(1+\delta)} &> \exp(\delta + \frac{\delta^2}{3})
        \end{align*}
        所以,
        \begin{align*}
            P(X > (1 + \delta)\mu) &< \left(\frac{e^{\delta}}{(1+\delta)^{(1+\delta)}}\right)^\mu \\
                                   &< \left(\frac{e^{\delta}}{\exp(\delta + \frac{\delta^2}{3})}\right)^\mu \\
                                   &= \exp\left(\frac{-\mu \delta^2}{3}\right)
        \end{align*}
    \end{enumerate}
\end{solution}

## Morris算法 (计数器)

- [ ] 优化过程?

1. 初始化计数器$X = 0$
1. 以$\frac{1}{2^X}$的概率`++`
1. 最终估计值为$2^X - 1$

### Morris+

运行多个Morris, 结果取平均值

### Morris++

运行多个Morris++, 结果取中位数

## 例题

\begin{problem}{45}{3}
    假设抛一枚均匀的硬币$n$次, 随机变量$X$定义为正面朝上的次数.
    \begin{enumerate}[label= (\arabic*)]
        \item 运用Chebyshev不等式给出事件$X < \dfrac{n}{4}$的概率上界;
        \item 运用Chernoff不等式给出事件$X < \dfrac{n}{4}$的概率上界.
    \end{enumerate}
\end{problem}
\begin{solution}{解}
    根据题意得$E(X) = \dfrac{n}{2}$, $Var(X) = \dfrac{n}{4}$

    \begin{enumerate}[label= (\arabic*)]
        \item 根据Chebyshev不等式:

        \begin{align*}
            P(X < \frac{n}{4})
            &= P(X > \frac{3n}{4}) \\
            &= P(X - \frac{n}{2} < \frac{n}{4}) \\
            &< P(|X - \frac{n}{2}| < \frac{n}{4}) \\
            &< \left.\frac{n}{4} \middle/ \frac{n}{4}^2\right. 
            = \frac{4}{n}
        \end{align*}

        \item 根据Chernoff不等式:

        \begin{align*}
            P(X < \frac{n}{4})
            &= P(X < (1 - \frac{1}{2}) \frac{n}{2}) \\
            &< \exp(\frac{-\frac{n}{2}\frac{1}{2}^2}{2}) = \exp(-\frac{n}{16})
        \end{align*}
    \end{enumerate}
\end{solution}