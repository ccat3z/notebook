---
title: 线性代数
...

<!-- Lec2 -->

# 向量和矩阵基础

## 数据表示

`数域`{.idx}
\begin{define}
设$\mathbb{K}$是由一些数组成的集合，如果$\mathbb{K}$中包含$0$与$1$,
并且$\mathbb{K}$中任意两个数的和，差，积，商（除数不为零）仍在$\mathbb{K}$中，
则称$\mathbb{K}$是一个\textbf{数域}。
\end{define}

## 运算

\begin{mthm}
矩阵的乘积满足下列规律：

\begin{enumerate}
\item 结合律 $(AB)C = A(BC)$
\item 左分配律 $A(B + C) = AB + AC$, 右分配律 $(B + C)A = BA + CA$。
\end{enumerate}
\end{mthm}

\begin{mthm}
分块矩阵乘法, 若$A$的列的分法与$B$的行的分法一致, 就和矩阵乘法一致.
\end{mthm}

`初等矩阵`{.idx}
\begin{define}
由单位矩阵$I$经过一次初等行 (列) 变换得到的矩阵称为\textbf{初等矩阵}.
\end{define}

`逆矩阵`{.idx}
\begin{mthm}
\label{可逆矩阵与初等矩阵}

$n$阶矩阵$A$可逆的充分必要条件是它能表示成一些初等矩阵
$Q_1, Q_2 , \ldots , Q_m$的乘积:

\[
    A = Q_1 Q_2 \ldots Q_m
\]
\end{mthm}

`逆矩阵`{.idx}
由\ref{可逆矩阵与初等矩阵}可得: $(Q_1 Q_2 \ldots Q_m)^{-1} (A I) = (I A^{-1})$