# 优化问题

## 牛顿法

$$
x_{n+1} = x_n - \frac{f^{\prime}(x_n)}{f^{\prime\prime}(x_n)}
$$

## 例题

\begin{problem}
计算$f(x)$的共轭函数, 以及共轭函数的定义域.

\begin{itemize}
    \item $f(x) = - \log x$
    \item $f(x) = e^x$
\end{itemize}
\end{problem}
\begin{solution}{解}
\begin{itemize}
\item $f(x) = - \log x$

\begin{align*}
    f^{*} (y) &= \sup_{x > 0}(y x + \log x) \\
              &= \begin{cases}
                  -1 - \log(-y) & y < 0 \\
                  \infty & \text{otherwise}
              \end{cases}
\end{align*}

\item $f(x) = e^x$

\begin{align*}
    f^{*} (y) &= \sup_{x \in \mathbb{R}}(y x - e^x) \\
              &= \begin{cases}
                  \infty & y < 0 \\
                  0 & y = 0 \\
                  y \ln(y) - y & y > 0
              \end{cases}
\end{align*}
\end{itemize}
\end{solution}

\begin{problem}
求解线性规划
\begin{align*}
\min&\ e^Tx \\
\text{s.t.}&\ Gx \le h \\
           &\ Ax = b
\end{align*}
的对偶函数，给出对偶问题。
\end{problem}
\begin{solution}{解}
Lagrange函数:

\begin{align*}
    L(x, \lambda, \nu) &= e^T x + \lambda^T (Gx - h) + \nu^T (Ax - b) \\
                       &= - \lambda^T h - \nu^T b + (e^T + \lambda^T G + \nu^T A) x
\end{align*}

对应的对偶函数为:

\[
    g(\lambda, \nu) = \inf_x L(x, \lambda, \nu) = \begin{cases}
        - \lambda^T h - \nu^T b & e^T + \lambda^T G + \nu^T A = 0 \\
        -\inf & \text{otherwise}
    \end{cases}
\]

对应的对偶问题为:

\begin{align*}
    \max &\ -\lambda^T h - \nu^T b \\
    s.t. &\ e^T + \lambda^T G + \nu^T A = 0 \\
         &\ \lambda, \nu \ge 0
\end{align*}
\end{solution}

\begin{problem}
求优化问题
\[
\arg \min_{x_1, x_2, x_3} x_1 x_2 x_3
\]
当$x_1$, $x_2$, $x_3$满足$x_1^2 + x_2^2 + x_3^2 = 1$的解。
\end{problem}
\begin{solution}{解}
Lagrange函数:

\begin{align*}
    L(x_1, x_2, x_3, \lambda) &= x_1x_2x_3 + \lambda(x_1^2 + x_2^2 + x_3^2 - 1)
\end{align*}

\[
    \nabla L = 0 \Rightarrow
    \begin{cases}
        \frac{\partial L}{\partial x_1} = x_2x_3 + 2\lambda x_1 = 0 \\
        \frac{\partial L}{\partial x_2} = x_1x_3 + 2\lambda x_2 = 0 \\
        \frac{\partial L}{\partial x_3} = x_1x_2 + 2\lambda x_3 = 0 \\
        \frac{\partial L}{\partial \lambda} = (x_1^2 + x_2^2 + x_3^2 - 1) = 0
    \end{cases} \Rightarrow
    \begin{cases}
        |x_1| = |x_2| = |x_3| = \frac{1}{\sqrt{3}} \\
        \lambda = \frac{1}{2 \sqrt{3}}
    \end{cases}
\]

因此$x_1$, $x_2$, $x_3$的解为:

\[
    \begin{cases}
        x_1 = \frac{1}{\sqrt{3}} \\
        x_2 = \frac{1}{\sqrt{3}} \\
        x_3 = -\frac{1}{\sqrt{3}}
    \end{cases},
    \begin{cases}
        x_1 = \frac{1}{\sqrt{3}} \\
        x_2 = -\frac{1}{\sqrt{3}} \\
        x_3 = -\frac{1}{\sqrt{3}}
    \end{cases}
\]
\end{solution}

\begin{problem}
已知矩阵$A \in \mathbb{R}^{p \times q}$, $B \in \mathbb{R}^{p \times r}$,
$rank(A) = min(p, q)$, 未知矩阵$X \in \mathbb{R}^{q \times r}$,
求以下优化问题。

若$p < q$, 求Frobenius范数最小的矩阵$X$, 使得$AX = B$, 即求解优化问题:

\begin{align*}
\min &\ f(X) = \frac{1}{2} ||X||_F^2 \\
\text{s.t.} &\ AX = B
\end{align*}
\end{problem}
\begin{solution}{解}
Lagrange函数:

\begin{align*}
L(X, \Lambda) &= \frac{1}{2} ||X||^2_F - \Lambda^T (AX - B) \\
              &= Tr(\frac{1}{2} X^T X) - Tr(\Lambda^T (AX - B))
\end{align*}

\[
    \nabla L = 0 \Rightarrow
    \begin{cases}
        \frac{\partial L}{\partial X} = X - A^T\Lambda  = 0 \\
        \frac{\partial L}{\partial \Lambda} = (AX - B)^T = 0
    \end{cases}
\]

因为$p < q \Rightarrow rank(A) = p$, 所以$AA^T$可逆。

\begin{align*}
    X &= A^T\Lambda \\
    A X &= A A^T \Lambda \\
    B &= A A^T \Lambda \\
    X &= A^T (A A^T)^{-1} B
\end{align*}
\end{solution}

\begin{problem}
梯度下降法是最常用的优化方法之一。考虑优化问题

\[
    \min f(x) = x_1^2 + x_2^2 + 2x_3^2
\]

证明: 在点$x_0 = (x_1, x_2, x_3)$处沿梯度方向迭代的最佳步长为:

\[
    \lambda = \frac{x_1^2 + x_2^2 + 4x_3^2}{2x_1^2 + 2x_2^2 + 16x_3^2}
\]
\end{problem}
\begin{solution}{证}
    即求解$\arg \min_\lambda f(x_0 - \lambda^T \nabla f(x_0))$

    \begin{align*}
        f(x_0 - \lambda^T \nabla f (x_0)) &=
        f(x_0 - \lambda^T (2x_1, 2x_2, 4x_2)^T) \\
        &= (1-\lambda_1)^2 x_1^2
         + (1-\lambda_2)^2 x_2^2
         + 2 (1-4\lambda)^2 x_3^2 \\
        \frac{\partial f(x_0 - \lambda^T \nabla f (x_0))}{\partial \lambda} &= 
        (8x_1^2 + 8x_2^2 + 64x_3^2)\lambda - (4x_1^2 + 4x_2^2 + 16x_3^2) = 0\\
        \lambda &= \frac{x_1^2 + x_2^2 + 4x_3^2}{2x_1^2 + 2x_2^2 + 16x_3^2}
    \end{align*}
\end{solution}