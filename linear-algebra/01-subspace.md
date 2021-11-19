# 子空间

## 向量子空间基础

<!-- Lec3 -->

### 向量子空间

`向量子空间!直和`{.idx}
\begin{define}
如果$\mathbb{Y}$中的每个向量$x$可唯一地表成
$x = y_1 + y_2 (y_1 \in \mathbb{Y}_1 , y_2 \in \mathbb{Y}_2 )$ 的形式，
则称$\mathbb{Y}$为
$\mathbb{Y}_1$与$\mathbb{Y}_2$的\textbf{直和}。
记作$\mathbb{Y} = \mathbb{Y}_1 + \mathbb{Y}_2$
或$\mathbb{Y} = \mathbb{Y}_1 \oplus \mathbb{Y}_2$
$\Leftrightarrow \mathbb{Y}_1 \cap \mathbb{Y}_2 = {0}$
\end{define}

### 仿射子空间

`仿射子空间`{.idx}
\begin{define}
\textbf{仿射子空间}即向量子空间偏移向量$x_0$
\end{define}

### 四个基本子空间

* 列空间$Col(A) = span(a_1, a_2, \ldots, a_n)$
* 行空间$Row(A) = Col(A^T)$
* 零空间$Null(A) = \{ x | Ax = 0\}$
* 左零空间$Null(A^T)$

#### 正交和正交补

\begin{mthm}
$Col(A) \cap Null(A^T) = \{0\}$
\end{mthm}

\begin{mthm}
$Col(A^T) \cap Null(A) = \{0\}$
\end{mthm}

\begin{mthm}
$Col(A)^{\bot} = Null(A^T)$
\end{mthm}

\begin{mthm}
$Col(A^T)^{\bot} = Null(A)$
\end{mthm}

## 投影

`正交投影`{.idx}
\begin{mthm}
正交投影矩阵为$B(B^T B)^{-1}B^T$, 其中$B$为是一个有序基底
\end{mthm}