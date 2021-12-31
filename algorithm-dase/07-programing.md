# 整数规划

## 表示约束

### 或

\begin{example}{
    $x + y \le 3$ or $x - y \ge 4$
}
引入足够大的数$M$和$\omega \in \{0, 1\}$.

\[
    \begin{cases}
        x + y \le 3 + M\omega \\
        x - y \ge 4 - M(1 - \omega)
    \end{cases}   
\]
\end{example}

### 分段函数

\begin{problem}{218}{3}
将下面的非线性规划问题重写成整数规划问题。

\[
f(x) =
\begin{cases}
    10x, & \text{如果} 0 \le x \le 50 \\
    500, & \text{如果} 51 \le x \le 100 \\
    5x, & \text{如果} x \ge 101 \\
\end{cases}
\]
\end{problem}
\begin{solution}{解}
引入0-1变量$w_1$, $w_2$, $w_3$, 整数变量$x_1$, $x_2$, $x_3$, 满足:

\[
    \begin{split}
        w_1 &= \begin{cases}
            1 & 0 \le x \le 50 \\
            0 & \text{其他}
        \end{cases} \\
        w_2 &= \begin{cases}
            1 & 51 \le x \le 100 \\
            0 & \text{其他}
        \end{cases} \\
        w_3 &= \begin{cases}
            1 & 101 \le x \\
            0 & \text{其他}
        \end{cases}
    \end{split}
    \begin{split}
        x_1 &= \begin{cases}
            x & 0 \le x \le 50 \\
            0 & \text{其他}
        \end{cases} \\
        x_2 &= \begin{cases}
            x & 51 \le x \le 100 \\
            0 & \text{其他}
        \end{cases} \\
        x_3 &= \begin{cases}
            x & 101 \le x \\
            0 & \text{其他}
        \end{cases}
    \end{split}
\]

对应约束条件可改写为:

\begin{align*}
    f(x) =& 10 x_1 + 500 w_2 + 5 x_3 \\
          & 0 \le x_1 \le 50w_1 \\
          & 51 w_2 \le x_2 \le 100 w_2 \\
          & 101 w_3 \le x_3 \\
          & w_1, w_2, w_3 \in \{0, 1\} \\
          & x_1 + x_2 + x_3 = x \\
          & x_1, x_2, x_3 \in Z
\end{align*}
\end{solution}

## 线性规划

### 标准型

所有的约束都是不等式

\begin{example}{
\begin{align*}
\min &\ -2x_1 + 3x_2 \\
\text{约束条件} &\ x_1 + x_2 = 7 \\
                &\ x_1 - 2x_2 <= 4 \\
                &\ x_1 >= 0
\end{align*}
}
\begin{enumerate}
\item 目标函数可能是最小化，而不是最大化

$$\min -2 x_1 + 3x_2 \rightarrow \max 2 x_1 + 3x_2$$

\item 可能有变量不具有非负约束. 将$x_2$改为$x_2^{\prime} - x_2^{\prime\prime}$

\begin{align*}
\text{约束条件} &\ x_1 + x_2^{\prime} - x_2^{\prime\prime} = 7 \\
                &\ x_1 - x_2^{\prime} - x_2^{\prime\prime} <= 4 \\
                &\ x_1, x_2^{\prime}, x_2^{\prime\prime} >= 0
\end{align*}

\item 可能有等式约束. 转化成一组不等式

$$
x_1 + x_2^{\prime} - x_2^{\prime\prime} = 7
\rightarrow
x_1 + x_2^{\prime} - x_2^{\prime\prime} \ge 7
x_1 + x_2^{\prime} - x_2^{\prime\prime} \le 7
$$

\item 可能有不等式约束，但不是小于等于号，而是大于等于号
\end{enumerate}

最终结果:

\begin{align*}
\max &\ 2x_1 - 3(x_2^{\prime} - x_2^{\prime\prime}) \\
\text{约束条件}
&= x_1 + x_2^{\prime} - x_2^{\prime\prime} \ge 7 \\
&= x_1 + x_2^{\prime} - x_2^{\prime\prime} \le 7 \\
&\ x_1, x_2^{\prime}, x_2^{\prime\prime} >= 0
\end{align*}
\end{example}

### 松弛型

约束都是等式（除了要求变量非负的约束）. 为每一个标准型中的不等式引入一个变量.
例如:

$$
x + y \ge 3 \rightarrow z = x + y  - 3, z \ge 0
$$

### 单纯型法

See [wikipedia](https://zh.wikipedia.org/wiki/%E5%8D%95%E7%BA%AF%E5%BD%A2%E6%B3%95#%E5%AE%9E%E4%BE%8B).

## 例题

\begin{problem}{218}{6}
给定下面的整数规划问题:

\begin{align*}
    IP(1) & \\
     \max &\  10 x_1 + 4 x_2 + 9 x_3 \\
     \text{约束条件:} &\  5 x_1 + 4 x_2 + 3 x_3 \le 9 \\
          &\  0 \le x_i \le 1, x_i \in Z, 1 \le i \le 3
\end{align*}

\begin{enumerate}
\item 写出关于$IP(1)$的线性规划松弛。
\item 如果$x_1 = 1$, 试找出对应整数规划问题的上界。
\item 使用分支定界方法求解$IP(1)$
\end{enumerate}
\end{problem}
\begin{solution}{解}
\begin{enumerate}
\item 写出关于$IP(1)$的线性规划松弛。

\begin{align*}
     \max &\  10 x_1 + 4 x_2 + 9 x_3 \\
     \text{约束条件:} &\  5 x_1 + 4 x_2 + 3 x_3 \le 9 \\
          &\  0 \le x_i \le 1, 1 \le i \le 3
\end{align*}

\item 如果$x_1 = 1$, 试找出对应整数规划问题的上界。

当$x_1 = 1$时, $IP(1)$可化为:

\begin{align*}
     \max &\  10 + 4 x_2 + 9 x_3 \\
     \text{约束条件:} &\  4 x_2 + 3 x_3 \le 4 \\
          &\  0 \le x_i \le 1, x_i \in Z, 2 \le i \le 3
\end{align*}

此时$(x_2, x_3)$的可行域为$\{(0, 0), (1, 0), (0, 1)\}$。
易得当$(x_2, x_3) = (0, 1)$时$10 + 4 x_2 + 9 x_3$取最大值$19$。

\item 使用分支定界方法求解$IP(1)$

令$Z_I = - \infty$

$LP(1)$的最优解为:

\[
    x_1 = 1, x_2 = \frac{1}{4}, x_3 = 1, Z_{LP(1)} = 20
\]

由于$Z_{LP(1)} > Z_I$且非整数解，
选择$x_1 = 1$时的节点$IP(2)$和$x_1 = 0$时的节点$IP(3)$。

由题2可得, $IP(2)$的最优解为:

\[
    x_1 = 1, x_2 = 0, x_3 = 1, Z_{IP(2)} = 19
\]

$Z_{IP(2)} > Z_I$, 将$Z_I$设置为$19$。

求$IP(3)$, $IP(3)$可表示为:

\begin{align*}
     \max &\ 4 x_2 + 9 x_3 \\
     \text{约束条件:} &\  4 x_2 + 3 x_3 \le 9 \\
          &\  0 \le x_i \le 1, x_i \in Z, 2 \le i \le 3
\end{align*}

此时$(x_2, x_3)$的可行域为$\{(0, 0), (1, 0), (0, 1), (1, 1)\}$。
易得当$(x_2, x_3) = (1, 1)$时$4 x_2 + 9 x_3$取最大值$13$，
即$Z_{IP(3)} = 13$，小于当前$Z_I$。

算法终止，$IP(1)$的最优解为:

\[
    x_1 = 1, x_2 = 0, x_3 = 1, Z_{IP(1)} = 19
\]
\end{enumerate}
\end{solution}