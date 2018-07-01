---
# vi: ft=pandoc.markdown
---

# 随机变量的数字特征

切比雪夫不等式`切比雪夫不等式`{.idx}
: $P\{|X - E(X)| \geq \varepsilon\} \leq \frac{D(X)}{\varepsilon^2}$, $P\{|X - E(X)| < \varepsilon\} \geq 1 - \frac{D(X)}{\varepsilon^2}$

## 数学期望

数学期望`数学期望`{.idx}
: $E(X) = \sum_{k = 1}^{\infty} x_k p_k$, $E(X) = \int_{-\infty}^{\infty} xf(x) dx$

   $E(Y) = E(g(X)) = \sum_{k = 1}^{\infty} g(x_k) pk$, $E(Y) = E(g(X)) = \int_{-\infty}^{\infty} g(x_k) pk$

### 数学期望性质

1. $E(C) = C$
1. $E(CX) = CE(X)$
1. $E(X + Y) = E(X) + E(Y)$
1. $E(XY) = E(X)E(Y)$ ($X$, $Y$相互独立)

## 方差

方差`方差`{.idx}
: $D(X) = \sum_{k = 1}^{\infty} [x_k - E(X)]^2 p_k$, $D(X) = \int_{-\infty}^{\infty} [x - E(X)]^2 f(x) dx$, $D(X) = E(X^2) - E^2(X)$

### 方差性质

1. $D(C) = 0$
1. $D(CX) = C^2 D(X)$
1. $D(X + Y) = D(X) + D(Y) + Cov(X, Y)$
1. $D(X) = 0 \Leftrightarrow P\{X = E(X)\} = 1$

## 协方差

协方差`协方差`{.idx}
: $Cov(X, Y) = E\{[X - E(X)][Y - E(Y)]\} = E(XY) - E(X)E(Y)$

1. $Cov(X, Y) = Cov(Y, X)$
1. $Cov(X, X) = D(X)$

$X$, $Y$独立时$Cov(X, Y) = 0$

相关系数
: $\rho_{XY} = \frac{Cov(X, Y)}{\sqrt{D(X)} \sqrt{D(Y)}}$
