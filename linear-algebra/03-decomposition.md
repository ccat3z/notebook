# 矩阵分解

## LU分解

1. 利用Gauss变换化矩阵$A$为阶梯型矩阵$U$.
   应确保每一步的主元均不为0 $\Leftrightarrow$ $k$ 阶顺序主子式不为 $0$.

   Gauss变换: $R_i = R_i \pm k R_j, i > j$,
   或可描述为
   $Q = \begin{pmatrix}
   1 & & & \\
   & 1 & & \\
   & k_3 & 1 & \\
   & k_4 & & 1
   \end{pmatrix}$

2. 对$I$执行与上一步的初等变换的逆变换$L$
3. $A = LU$

### 选主元的LU分解

## QR分解

## 谱分解/特征值分解

::: {.example}
矩阵的幂$A^k$

$$
A^k = (Q \Lambda Q^{-1})^k
$$

$\Lambda$为`#特征值`对角矩阵, $Q$为特征向量
:::

## 奇异值分解