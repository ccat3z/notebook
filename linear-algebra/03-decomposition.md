# 矩阵分解

## LU分解

<!-- Lec 10 -->

主要用于求解$Ax = b$.

::: {.define latex=true}
**`#LU分解`**: $A = LU$, $L$下三角方阵, $U$上三角方阵.
:::

## Gauss变换

1. 利用Gauss变换化矩阵$A$为上三角阶梯型矩阵$U = QA$.
   应确保$k$ 阶顺序主子式始终不为 $0$ ($\Rightarrow$ 每一步的主元均不为$0$).

   Gauss变换: $R_i \pm = k R_j, i > j$,
   或可描述为
   $Q = \begin{pmatrix}
   1 & & & \\
   & 1 & & \\
   & k_3 & 1 & \\
   & k_4 & & 1
   \end{pmatrix}$

2. 对$I$执行与上一步的初等变换的逆变换, 下三角矩阵$L = Q^{-1} I$
3. $A = LU$

\begin{problem}
判定矩阵$C=\begin{bmatrix}3&2&-1\\-1&0&0\\-1&3&0\end{bmatrix}$
和 $B=\begin{bmatrix}0&2&-1\\-1&4&-1\\1&3&-5\end{bmatrix}$
能否进行LU分解, 为什么?
如果能分解, 试分解之.
\end{problem}

\begin{solution}{解}
矩阵$C$的顺序主子式均不为0, 可以进行LU分解.

$$
\begin{bmatrix}3&2&-1\\-1&0&0\\-1&3&0\end{bmatrix}
\xrightarrow[R_3 + \frac{1}{3} R_1]{R_2 + \frac{1}{3} R_1}
\begin{bmatrix}3&2&-1\\0&\frac{2}{3}&-\frac{1}{3}\\0&\frac{11}{3}&-\frac{1}{3}\end{bmatrix}
\xrightarrow{R_3 - \frac{11}{2} R_1}
\begin{bmatrix}3&2&-1\\0&\frac{2}{3}&-\frac{1}{3}\\0&0&\frac{3}{2}\end{bmatrix}
\rightarrow U
$$
$$
\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}
\xrightarrow{R_3 + \frac{11}{2} R_1}
\begin{bmatrix}1&0&0\\0&1&0\\0&\frac{11}{2}&1\end{bmatrix}
\xrightarrow[R_3 - \frac{1}{3} R_1]{R_2 - \frac{1}{3} R_1}
\begin{bmatrix}1&0&0\\-\frac{1}{3}&1&0\\-\frac{1}{3}&\frac{11}{2}&1\end{bmatrix}
\rightarrow L
$$

矩阵$B$的1阶主子式均为0, 因此$B$不可以进行LU分解.
\end{solution}

\begin{problem}
求矩阵$A=\begin{bmatrix}2&1&1\\1&2&1\\1&1&0\end{bmatrix}$的LU分解.
\end{problem}

\begin{solution}{解}
$$
\begin{bmatrix}2&1&1\\1&2&1\\1&1&0\end{bmatrix}
\xrightarrow{R_3 - R_2}
\begin{bmatrix}2&1&1\\1&2&1\\0&-1&-1\end{bmatrix}
\xrightarrow{R_2 - \frac{1}{2} R_1}
\begin{bmatrix}2&1&1\\0&\frac{3}{2}&\frac{1}{2}\\0&-1&-1\end{bmatrix}
\xrightarrow{R_3 + \frac{2}{3} R_2}
\begin{bmatrix}2&1&1\\0&\frac{3}{2}&\frac{1}{2}\\0&0&-\frac{2}{3}\end{bmatrix}
\rightarrow
U
$$

$$
\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}
\xrightarrow{R_3 - \frac{2}{3} R_2}
\begin{bmatrix}1&0&0\\0&1&0\\0&-\frac{2}{3}&1\end{bmatrix}
\xrightarrow{R_2 + \frac{1}{2} R_1}
\begin{bmatrix}1&0&0\\\frac{1}{2}&1&0\\0&-\frac{2}{3}&1\end{bmatrix}
\xrightarrow{R_3 + R_2}
\begin{bmatrix}1&0&0\\\frac{1}{2}&1&0\\\frac{1}{2}&\frac{1}{3}&1\end{bmatrix}
\rightarrow
L
$$
\end{solution}

### 选主元的LU分解

如果得到$U$不存在主元为$0$的上三角阵, 可以使用行交换$P$进行选主元 (重排).
即$U^{\prime} = PU = PQA \Rightarrow P (PQ)^{-1} PU = PA$.

## QR分解

<!-- Lec 11 -->

::: {.define latex=true}
**`#QR分解`** (`#正交三角分解`): $A = Q \begin{pmatrix}R\\O\end{pmatrix}$.
$A \in \mathbb{R}^{m \times n} (m \ge n)$,
$\text{正交矩阵}Q \in \mathbb{R}^{m \times m}$, $Q$
$\text{上三角矩阵}R \in \mathbb{R}^{n \times n}$.
:::

`#QR`分解主要用于解决最小二乘问题, 矩阵特征值计算.

### 基于Gram-Schmidt正交化

使用`#Gram-Schmidt`对满秩矩阵$A$正交化得到正交基$Q = (q_1, q_2, \ldots, q_m)$,
再用$Q$表示$A = QR$.

### Householder

TODO: After lec 8

### Givens

TODO: After lec 8

## 谱分解/特征分解

<!-- Lec 12 -->

### 特征分解

::: {.define latex=true}
**`#特征分解`**: $A = Q \Lambda Q^{-1}$,
$\Lambda$为`#特征值`对角矩阵, $Q$为特征向量
:::

::: {.example}
矩阵的幂$A^k$

$A^k = (Q \Lambda Q^{-1})^k$
:::

### 谱分解

::: {.define latex=true}
对称矩阵$A$, 如果$A$可以本分解为$A = Q \Lambda Q^T$.
其中$Q$为单位化特征向量矩阵,
$\Lambda$是特征值对角矩阵.
称为**`#谱分解`**.
:::

### Cholesky分解

``` {=latex}
\begin{problem}
求对称正定矩阵
$$
A = \begin{bmatrix}5&2&-4\\2&1&-2\\-4&-2&5\end{bmatrix}
$$
的不带平方根的Cholesky分解.
\end{problem}

\begin{solution}{解}
$$
D_1 = A_{11} = 5
$$
$$
L_{21} = \frac{1}{D_1} A_{21}
= \frac{1}{5} \times 2
= \frac{2}{5}
,\ 
L_{31} = \frac{1}{D_1} A_{31}
= \frac{1}{5} \times (-4)
= -\frac{4}{5}
$$
$$
D_2 = A_{22} - L^2_{21} D_1
= 1 - \left( \frac{2}{5} \right)^2 \times 5
= \frac{1}{5}
$$
$$
L_{32} = \frac{1}{D_2} \left(A_{32} - L_{31} L_{21} D_1\right)
= 5 \left( -2 + \frac{4}{5} \times \frac{2}{5} \times 5 \right)
= -2
$$
$$
D_3 = A_{33} - \sum_{k=1}^2 L^2_{3k} D_k
= 5 - \left(\frac{4}{5}\right)^2 \times 5 - \left(2\right)^2 \times \frac{1}{5}
= 1
$$
$$
A
= LDL^T
=
\begin{bmatrix}
   1 & 0 & 0 \\
   \frac{2}{5} & 1 & 0 \\
   -\frac{4}{5} & -2 & 1
\end{bmatrix}
\begin{bmatrix}
   5 & 0 & 0 \\
   0 & \frac{1}{5} & 0 \\
   0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
   1 & 0 & 0 \\
   \frac{2}{5} & 1 & 0 \\
   -\frac{4}{5} & -2 & 1
\end{bmatrix}^T
$$
\end{solution}
```

## 奇异值分解

<!-- Lec 13 -->