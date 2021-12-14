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

### 正交和正交补

::: {.define latex=true}
$\forall v \in \mathbb{S}$, $\forall w \in \mathbb{T}$, 均有:
$v^T w = 0$
记做$\mathbb{S}$**`#垂直`**于$\mathbb{T}$, 或**`#正交`**.
:::

::: {.define latex=true}
**`#正交补`**: $\{ w \in \mathbb{R}^n | v^T w = 0, \forall v \in \mathbb{V} \}$
:::

::: {.example}
求$span{(1, 2, 0)^T, (0, 1, 2)^T}$的正交补空间:

$$
\begin{pmatrix}
1 & 0 \\ 
2 & 1 \\
0 & 2
\end{pmatrix}^T
x
= 0
\Rightarrow
x = k (4, -2, 1)^T
$$

正交补空间为$span\{ (4, -2, 1)^T \}$
:::

### 四个基本子空间

* 列空间$Col(A) = span(a_1, a_2, \ldots, a_n)$
* 行空间$Row(A) = Col(A^T)$
* 零空间$Null(A) = \{ x | Ax = 0\}$
* 左零空间$Null(A^T)$

::: {.mthm latex=true}
四个基本子空间的正交关系

* $Col(A) \cap Null(A^T) = \{0\}$
* $Col(A^T) \cap Null(A) = \{0\}$
* $Col(A)^{\bot} = Null(A^T)$
* $Col(A^T)^{\bot} = Null(A)$
:::

::: {.prop latex=true}
初等变换有关的性质

1. 一系列初等行变换不改变矩阵的行空间。
1. 一系列初等行变换不改变矩阵的零空间。
1. 一系列初等列变换不改变矩阵的列空间。
1. 一系列初等列变换不改变矩阵的左零空间。
:::

## 投影

`正交投影`{.idx}
\begin{mthm}
正交投影矩阵为$B(B^T B)^{-1}B^T$, 其中$B$为是一个有序基底
\end{mthm}

## 正交基

::: {.mthm latex=true}
**`#Gram-Schmidt 正交化`**:
$b_n = a_n
- \sum_{i=1}^{n-1}
\frac{\langle b_i, a_n \rangle}{\langle b_i, b_i \rangle}
b_i$
:::

::: {.example}
利用 Gram-Schmidt 正交化的过程，求下述矩阵列空间的一组正交基：
$$
\begin{pmatrix}
−10 & 13 & 7 & −11 \\
2 & 1 & −5 & 3 \\
−6 & 3 & 13 & −3 \\
16 & −16 & −2 & 5 \\
2 & 1 & −5 & −7
\end{pmatrix}
$$

$$
\begin{split}
    b_1 &= a_1
         = (-10, 2, -6, 16, 2)^T \\
    b_2 &= a_2 - \frac{\langle b_1, a_2 \rangle}{\langle b_1, b_1 \rangle} b_1
         = (3, 3, -3, 0, 3)^T \\
    b_3 &= a_3 - \sum_{i=1}^{2} \frac{\langle b_i, a_3 \rangle}{\langle b_i, b_i \rangle} b_i
         = (6, 0, 6, 6, 0)^T \\
    b_4 &= a_4 - \sum_{i=1}^{3} \frac{\langle b_i, a_4 \rangle}{\langle b_i, b_i \rangle} b_i
         = (0, 5, 0, 0, -5)^T
\end{split}
$$

单位化:

$$
\begin{split}
    e_1 &= (
     -\frac{1}{2}, \frac{1}{10}, -\frac{3}{10}, \frac{4}{5}, \frac{1}{10}
    )^T \\
    e_2 &= (
      \frac{1}{2}, \frac{1}{2}, -\frac{1}{2}, 0, \frac{1}{2}
    )^T \\
    e_3 &= (
      \frac{1}{\sqrt{3}}, 0, \frac{1}{\sqrt{3}}, \frac{1}{\sqrt{3}}, 0
    )^T \\
    e_4 &= (
      0, \frac{1}{\sqrt{2}}, 0, 0, -\frac{1}{\sqrt{2}}
    )^T
\end{split}
$$
:::