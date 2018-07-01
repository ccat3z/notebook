---
# vi: ft=pandoc.markdown
---

# 大数定律和中心极限定理

## 大数定律

弱大数定理(辛钦大数定理)`弱大数定理`{.idx}`辛钦大数定理`{.idx}
: 对于$X_1, X_2, \ldots$相互独立且服从同一分布,

    $\lim_{n \rightarrow \infty} P\{|\frac{1}{n} \sum_{k = 1}^n X_k - \mu| < \varepsilon\} = 1, \forall \varepsilon > 0, E(X_k) = \mu$

    `重点!弱大数定理证明`{.idx}

    ::: {.example}
    证明弱大数定理

    $E(\frac{1}{n} \sum_{k = 1}^n X_k) = \frac{1}{n} \sum_{k = 1}^n E(X_k) = \frac{1}{n} n\mu = \mu$

    $D(\frac{1}{n} \sum_{k = 1}^n X_k) = \frac{1}{n} \sum_{k = 1}^n D(X_k) = \frac{1}{n} n\sigma^2 = \sigma^2$

    $1 \geq P\{|\frac{1}{n} \sum_{k = 1}^n X_k - \mu| < \varepsilon\} \geq 1 - \frac{\sigma^2}{\varepsilon^2}$

    $n \rightarrow \infty, P\{|\frac{1}{n} \sum_{k = 1}^n X_k - \mu| < \varepsilon\} \rightarrow 1$
    :::

伯努力大数定理`伯努力大数定理`{.idx}
: $\lim_{n \rightarrow \infty} P\{|\frac{f_A}{n} - p| < \varepsilon\}$ = 1

## 中心极限定理

独立同分布的中心极限定理`独立同分布的中心极限定理`{.idx}
: $\lim_{n \rightarrow \infty} P\{\frac{\sum_{k = 1}^{\infty} X_k - n\mu}{\sqrt{n} \sigma} \leq x\} = \Phi(x)$

李雅普诺夫定理
: *补充? P122*

棣莫弗—拉普拉斯定理
: 设随机变量$\eta_n \sim b(n, p)$

    $\lim_{n \rightarrow \infty} P\{\frac{\eta_n - np}{\sqrt{np(1 - p)}} \leq x\} = \Phi(x)$
